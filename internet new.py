import pydivert
import keyboard
import time
import random
import os
import time
from colorama import Fore
import win32api , win32con
from ctypes import wintypes
import pyperclip
import sys
from tqdm import tqdm
import http.client
import psutil
import threading

url = 'pastebin.com'
path = '/raw/qhuduqif'
conn = http.client.HTTPSConnection(url)
conn.request('GET', path)
response = conn.getresponse()
data = response.read()
conn.close()
import threading

def get_hardware():
    machine_guid = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Cryptography')
    hardware, _ = win32api.RegQueryValueEx(machine_guid, 'MachineGuid')
    win32api.RegCloseKey(machine_guid)
    return f"Zeroz-{hardware}"

hardware = get_hardware()

PROCNAMES = [
    "ProcessHacker.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "fiddler.exe",
    "regedit.exe",
    "http toolkit.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "fiddler.exe",
    "charles.exe",
    "regedit.exe",
    "taskmgr.exe",
    "vboxservice.exe",
    "df5serv.exe",
    "processhacker.exe",
    "vboxtray.exe",
    "vmtoolsd.exe",
    "vmwaretray.exe",
    "ida64.exe",
    "ollydbg.exe",
    "pestudio.exe",
    "vmwareuser",
    "vgauthservice.exe",
    "vmacthlp.exe",
    "x96dbg.exe",
    "vmsrvc.exe",
    "x32dbg.exe",
    "x64dbg.exe",
    "vmusrvc.exe",
    "prl_cc.exe",
    "prl_tools.exe",
    "qemu-ga.exe",
    "joeboxcontrol.exe",
    "ksdumperclient.exe",
    "ksdumper.exe",
    "joeboxserver.exe",
    "xenservice.exe",
]

def check_for_debugging_tools():
    for proc in psutil.process_iter():
        if proc.name().lower() in PROCNAMES:
            print(f"Detected debugging tool: {proc.name}")
            #os.system('powershell wininit')
            proc.kill()
            sys.exit()


def network_simulation(w, is_active):
    # ตั้งค่าเริ่มต้น
    drop_interval = 0.010  # ทิ้งทุก 3 มิลลิวินาที
    last_packet_time = time.time()

    duplicate_chance = 0.20  # โอกาสการทำซ้ำ 3%
    duplicate_count = 5  # จำนวนครั้งในการทำซ้ำ

    out_of_order_chance = 0.10  # โอกาสส่งไม่ตามลำดับ 3%
    out_of_order_packets = []

    while True:
        packet = w.recv()
        current_time = time.time()

        if not is_active[0]:  # ถ้าการทำงานไม่ได้ถูกเปิดใช้งาน
            w.send(packet)
            continue

        # ตัดสินใจทิ้งแพคเก็ต
        if current_time - last_packet_time < drop_interval:
            #print("Dropping packet")
            last_packet_time = current_time
            continue

        last_packet_time = current_time

        # ตัดสินใจส่งไม่ตามลำดับ
        if random.random() < out_of_order_chance:
            #print("Queueing out-of-order packet")
            out_of_order_packets.append(packet)
            continue

        # ส่งแพคเก็ตปกติ
        w.send(packet)

        # ส่งแพคเก็ตที่เก็บไว้
        while out_of_order_packets:
            w.send(out_of_order_packets.pop(0))
            #print("Sending queued out-of-order packet")

        # ตัดสินใจทำซ้ำแพคเก็ต
        if random.random() < duplicate_chance:
            for _ in range(duplicate_count):
                w.send(packet)
                #print("Sending duplicated packet")

# ตัวแปรสำหรับเก็บสถานะการทำงาน (เปิด/ปิด)
is_active = [False]

# ฟังก์ชันสำหรับสลับการทำงาน
def toggle_simulation():
    is_active[0] = not is_active[0]
    state = "Enable" if is_active[0] else "Disable"
    print(f"Status: {state}")

# ตั้งค่าการกดปุ่ม 'F' เพื่อสลับการทำงาน
keyboard.add_hotkey('f', toggle_simulation)

def check_realtime():
    while True:
        check_for_debugging_tools()
        time.sleep(1)
        

def program():
    print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Welcome to The Futures')
    time.sleep(2)
    os.system("cls & title Zeroz l Project : SXYZ")
    print("")
    print("")
    print("")
    print("")
    print(Fore.BLUE +"                              ______   ____  ____  ____  ____  ________  ")
    print(Fore.BLUE +"                            .' ____ \ |_  _||_  _||_  _||_  _||  __   _| ")
    print(Fore.BLUE +"                            | (___ \_|  \ \  / /    \ \  / /  |_/  / /   ")
    print(Fore.CYAN +"                             _.____`.    > `' <      \ \/ /      .'.' _  ")
    print(Fore.CYAN +"                            | \____) | _/ /'`\ \_    _|  |_    _/ /__/ | ")
    print(Fore.CYAN +"                             \______.'|____||____|  |______|  |________|  ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(Fore.LIGHTBLACK_EX + '                            [', Fore.CYAN + 'F', Fore.LIGHTBLACK_EX + ']', Fore.BLUE + 'Keyboard' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Enable / Disable')
    check_for_debugging_tools()
    with pydivert.WinDivert("udp.DstPort == 30120") as w:
        check_for_debugging_tools()
        network_simulation(w, is_active)

def Main_Program():
    if hardware in data.decode('utf-8'):
        time.sleep(0.05)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Project' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Style')
        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Product' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Zeroz Store')
        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Support By' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Soy Smit')

        time.sleep(2)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'HWID' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + hardware)

        time.sleep(2)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTGREEN_EX + 'Successful')
        time.sleep(2)
        os.system("cls & title Zeroz l Project : Style")
        pass
    else:
        time.sleep(0.05)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Project' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Style')
        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Product' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Zeroz Store')
        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'Support By' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + 'Soy Smit')

        time.sleep(2)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTCYAN_EX + '+', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTBLACK_EX + 'HWID' , Fore.LIGHTCYAN_EX + ':', Fore.LIGHTWHITE_EX + hardware)

        time.sleep(2)
        os.system("cls & title Zeroz l Project : Style")

        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTRED_EX + '-', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTRED_EX + 'Login Failed')
        time.sleep(2)

        os.system("cls & title Zeroz l Project : Style")
        print(Fore.LIGHTBLACK_EX + '[', Fore.LIGHTRED_EX + '-', Fore.LIGHTBLACK_EX + ']', Fore.LIGHTRED_EX + 'Copying HWID ...')
        pyperclip.copy(hardware)
        time.sleep(2)
        sys.exit()


Main_Program()

thread = threading.Thread(target=check_realtime)
thread.start()

program()