import scapy.all as scapy
from scapy.layers import http

def listen_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packet)

def analyze_packet(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            packet[scapy.Raw].load
