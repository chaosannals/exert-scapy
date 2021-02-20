from scapy.all import *

# 模拟 TCP 握手
source = IP(dst="192.168.0.1")/TCP(dport=22)
rsp = sr1(source)
source2 = IP(dst="192.168.0.1")/TCP(dport=22, flags='A', seq=rsp.ack, ack=rsp.seq+1)
rsp2 = sr1(source2)
print(rsp2.show())