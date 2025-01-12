import requests
base_url="https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM"
# getUpdates
def getMessage(offset):
    
    parameters = {
        "offset" : offset
    }
    resp = requests.get(base_url + "/getUpdates", data=parameters)
    data = resp.json()
    
    for result in data["result"]:
        if "text" in result["message"]:
            message_text = result["message"]["text"]
            sendMessage(message_text)
        else:
            print("Message does not contain text:", result["message"])
    
    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def sendMessage(message):
    # time.sleep(10)
    parameters = {
        "chat_id" : "-1002439463012",
        "text" : message
    }
    
    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)


offset = 0

while True:
    offset = getMessage(offset)
