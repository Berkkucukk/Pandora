import scapy.all as scapy
import optparse as opt
#scapy.ls(<bilgi almak istediğimiz sınıf(scapy.ARP())>)
def userInput():
    parser_object=opt.OptionParser()
    parser_object.add_option("-i","--ipadress",dest="ip_adress",help="Enter Ip Adress")
    (user_input,arguments)=parser_object.parse_args()
    if not user_input.ip_adress:
        print("Enter Ip adress. Use --help for more info.")
    return user_input
def scanner(ip):

    #arp_request
    arp_request=scapy.ARP(pdst=ip)
    #broadcast
    broadcast_request=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #arp_response
    combined_request=broadcast_request/arp_request
    (answered_list,unanswered_list)=scapy.srp((combined_request),timeout=1)
    return answered_list


def toString(answered_list):

    print(answered_list.summary())

ip_adress=userInput()

toString(scanner(ip_adress.ip_adress))
