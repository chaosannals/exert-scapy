
from scapy.layers.l2 import Dot3, LLC, SNAP
from scapy.contrib.dtp import *


def negotiate_trunk(iface=conf.iface, mymac=str(RandMAC())):
    print('iface')
    tlvlist = [
        DTPDomain(),
        DTPStatus(),
        DTPType(),
        DTPNeighbor(neighbor=mymac)
    ]
    dot3 = Dot3(src=mymac, dst="01:00:0c:cc:cc:cc")
    p = dot3 / LLC()/SNAP()/DTP(tlvlist=tlvlist)
    sendp(p)
