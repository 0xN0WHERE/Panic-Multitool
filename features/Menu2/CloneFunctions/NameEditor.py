from config.settings import *

def EditName(targetId, cloneId, headers):
        TargetRes  = requests.get(f"{BaseURL}/guilds/{targetId}", headers=headers)
        TargetName = TargetRes.json().get("name", "Unknown Server")

        payload = {
            "name": TargetName
        }
        
        res = requests.patch(
            f"{BaseURL}/guilds/{cloneId}", 
            headers=headers, 
            json=payload
        )
        
        if res.status_code in succesStatus:
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned server name        : {Style.RESET_ALL}{TargetName}")
        else:
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone name      : {Style.RESET_ALL}{TargetName}")