import requests
import time
base_url="https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM/sendAudio"

my_file = open("thaok.ogg", "rb")

parameters = {
    "chat_id" : "-1002439463012",
    "caption" : "hello"
}

files = {
    "audio" : my_file
}

resp = requests.get(base_url, data=parameters, files=files)
print(resp.text)