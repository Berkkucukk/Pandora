import time
import os
import sys
def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th
w, h = terminal_size()

print("\033[91m")
print(' ' * int((w-77)/2),"          .                                                      .")
print(' ' * int((w-77)/2),"        .n                   .                 .                  n.")
print(' ' * int((w-77)/2),"  .   .dP                  dP                   9b                 9b.    .")
print(' ' * int((w-77)/2)," 4    qXb         .       dX                     Xb       .        dXp     t")
print(' ' * int((w-77)/2),"dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb")
print(' ' * int((w-77)/2),"9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP")
print(' ' * int((w-77)/2)," 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP")
print(' ' * int((w-77)/2),"  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'")
print(' ' * int((w-77)/2),"    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'")
print(' ' * int((w-77)/2),"        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~")
print(' ' * int((w-77)/2),"                        )b.  .dbo.dP'`v'`9b.odb.  .dX(")
print(' ' * int((w-77)/2),"                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.")
print(' ' * int((w-77)/2),"                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb")
print(' ' * int((w-77)/2),"                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
print(' ' * int((w-77)/2),"                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP")
print(' ' * int((w-77)/2),"                     `'      9XXXXXX(   )XXXXXXP      `'")
print(' ' * int((w-77)/2),"                              XXXX X.`v'.X XXXX")
print(' ' * int((w-77)/2),"                              XP^X'`b   d'`X^XX")
print(' ' * int((w-77)/2),"                              X. 9  `   '  P )X")
print(' ' * int((w-77)/2),"                              `b  `       '  d'")
print(' ' * int((w-77)/2),"                               `             '   ")


if os.geteuid() != 0:
    print(' ' * int((w-24)/2),"Run with root privilege!")
    sys.exit()

try:
    import scapy
    import pandas
    import platform
    import netifaces

except ImportError:
    print("Librarys Not Found!")
    os.system("pip3 install scapy")
    os.system("pip3 install pandas")
    os.system("pip3 install netifaces")
    os.system("pip3 install platform")
    os.execv(sys.executable, ['python3', 'Wireless_Attacks.py'])

import platform
os_name = platform.uname().system

def select_adapter_linux():
    print("Available WiFi adapters:\n")
    adapters = os.listdir('/sys/class/net/')
    for index, adapter in enumerate(adapters):
        if adapter.startswith('wlan'):
            print(f"{index}: {adapter}")
    while True:
        choice = input("Enter the index of the adapter you want to use: ")
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(adapters):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter a valid index.")

    return adapters[choice]



if os_name == "linux" or os_name == "linux2":
    adapter = select_adapter_linux()
    os.system("airmon-ng start ",adapter)
else:
    print("Works only on linux operating systems.")
    sys.exit()

try:
    while True:
        w, h = terminal_size()
        print(' ' * int((w-17)/2) , "\033[0m Wireless Attacks")
        print("-"*w)
        print(' ' * int((w-17)/2), "1.)Network Scan")
        print(' ' * int((w - 17) / 2), "2.)Mac Change")
        print(' ' * int((w - 17) / 2), "3.)MITM Attack")
        print(' ' * int((w - 17) / 2), "4.)Network Sniff")
        print(' ' * int((w-17)/2) ,"Choose the attack:", end=" ")
        attack=input('')

        if attack =="1":
            import Network_Scanners

        if attack =="2":
            import Macchangers

        if attack =="3":
            import MITM_Attacks

        if attack =="4":
            import Packets_Listener
        time.sleep(1)

except KeyboardInterrupt:
    print("\nQuit Program...")

