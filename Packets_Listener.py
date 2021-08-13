import scapy.all as scapy
from scapy_http import http
import optparse
def user_input():
    parser=optparse.optparse()
    parser.add_option("-i","--interface",dest="interface",help="Enter Interface.")
    options=parser.parse_args()[0]
    if not options.target_ip:
        print("Enter target ip...")
    return options
def listen_packet(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packet)
    #prn=callback function

def analyze_packet(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            packet[scapy.Raw].load
interface=user_input().interface
listen_packet(interface)
