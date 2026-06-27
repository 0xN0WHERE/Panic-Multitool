from config.settings import *

def OpenOsintFramwork():
        os.system("cls")
        Slow(osint_banner)
        time.sleep(1.5)
        os.system("cls")

        try:
            webbrowser.open("https://osintframework.com/")

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Website is unreachable{Style.RESET_ALL}")
            time.sleep(2)
        