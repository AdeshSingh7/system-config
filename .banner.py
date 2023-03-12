#!/usr/bin/python3 python3
import os

def get_ip_address():
    """Get the system's IP addresses."""
    ip_addresses = os.popen("hostname -I").read().strip().replace(" ", " | ")
    if ip_addresses:return ip_addresses
    else:return "___.___.___.___"

def get_mac_address():
    """Get the system's MAC addresses."""
    mac_addresses = os.popen("ifconfig | awk '/ether/ {print $2}'").read().split()
    if len(mac_addresses) > 1:return mac_addresses
    else:return [mac_addresses[0],'___.___.___.___']

def display_banner(size, vendor, os_name, Serial_Number, uptime, lan_mac, wlan_mac, ipv4):
    print(f"\33[1;7;91m ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛ ♛  \33[0m".center(size))
    print(f"\33[1;7;91m   █████╗ ██████╗ ███████╗███████╗██╗  ██╗    ███████╗██╗███╗   ██╗ ██████╗ ██╗  ██╗  \33[0m".center(size))
    print(f"\33[1;7;91m  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║    ██╔════╝██║████╗  ██║██╔════╝ ██║  ██║  \33[0m".center(size))
    print(f"\33[1;7;91m  ███████║██║  ██║█████╗  ███████╗███████║    ███████╗██║██╔██╗ ██║██║  ███╗███████║  \33[0m".center(size))
    print(f"\33[1;7;91m  ██╔══██║██║  ██║██╔══╝  ╚════██║██╔══██║    ╚════██║██║██║╚██╗██║██║   ██║██╔══██║  \33[0m".center(size))
    print(f"\33[1;7;91m  ██║  ██║██████╔╝███████╗███████║██║  ██║    ███████║██║██║ ╚████║╚██████╔╝██║  ██║  \33[0m".center(size))
    print(f"\33[1;7;91m  ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝  \33[0m".center(size))
    print(f"\33[1;7;91m ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾  https://github.com/AdeshSingh7 ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾ ✾  \33[0m".center(size))
    print("".center(size,"❄"))
    print(f"\33[1;91m\u2713 Operating System\33[1;94m ⟶  \33[1;92m {vendor}-{os_name}\33[0m")
    print(f"\33[1;91m\u2713 Serial Number\33[1;94m    ⟶  \33[1;92m {Serial_Number}\33[0m")
    print(f"\33[1;91m\u2713 System Uptime\33[1;94m    ⟶  \33[1;92m {uptime}\33[0m")
    print(f"\33[1;91m\u2713 LAN MAC Address\33[1;94m  ⟶  \33[1;92m {lan_mac}\33[0m")
    print(f"\33[1;91m\u2713 WLAN MAC Address\33[1;94m ⟶  \33[1;92m {wlan_mac}\33[0m")
    print(f"\33[1;91m\u2713 LAN IP Address\33[1;94m   ⟶  \33[1;92m {ipv4}\33[0m")
    print("".center(size,"❄"))

if __name__ == '__main__':
    try:
        os.system("clear")
        size = os.get_terminal_size()[0]
        vendor = os.popen("sudo dmidecode -s bios-vendor").read().strip()
        os_name = os.popen("uname -n -o").read().strip()
        uptime = os.popen("uptime -p").read().strip()
        Serial_Number = os.popen("sudo dmidecode -s system-serial-number").read().strip()
        lan_mac = get_mac_address()[0].upper()
        wlan_mac = get_mac_address()[1].upper()
        ipv4 = get_ip_address()
        display_banner(size, vendor, os_name, Serial_Number, uptime, lan_mac, wlan_mac, ipv4)
    except KeyboardInterrupt:exit()
    except Exception as error:
        print(f"\33[1;91m\u2713Error: \33[1;92m{error}\33[0m")
    finally:exit()
