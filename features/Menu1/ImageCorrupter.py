from config.settings import *

def clean_path(inp: str) -> str:
    m = re.match(r'^\s*&?\s*["\']?(.*?)["\']?\s*$', inp)
    return m.group(1) if m else inp.strip().strip('"').strip("'")

def CorruptImage():
        os.system("cls")
        Slow(file_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Image corrupter{Style.RESET_ALL}")
        print("")
        raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Image -> {Style.RESET_ALL}")

        FilePath = clean_path(raw)

        if not os.path.isfile(FilePath):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image not found :{Style.RESET_ALL} {FilePath}")
            time.sleep(2)
            return

        def is_image(path):
            with open(path, "rb") as f:
                header = f.read(20)

            signatures = [
                b"\x89PNG\r\n\x1a\n",
                b"\xff\xd8\xff",
                b"GIF87a",
                b"GIF89a",
                b"RIFF"
            ]

            return any(header.startswith(sig) for sig in signatures)

        if not is_image(FilePath):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Invalid file type{Style.RESET_ALL}")
            time.sleep(2)
            return

        try:
            with open(FilePath, "rb") as f:
                data = bytearray(f.read())

            file_size = len(data)

            if file_size < 2560 or file_size > 41943040:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image too large or too small{Style.RESET_ALL}")
                time.sleep(2)
                return
            
            min_pos = 1500
            max_pos = file_size - 1000
            
            if file_size < 5120:
                glitch_count = 10
            elif file_size < 10240:
                glitch_count = 20
            elif file_size < 20480:
                glitch_count = 30
            elif file_size < 51200:
                glitch_count = 40
            elif file_size < 102400:
                glitch_count = 50
            elif file_size < 512000:
                glitch_count = 60
            elif file_size < 1048576:
                glitch_count = 70
            elif file_size < 2097152:
                glitch_count = 80
            elif file_size < 5242880:
                glitch_count = 90
            elif file_size < 10485760:
                glitch_count = 100
            elif file_size < 20971520:
                glitch_count = 110
            elif file_size < 31457280:
                glitch_count = 120
            else:
                glitch_count = 500

            rnd = random.Random()
            for _ in range(glitch_count):
                    pos = rnd.randint(min_pos, max_pos)
                    data[pos] = rnd.randint(0, 255)

            with open(FilePath, "wb") as f:
                    f.write(data)

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Corrupting image... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Image corrupted :{Style.RESET_ALL} {FilePath}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image could not be corrupted{Style.RESET_ALL}")
            time.sleep(2)
        