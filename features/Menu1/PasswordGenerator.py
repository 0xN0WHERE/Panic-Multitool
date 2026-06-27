from config.settings import *

def GeneratePassword():
        os.system("cls")
        Slow(password_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Password generator{Style.RESET_ALL}")
        print("")
        try:
            length = int(input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Number of characters -> {Style.RESET_ALL}"))
        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid number{Style.RESET_ALL}")
            time.sleep(2)
            return

        try:
            Uppercase = string.ascii_uppercase
            Lowercase = string.ascii_lowercase
            Numbers = string.digits
            SpecialCharacters = "!#$%&'()*+,-.:<=>?@\_|"

            allCharacters = Uppercase + Lowercase + Numbers + SpecialCharacters

            password = "".join(random.choice(allCharacters) for _ in range(length))

            if length > 100:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{bracketclosed} {Fore.GREEN}Maximum 100 characters{Style.RESET_ALL}")
                time.sleep(2)
                return
            elif length < 1:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{bracketclosed} {Fore.GREEN}Minimum 1 character{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Generating password... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Password :{Style.RESET_ALL} {password}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to generate password{Style.RESET_ALL}")
            time.sleep(2)
        