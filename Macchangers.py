import subprocess as sub


def get_interface():
    user_input=input("Select your interface:\n1.)Wlan0\n2.)Wlan1\n3.)Eth0\n")
    interface=""
    if user_input =="1":
        interface="wlan0"
    elif user_input =="2":
        interface="wlan1"
    elif user_input =="3":
        interface="eth0"
    return interface

def get_mac():
    new_mac=input("Enter new mac adress(default=00:11:22:33:44:55):")
    if new_mac=="":
        new_mac="00:11:22:33:44:55"
    return new_mac
def change_mac(interface,new_mac):
    print("[+]Changing Mac Adress for "+interface+" to "+new_mac)
    sub.call(["ifconfig",interface,"down"])
    sub.call(["ifconfig",interface,"hw","ether",new_mac])
    sub.call(["ifconfig",interface,"up"])

interface=get_interface()
new_mac=get_mac()
change_mac(interface,new_mac)
