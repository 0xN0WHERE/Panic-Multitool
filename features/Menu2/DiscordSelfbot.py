from config.settings import *
from features.Menu2.SelfbotMenu.Unfriender import UnfriendEveryone
from features.Menu2.SelfbotMenu.Messager import MessageEveryone
from features.Menu2.SelfbotMenu.DmCloser import CloseAllDms
from features.Menu2.SelfbotMenu.ServerLeaver import LeaveAllServers
from features.Menu2.SelfbotMenu.GroupLeaver import LeaveAllGroups
from features.Menu2.SelfbotMenu.Nuker import NukeToken

BaseURL = "https://discord.com/api/v9"
            
def MainSelfbot(token):
     while True:
        os.system("cls")
        Slow(Selfbot_banner)
        Slow(SelfbotMenu)
        print("")

        option = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{username}{Fore.GREEN})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
        
        if option == "1" or option == "01":
            asyncio.run(UnfriendEveryone(HEADERS={"Authorization": token}))
        elif option == "2" or option == "02":
            asyncio.run(MessageEveryone(HEADERS={"Authorization": token}))
        elif option == "3" or option == "03":
            asyncio.run(CloseAllDms(HEADERS={"Authorization": token}))
        elif option == "4" or option == "04":
            asyncio.run(LeaveAllGroups(HEADERS={"Authorization": token}))
        elif option == "5" or option == "05":
            asyncio.run(LeaveAllServers(HEADERS={"Authorization": token}))
        elif option == "5" or option == "05":
            asyncio.run(LeaveAllServers(HEADERS={"Authorization": token}))
        elif option == "6" or option == "06":
            asyncio.run(NukeToken(HEADERS={"Authorization": token}))
        elif option == "7" or option == "07":
            break

def RunMenu():
        os.system("cls")
        Slow(Selfbot_banner)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        time.sleep(0.05)
        print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2} {Fore.GREEN}Your token :{Style.RESET_ALL} {MyToken()}")
        time.sleep(0.05)
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print("")
        RawToken = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Token -> {Style.RESET_ALL}")

        try:
            headers = {
                "Authorization": RawToken
            }

            r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)

            if r.status_code in succesStatus:
                DcToken = RawToken
            else:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid token{Style.RESET_ALL}")
                time.sleep(2)
                return

            MainSelfbot(token=DcToken)
        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Error running selfbot{Style.RESET_ALL}")
            time.sleep(2)