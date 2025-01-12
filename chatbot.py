import requests
import pandas as pd

url = "https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv"

df = pd.read_csv(url, sep="\t")

base_url = "https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM"

def read_msg(offset):
    parameters = {
        "offset" : offset
    }
    
    resp = requests.get(base_url + "getUpdates", data = parameters)
    data = resp.json()

    print(data)

    for result in data["result"]:
        if "message" in result and "text" in result["message"] and "Hello" in result["message"]["text"]:
            sendMessage(result["message"]["text"])
    
    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def auto_answer(message):
    answer = df.loc[df['Question'].str.lower() == message.lower]

    if not answer.empty:
        answer = answer.iloc[0]['Answer']
        return answer
    else:
        return "Sorry, I could not understand you !!! I am still learning and try to get better in answering."

def sendMessage(message):
    answer = auto_answer(message)

    parameters = {
        "chat_id" : "-1002439463012",
        "caption" : answer
    }
    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)


offset = 0

while True:
    offset = read_msg(offset)
