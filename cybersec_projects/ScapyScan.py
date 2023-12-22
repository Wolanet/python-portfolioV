# we import the Scapy library, which is the core of this script
from scapy.all import *

# defining some common ports to scan, namely SSH, HTTP, HTTPS, DNS
ports = [22, 53, 80, 443, 8080]
# here we're using google DNS server as an example of host to scan
host = "8.8.4.4"

Scapy_logo = """        
        "                                      ",
        "                     aSPY//YASa       ",
        "             apyyyyCY//////////YCa    ",
        "            sY//////YSpcs  scpCY//Pp  ",
        "  ypaayyyyyyySCP//Pp           syY//C ",
        "  YAsAYYYYYYYY///Ps              cY//S",
        "         pCCCCY//p          cSSps y//Y",
        "         SPPPP///a          pP///AC//Y",
        "              A//A            cyP////C",
        "              p///Ac            sC///a",
        "              P////YCpc           A//A",
        "       scccccp///pSP///p          p//Y",
        "      sY/////////y  caa           S//P",
        "       cayCyayP//Ya              pY/Ya",
        "        sY/PsY////YCc          aC//Yp ",
        "         sc  sccaCY//PCypaapyCP//YSs  ",
        "                  spCPY//////YPSps    ",
        "                       ccaacs         ",
        "                                      ",                   
"""

# our main function to perform a scan, syn scan in this case
def S_Scan(host):
    print(Scapy_logo)
    # sr () function is used to send and receive packets, in this case we're performing a TCP SYN scan
    # ans stands for answered (packets) and unans for unanswered, which is what the variables store
    ans, unans = sr(IP(dst=host) / TCP(dport=ports, flags="S"), timeout=3, retry=5)
    print("Discovered open ports for %s:" % host)

    # this for loop is to check with the haslayer() function if a layer like TCP or UDP is present inside a packet
    # we then print the destination port if it matches with the source port, since we got a reply
    for sent,received in ans:
        if sent.haslayer(TCP) and received.haslayer(TCP):
            if sent[TCP].dport == received[TCP].sport:
                print(sent[TCP].dport)

# our second function to perform a dns scan, with pre-defined dport UDP 53 (which is for DNS)
def DNS_scan(host):
    print(Scapy_logo)
    # the DNS field has various classes defined in Scapy, essentially we specify google.com as the domain we want to query
    ans, unans = sr(IP(dst=host) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qtype="A", qname="google.com")), timeout=3, retry=5)
    if ans:
        print("DNS Server for %s:" % host)
        print(ans.summary())

# we call our 2 functions with the example host defined above
S_Scan(host)
DNS_scan(host)

# lastly I added the sniff function to sniff packets from our host, sniff () returns an array
packets = []
packets = sniff(filter=host)
print("Sniffed packets: %s" % packets)

# Scapy has many more functions and capabilities!
