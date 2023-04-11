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
time.sleep(0.1)
print(' ' * int((w-77)/2),"        .n                   .                 .                  n.")
time.sleep(0.1)
print(' ' * int((w-77)/2),"  .   .dP                  dP                   9b                 9b.    .")
time.sleep(0.1)
print(' ' * int((w-77)/2)," 4    qXb         .       dX                     Xb       .        dXp     t")
time.sleep(0.1)
print(' ' * int((w-77)/2),"dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb")
time.sleep(0.1)
print(' ' * int((w-77)/2),"9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP")
time.sleep(0.1)
print(' ' * int((w-77)/2)," 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP")
time.sleep(0.1)
print(' ' * int((w-77)/2),"  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'")
time.sleep(0.1)
print(' ' * int((w-77)/2),"    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'")
time.sleep(0.1)
print(' ' * int((w-77)/2),"        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                        )b.  .dbo.dP'`v'`9b.odb.  .dX(")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                     `'      9XXXXXX(   )XXXXXXP      `'")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                              XXXX X.`v'.X XXXX")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                              XP^X'`b   d'`X^XX")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                              X. 9  `   '  P )X")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                              `b  `       '  d'")
time.sleep(0.1)
print(' ' * int((w-77)/2),"                               `             '   ")
time.sleep(0.5)


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



if os_name == "Linux" or os_name == "Linux2":
    adapter = select_adapter_linux()
    print(adapter)
    cmnd = "airmon-ng start " + adapter
    os.system(cmnd)
else:
    print(' ' * int((w - 37) / 2),"Works only on linux operating systems")
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
        print(' ' * int((w - 17) / 2), "5.)Install Hack Tool")
        print(' ' * int((w-17)/2) ,"Choose the attack:", end=" ")
        attack=input('')

        if attack =="1":
            import Network_Scanners

        if attack =="2":
            import Macchangers

        if attack =="3":
            import MITM_Attacks

        if attack =="4":
            from Packets_Listener import listen_packet
            listen_packet(adapter)
        if attack == "5":
            os.system("cp -f WirelessAttack /usr/bin/")
            os.system("cd /usr/share/ && git clone https://github.com/Berkkucukk/Wireless_Attack.git")
            os.system("cd")
            os.system("chmod +x /usr/bin/WirelessAttack")
            os.system("chmod +x /usr/share/Wireless_Attack/Wireless_Attacks.py")
            print("The tool has been moved under the /usr/share directory and you can run it by typing 'WirelessAttack' in the terminal.")
            time.sleep(3)
            


        time.sleep(1)

except KeyboardInterrupt:
    print("\nQuit Program...")

