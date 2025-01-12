import requests
import time
base_url="https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM/sendMessage"

word = ["Hello", "Test 1", "Test 2", "Test 3"]

for w in word:
    # time.sleep(10)
    parameters = {
        "chat_id" : "-1002439463012",
        "text" : w
    }
    
    resp = requests.get(base_url, data=parameters)
    print(resp.text)