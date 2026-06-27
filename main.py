from features.Menu1.IpLookup import *
from features.Menu1.PhoneLookup import *
from features.Menu1.MetadataExtractor import *
from features.Menu1.OsintFramework import *
from features.Menu1.FileCorrupter import *
from features.Menu1.ImageCorrupter import *
from features.Menu1.FileEraser import *
from features.Menu1.AntiScreenCapture import *
from features.Menu1.PasswordGenerator import *
from features.Menu1.PasswordChecker import *
from features.Menu2.DiscordSelfbot import *
from features.Menu2.ServerCloner import *
from features.Menu2.StealerConfig import *

#Menu 2
def mainMenu2():
    while True:
        os.system("cls")
        Slow(banner)
        print("")
        Slow(menu2)
        
        command2 = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{username}{Fore.GREEN})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
        
        if command2 == "11":
            RunMenu()
        elif command2 == "12":
            CloneServer()
        elif command2 == "13":
            ConfigStealer()
        elif command2 == "+":
            main()

#Menu 1
def main():
    while True:
        os.system("cls")
        Slow(banner)
        print("")
        Slow(menu1)
        
        command = input(f"""{Fore.GREEN} ┌──({Fore.WHITE}{username}{Fore.GREEN})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.GREEN}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}""")
                
        if command == "1" or command == "01":
            IPLookup()
        elif command == "2" or command == "02":
            LookupPhone()
        elif command == "3" or command == "03":
            ExtractMetadata()
        elif command == "4" or command == "04":
            OpenOsintFramwork()
        elif command == "5" or command == "05":
            CorruptFile()
        elif command == "6" or command == "06":
            CorruptImage()
        elif command == "7" or command == "07":
            EraseFile()
        elif command == "8" or command == "08":
            AntiCapture()
        elif command == "9" or command == "09":
            GeneratePassword()
        elif command == "10":
            CheckPassword()
        elif command == "+":
            mainMenu2()
main()