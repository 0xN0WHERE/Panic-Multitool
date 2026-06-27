from config.settings import *

async def CloneChannels(targetId, cloneId, headers, rolemap):
    channels = requests.get(f"{BaseURL}/guilds/{targetId}/channels", headers=headers)
    DelChannels = requests.get(f"{BaseURL}/guilds/{cloneId}/channels", headers=headers)

    DelChannelData = DelChannels.json()

    if channels.status_code in succesStatus:
        for DelChannel in DelChannelData:
            DelChannelName = DelChannel["name"]
            DelChannelID = DelChannel["id"]
            
            rDel = requests.delete(
                f"{BaseURL}/channels/{DelChannelID}",
                headers=headers
            )

            if rDel.status_code == 200 or rDel.status_code == 204:
                if DelChannel["type"] == 4:
                    print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Deleted category          : {Style.RESET_ALL}{DelChannelName} - {DelChannelID}")
                else:
                    print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Deleted channel           : {Style.RESET_ALL}{DelChannelName} - {DelChannelID}")
            elif rDel.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)  
            else:
                if DelChannel["type"] == 4:
                    print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to delete category : {Style.RESET_ALL}{DelChannelName} - {DelChannelID}")
                else:
                    print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to delete channel  : {Style.RESET_ALL}{DelChannelName} - {DelChannelID}")

            time.sleep(0.2)

        channelData = channels.json()
        categoryMap = {}

        for channel in channelData:
            ChannelName = channel["name"]
            ChannelID = channel["id"]

            if channel["type"] == 4:
                Overwrites = []
                for overwrite in channel.get("permission_overwrites", []):
                    OldID = overwrite["id"]
                    if overwrite["type"] == 0 and OldID in rolemap:
                        overwrite["id"] = rolemap[OldID]
                        Overwrites.append(overwrite)
                    elif overwrite["type"] == 1:
                        Overwrites.append(overwrite)

                payload = {
                    "name": channel["name"],
                    "type": channel["type"],
                    "position": channel["position"],
                    "permission_overwrites": Overwrites
                }

                r = requests.post(
                    f"{BaseURL}/guilds/{cloneId}/channels",
                    headers=headers,
                    json=payload
                )

                if r.status_code in succesStatus:
                    print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned category           : {Style.RESET_ALL}{ChannelName} - {ChannelID}")
                    try:
                        ResData = r.json()
                        categoryMap[ChannelID] = ResData["id"]
                    except Exception:
                        pass

                else:
                    print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone category  : {Style.RESET_ALL}{ChannelName} - {ChannelID}")

                time.sleep(0.2)

        for channel in channelData:
            if channel["type"] != 4: 
                Overwrites = []
                for overwrite in channel.get("permission_overwrites", []):
                    OldID = overwrite["id"]
                    if overwrite["type"] == 0 and OldID in rolemap:
                        overwrite["id"] = rolemap[OldID]
                        Overwrites.append(overwrite)
                    elif overwrite["type"] == 1:
                        Overwrites.append(overwrite)

                payload = {
                    "name": channel["name"],
                    "type": channel["type"],
                    "position": channel["position"],
                    "permission_overwrites": Overwrites
                }

                oldCatID = channel.get("parent_id")
                if oldCatID and oldCatID in categoryMap:
                    payload["parent_id"] = categoryMap[oldCatID]

                r = requests.post(
                    f"{BaseURL}/guilds/{cloneId}/channels",
                    headers=headers,
                    json=payload
                )

                if r.status_code in succesStatus:
                    ClonedChannelData = r.json()
                    ClonedID = ClonedChannelData.get("id")
                    ClonedName = ClonedChannelData.get("name")

                    print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned channel            : {Style.RESET_ALL}{ClonedName} - {ClonedID}")
                elif r.status_code == 429:
                    Retry = r.json().get("retry_after", 5)
                    await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)     
                else:
                    print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone channel   : {Style.RESET_ALL}{ChannelName} - {ChannelID}")

                time.sleep(0.2)
            
    else:
        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Channels unavailable{Style.RESET_ALL}")