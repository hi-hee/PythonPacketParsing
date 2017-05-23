
# pip3 install scapy-python3

from scapy.all import *

#Read Pcap File----------Only Pcap(Pcapng is impossible)
a = rdpcap('c:/users/hee/desktop/test.pcap')

#The number of packet
pktNum = len(a)


#Payload of 10th packet
#Payload is data except Ethernet header
pktPayload = bytearray(bytes(a[9].payload))


#with PcapReader('filename.pcap') as pcap_reader:
  #for pkt in pcap_reader:
    #do something with the packet
