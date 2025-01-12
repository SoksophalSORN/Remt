import requests
import time
import pandas as pd

# Load the QnA dataset
url = "https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv"
df = pd.read_csv(url, sep="\t")

# Telegram Bot API URL
base_url = "https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM"

# Global variable to store the allowed group chat_id
allowed_chat_id = None


def get_initial_offset():
    """
    Fetch the latest updates to clear unprocessed messages and return the latest offset.
    """
    resp = requests.get(base_url + "/getUpdates")
    data = resp.json()

    if "result" in data and data["result"]:
        # Return the latest update_id + 1 to clear all previous messages
        return data["result"][-1]["update_id"] + 1
    return 0


def read_msg(offset):
    """
    Read new messages from Telegram and process them.
    """
    global allowed_chat_id

    parameters = {
        "offset": offset
    }

    resp = requests.get(base_url + "/getUpdates", params=parameters)
    data = resp.json()

    for result in data.get("result", []):  # Safely handle missing or empty 'result'
        if "message" in result and isinstance(result["message"], dict):
            chat_id = result["message"]["chat"]["id"]
            if "text" in result["message"]:  # Check if 'text' exists in the message
                message_text = result["message"]["text"]

                if message_text == "/start":  # Check for the /start command
                    if allowed_chat_id is None:
                        allowed_chat_id = chat_id  # Set allowed chat ID
                        sendMessage(chat_id, "Bot started! This group can now send queries.")
                    elif allowed_chat_id == chat_id:
                        sendMessage(chat_id, "The bot is already active in this group.")
                    else:
                        sendMessage(chat_id, "The bot is already active in another group.")
                elif allowed_chat_id == chat_id:
                    sendMessage(chat_id, message_text)
                else:
                    print(f"Ignored message from unallowed chat: {chat_id}")
            else:
                print("Message does not contain text:", result["message"])
        else:
            print("Result does not contain a valid 'message' key:", result)

    if data.get("result"):  # Check if 'result' is not empty
        return data["result"][-1]["update_id"] + 1

    return offset  # Return the same offset if no new updates


def auto_answer(message):
    """
    Provide an answer based on the question in the dataframe.
    """
    answer = df.loc[df['Question'].str.lower() == message.lower()]

    if not answer.empty:
        answer = answer.iloc[0]['Answer']
        return answer
    else:
        return "Sorry, I could not understand you !!!"


def sendMessage(chat_id, message):
    """
    Send a message to a Telegram chat.
    """
    answer = auto_answer(message)

    parameters = {
        "chat_id": chat_id,  # Use the dynamic chat ID
        "text": answer
    }
    resp = requests.get(base_url + "/sendMessage", params=parameters)  # Use 'params' for GET request
    print(resp.text)


# Main loop
offset = get_initial_offset()  # Clear unprocessed messages
while True:
    offset = read_msg(offset)
    time.sleep(1)  # Optional delay to avoid hitting the rate limit
