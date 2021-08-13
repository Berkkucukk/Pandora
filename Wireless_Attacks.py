import time
try:
    while True:
        print("Wireless Attack")
        print("------------------------------------")
        attack=input("Choose the attack.\n1.)Network Scan\n2.)Mac Change\n3.)MITM Attack\n4.)Network Sniff\nExit=Ctrl+C\n")

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

