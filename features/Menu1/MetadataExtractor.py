from config.settings import *

def ExtractMetadata():
        os.system("cls")
        Slow(analyze_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Metadata extractor{Style.RESET_ALL}")
        print("")
        raw = input(f"{bracketopen}>{bracketclosed} {Fore.GREEN}Image -> {Style.RESET_ALL}")

        def clean_path(inp: str) -> str:
            m = re.match(r'^\s*&?\s*["\']?(.*?)["\']?\s*$', inp)
            return m.group(1) if m else inp.strip().strip('"').strip("'")

        Image = clean_path(raw)

        if not os.path.isfile(Image):
            print("")
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Image not found :{Style.RESET_ALL} {Image}")
            time.sleep(2)
            return

        try:
            img = PIL.Image.open(Image)

            exif_raw = img._getexif()

            if not exif_raw:
                print("")
                print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} No metadata found{Style.RESET_ALL}")
                time.sleep(2)
                return

            exif = {}

            for k, v in img._getexif().items():
                tag = PIL.ExifTags.TAGS.get(k)
                if tag:
                    exif[tag] = v

            make = exif.get('Make', "None")
            model = exif.get('Model', "None")
            software = exif.get('Software', "None")
            date = exif.get('DateTime', "None")
            originalDate = exif.get('DateTimeOriginal', "None")
            gpsInfo = exif.get("GPSInfo")

            if not gpsInfo:            
                lat = None
                long = None
            else:
                try:
                    rawLat = gpsInfo[2]
                    rawLon = gpsInfo[4]

                    lat = rawLat[0]
                    long = rawLon[0]
                except Exception:
                    lat = None
                    long = None

            print(f"{bracketopen}~{bracketclosed} {Fore.GREEN}Searchig for information... {Style.RESET_ALL}")
            time.sleep(1.5)
            print("")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Make           :{Style.RESET_ALL} {make}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Model          :{Style.RESET_ALL} {model}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Software       :{Style.RESET_ALL} {software}")
            print("")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Recording time :{Style.RESET_ALL} {originalDate}")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Last modified  :{Style.RESET_ALL} {date}")
            print("")
            time.sleep(0.05)
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Latitude       :{Style.RESET_ALL} {lat}")
            time.sleep(0.05) 
            print(f"{bracketopen2}{Fore.GREEN}+{Style.RESET_ALL}{bracketclosed2}{Fore.GREEN} Longitude      :{Style.RESET_ALL} {long}")
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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Metadata could not be extracted{Style.RESET_ALL}")
            time.sleep(2)
        