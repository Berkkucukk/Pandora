from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt
from scapy.all import *

wifi_networks = []

def PacketHandler(pkt):
    if pkt.haslayer(Dot11Beacon):
        if pkt.getlayer(Dot11Beacon).info not in wifi_networks:
            wifi_networks.append(pkt.getlayer(Dot11Beacon).info)

def write_to_file(filename):
    with open(filename, 'w') as f:
        for network in wifi_networks:
            f.write(network.decode() + '\n')

def print_networks():
    for index, network in enumerate(wifi_networks):
        print(f"{index}: {network.decode()}")

def select_network():
    while True:
        choice = input("Enter the index of the network you want to connect to: ")
        try:
            choice = int(choice)
            if choice < 0 or choice >= len(wifi_networks):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter a valid index.")

    return wifi_networks[choice].decode()

iface = input("Enter the interface name (e.g. wlan0): ")
duration = input("Enter the duration of the scan in seconds: ")
filename = input("Enter the filename to save the list of networks: ")

print("Scanning for wifi networks...")
sniff(iface=iface, prn=PacketHandler, timeout=int(duration))

write_to_file(filename)
print(f"{len(wifi_networks)} networks found and saved to {filename}.\n")

print_networks()
selected_network = select_network()

print(f"You selected {selected_network}.")
