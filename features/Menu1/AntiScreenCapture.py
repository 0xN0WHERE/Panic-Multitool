from config.settings import *

AntiThread = None
AntiHwnd = None

def run():
    global AntiHwnd

    ClassName = "Window"

    def wnd(hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            return 0
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    hInstance = win32api.GetModuleHandle(None)

    wndclass = win32gui.WNDCLASS()
    wndclass.lpfnWndProc = wnd
    wndclass.hInstance = hInstance
    wndclass.lpszClassName = ClassName

    try:
        win32gui.RegisterClass(wndclass)
    except win32gui.error:
        pass

    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)

    AntiHwnd = win32gui.CreateWindowEx(
        win32con.WS_EX_LAYERED |
        win32con.WS_EX_TOPMOST |
        win32con.WS_EX_TRANSPARENT,
        ClassName,
        None,
        win32con.WS_POPUP,
        0, 0, w, h,
        None, None, hInstance, None
    )

    win32gui.ShowWindow(AntiHwnd, win32con.SW_SHOW)
    win32gui.SetLayeredWindowAttributes(AntiHwnd, 0, 0, win32con.LWA_COLORKEY)
    ctypes.windll.user32.SetWindowDisplayAffinity(AntiHwnd, 0x1)

    win32gui.PumpMessages()

def StopAntiCapture():
    global AntiHwnd

    if AntiHwnd:
        try:
            win32gui.PostMessage(AntiHwnd, win32con.WM_CLOSE, 0, 0)
        except:
            pass

def AntiCapture():
        global AntiThread

        os.system("cls")
        Slow(analyze_banner)
        time.sleep(1.5)
        os.system("cls")
        print(f"{bracketopen}!{bracketclosed} {Fore.GREEN}Anti screen capture{Style.RESET_ALL}")

        try:
            if AntiThread and AntiThread.is_alive():
                StopAntiCapture()
                AntiThread.join(timeout=2)

            AntiThread = threading.Thread(target=run, daemon=True)
            AntiThread.start()

            print("")
            print(f"{bracketopen}+{bracketclosed} {Fore.GREEN}Anti screen capture activated, to deactivate close the window in task manager or taskbar{Style.RESET_ALL}")

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
            print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed}{Fore.GREEN} Anti screen capture failed{Style.RESET_ALL}")
            time.sleep(2)