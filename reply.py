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
        if "message" in result and "text" in result["message"] and "Different Generation" in result["message"]["text"]:
            sendMessage()
        if "message" in result and "text" in result["message"] and "Ah K'theay" in result["message"]["text"]:
            sendMessage1()
        if "message" in result and "text" in result["message"] and "Ah pengly" or "ah pengly" or "Ah Pengly" in result["message"]["text"]:
            sendMessage2()
        if "message" in result and "text" in result["message"] and "Ah Kok" in result["message"]["text"]:
            sendMessage3()
    
    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def sendMessage():
    # time.sleep(10)
    parameters = {
        "chat_id" : "-1002439463012",
        "text" : "Thoak" 
    }
    
    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)

def sendMessage1():
    # time.sleep(10)
    parameters = {
        "chat_id" : "-1002439463012",
        "text" : "Kdmv ah k'theay" 
    }
    
    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)

def sendMessage3():
    # time.sleep(10)
    parameters = {
        "chat_id" : "-1002439463012",
        "text" : "Jorb Kok" 
    }
    resp = requests.get(base_url + "/sendMessage", data=parameters)
    print(resp.text)

def sendMessage2():
    # time.sleep(10)
    my_file = open("m.jpg", "rb")
    parameters = {
        "chat_id" : "-1002439463012",
        "caption" : "Jorb kok" 
    }
    
    files = {
    "photo" : my_file
    }

    resp = requests.get(base_url + "/sendPhoto", data=parameters, files=files)
    print(resp.text)


offset = 0

while True:
    offset = getMessage(offset)
