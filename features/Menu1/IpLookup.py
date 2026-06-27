from config.settings import *

def IPLookup():
        os.system("cls")
        Slow(map_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}IP lookup{Style.RESET_ALL}")
        print("")
        target_ip = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Ip -> {Style.RESET_ALL}")

        try:
            response = requests.get(f"http://ip-api.com/json/{target_ip}")
            api = response.json()

            status = "Valid" if api.get('status') == "success" else "Invalid"
            country = api.get('country', "None")
            country_code = api.get('countryCode', "None")
            region = api.get('regionName', "None")
            zip_code = api.get('zip', "None")
            city = api.get('city', "None")
            latitude = api.get('lat', "None")
            longitude = api.get('lon', "None")
            timezone = api.get('timezone', "None")
            isp = api.get('isp', "None")
            org = api.get('org', "None")
            as_host = api.get('as', "None")

            
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searchig for information... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Status       :{Style.RESET_ALL} {status}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Country      :{Style.RESET_ALL} {country}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Country code :{Style.RESET_ALL} {country_code}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Region       :{Style.RESET_ALL} {region}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Zip          :{Style.RESET_ALL} {zip_code}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} City         :{Style.RESET_ALL} {city}")#
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Latitude     :{Style.RESET_ALL} {latitude}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Longitude    :{Style.RESET_ALL} {longitude}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Timezone     :{Style.RESET_ALL} {timezone}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Isp          :{Style.RESET_ALL} {isp}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Org          :{Style.RESET_ALL} {org}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} As host      :{Style.RESET_ALL} {as_host}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} IP unavailable{Style.RESET_ALL}")
            time.sleep(2)
        