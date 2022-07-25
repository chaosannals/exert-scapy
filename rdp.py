from scapy.all import *

# 读取抓包保存的文件
a = rdpcap('hq.pcapng')
for i in a:
    print(i.show())