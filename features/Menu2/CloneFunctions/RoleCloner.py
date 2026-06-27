from config.settings import *

async def CloneRoles(targetId, cloneId, headers):
    roles = requests.get(f"{BaseURL}/guilds/{targetId}/roles", headers=headers)
    DelRoles = requests.get(f"{BaseURL}/guilds/{cloneId}/roles", headers=headers)

    DelRolesData = DelRoles.json()

    if roles.status_code in succesStatus:
        for DelRole in DelRolesData:
            DelRoleName = DelRole["name"]
            DelRoleID = DelRole["id"]

            if DelRole["name"] == "@everyone":
                continue
            
            rDel = requests.delete(
                f"{BaseURL}/guilds/{cloneId}/roles/{DelRoleID}",
                headers=headers
            )

            if rDel.status_code in succesStatus:
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Deleted role              : {Style.RESET_ALL}{DelRoleName} - {DelRoleID}")
            elif rDel.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry)      
            else:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to delete role     : {Style.RESET_ALL}{DelRoleName} - {DelRoleID}")
                
            time.sleep(0.2)

        rolesData = roles.json()
        roleMap = {}
        roleMap[targetId] = cloneId

        for role in rolesData:
            RoleName = role["name"]
            RoleID = role["id"]

            payload = {
                "name": role["name"],
                "permissions": role["permissions"],
                "color": role["color"]
            }

            if role["name"] == "@everyone":
                continue

            r = requests.post(
                f"{BaseURL}/guilds/{cloneId}/roles",
                headers=headers,
                json=payload
            )

            if r.status_code in succesStatus:
                print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Cloned role               : {Style.RESET_ALL}{RoleName} - {RoleID}")
                try:
                    roleMap[role["id"]] = r.json()["id"]
                except Exception:
                    pass

            elif r.status_code == 429:
                Retry = r.json().get("retry_after", 5)
                await asyncio.sleep(Retry / 1000 if Retry > 1000 else Retry) 
            else:
                print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Failed to clone role      : {Style.RESET_ALL}{RoleName} - {RoleID}")

            time.sleep(0.2)
            
    else:
        print(f"{bracketopen2}{Fore.GREEN}!{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Roles unavailable{Style.RESET_ALL}")

    return roleMap