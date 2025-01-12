import requests
import time
base_url="https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM/sendPhoto"




parameters = {
    "chat_id" : "-1002439463012",
    "photo" : "/home/suneater/Remt/mengeang.jpg"
}

resp = requests.get(base_url, data=parameters)
print(resp.text)