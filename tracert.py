from scapy.all import *

ans, unans = sr(IP(dst='8.8.8.8', ttl=(1, 20), id=RandShort())/TCP(flags=0x2))

for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))
