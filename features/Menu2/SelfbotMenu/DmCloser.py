from config.settings import *

async def CloseAllDms(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Dm selfbot{Style.RESET_ALL}")
    time.sleep(0.05)

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseURL}/users/@me/channels", headers=HEADERS
        )

        if res.status_code in succesStatus:
            channels = res.json()

            if not channels:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No open dms found{Style.RESET_ALL}")
                time.sleep(2)
                return

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Closing all dms... {Style.RESET_ALL}")
            time.sleep(1.5)
            try:
                print("")
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                time.sleep(0.05)

                for channel in channels:
                    recipients = channel.get("recipients", [])

                    if recipients:
                        DmUser = recipients[0].get("username", "Unknown")
                    else:
                        DmUser = "Unknown"

                    dm_id = channel["id"]
                    try:
                        delete_res = await client.delete(
                                f"{BaseURL}/channels/{dm_id}",
                                headers=HEADERS)
                        
                        if delete_res.status_code in succesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Closed dm       : {Style.RESET_ALL}{DmUser} - {dm_id}")
                        elif delete_res.status_code == 429:
                            Retry = delete_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to close : {Style.RESET_ALL}{DmUser} - {dm_id}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to close : {Style.RESET_ALL}{DmUser} - {dm_id}")
    
                time.sleep(0.05)
                print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

            except Exception:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Dms unavailable{Style.RESET_ALL}")
                time.sleep(2)
                return
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to close all dms{Style.RESET_ALL}")
            time.sleep(2)
            return
        
        print("")
        print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Selfbot menu{Style.RESET_ALL}")
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