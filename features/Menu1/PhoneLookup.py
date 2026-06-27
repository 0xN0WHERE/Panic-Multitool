from config.settings import *

def LookupPhone():
        os.system("cls")
        Slow(lookup_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Phone number lookup{Style.RESET_ALL}")
        print("")

        number = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Phone number (with country code) -> {Style.RESET_ALL}")

        try:
            phoneNumber = phonenumbers.parse(number)

            try:
                if number_type(phoneNumber) == 0:
                    PhoneType = "Fixed Line"
                elif number_type(phoneNumber) == 1:
                    PhoneType = "Mobile"
                elif number_type(phoneNumber) == 2:
                    PhoneType = "Fixed Line or Mobile"
                elif number_type(phoneNumber) == 3:
                    PhoneType = "Toll free"
                elif number_type(phoneNumber) == 4:
                    PhoneType = "Premium Rate"
                elif number_type(phoneNumber) == 5:
                    PhoneType = "Shared Cost"
                elif number_type(phoneNumber) == 6:
                    PhoneType = "Voip"
                elif number_type(phoneNumber) == 7:
                    PhoneType = "Personal Number"
                elif number_type(phoneNumber) == 8:
                    PhoneType = "Pager"
                elif number_type(phoneNumber) == 9:
                    PhoneType = "Universal Access Number"
                elif number_type(phoneNumber) == 10:
                    PhoneType = "Voicemail"
                elif number_type(phoneNumber) == -1:
                    PhoneType = "Unknown"

                TimeList = timezone.time_zones_for_number(phoneNumber)

                TzDisplay = TimeList[0] if TimeList else "Unknown"

                print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searchig for information... {Style.RESET_ALL}")
                print("")
                time.sleep(1.5)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Valid                : {Style.RESET_ALL}{is_valid_number(phoneNumber)}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} International number : {Style.RESET_ALL}{format_number(phoneNumber, PhoneNumberFormat.INTERNATIONAL)}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} National number      : {Style.RESET_ALL}{format_number(phoneNumber, PhoneNumberFormat.NATIONAL)}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Type                 : {Style.RESET_ALL}{PhoneType}")
                print("")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Timezone             : {Style.RESET_ALL}{TzDisplay}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Region               : {Style.RESET_ALL}{region_code_for_number(phoneNumber)}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Location             : {Style.RESET_ALL}{geocoder.description_for_number(phoneNumber, 'en')}")
                time.sleep(0.05)
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Provider             : {Style.RESET_ALL}{carrier.name_for_number(phoneNumber, 'en')}")
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

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
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to grab information{Style.RESET_ALL}")
                time.sleep(2) 

        except Exception:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid phone number{Style.RESET_ALL}")
            time.sleep(2)
        