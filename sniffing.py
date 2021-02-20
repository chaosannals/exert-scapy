from scapy.all import *

filter='icmp and host baidu.com'

a = sniff(count=10)
for s in a:
    print(type(s))