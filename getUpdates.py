import requests
base_url="https://api.telegram.org/bot7285184565:AAHepRbNrrI_57rh-gFPQkIqesGHbmCtLuM/getUpdates"
# getUpdates
parameters = {
    "offset" : "817441096",
    "limit " : "4"
}

resp = requests.get(base_url, data=parameters)
print(resp.text)