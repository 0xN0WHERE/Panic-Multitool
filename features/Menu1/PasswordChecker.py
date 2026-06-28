from config.settings import *

def CheckPassword():
        os.system("cls")
        Slow(password_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Password checker{Style.RESET_ALL}")
        print("")

        Password = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Password -> {Style.RESET_ALL}")

        try:
            CharSize = 0
            if any(c.islower() for c in Password):
                CharSize += 26
            if any(c.isupper() for c in Password):
                CharSize += 26
            if any(c.isdigit() for c in Password):
                CharSize += 10
            if any(c in string.punctuation for c in Password):
                CharSize += len(string.punctuation)
            if CharSize == 0:
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid password{Style.RESET_ALL}")

            combinations = int(CharSize ** len(Password))
            guesses_per_second = int(10000)
            seconds = combinations / guesses_per_second
            
            if seconds < 60:
                TimeEstimate = f"{seconds:.2f} Seconds to bruteforce"
            elif seconds < 3600:
                TimeEstimate = f"{seconds/60:.2f} Minutes to bruteforce"
            elif seconds < 86400:
                TimeEstimate = f"{seconds/3600:.2f} Hours to bruteforce"
            elif seconds < 31536000:
                TimeEstimate = f"{seconds/86400:.2f} Days to bruteforce"
            else:
                TimeEstimate = f"{seconds/31536000:.2f} Years to bruteforce"

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Checking password... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Time to bruetforce :{Style.RESET_ALL} {TimeEstimate}")
            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            print("")
            print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Main Menu{Style.RESET_ALL}")
            print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Exit{Style.RESET_ALL}")
            print("")

            command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{username}{Fore.GREEN})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")

            if command == "1" or command == "01":
                pass
            elif command == "2" or command == "02":
                sys.exit()
            else:
                pass

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to check password{Style.RESET_ALL}")
            time.sleep(2)
        