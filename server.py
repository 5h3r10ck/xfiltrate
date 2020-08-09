#!/usr/bin/env python3

# C2 Server

import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="execute command")
parser.add_argument("-t", "--transfer", help="transfer files")

args = parser.parse_args()

def execute(cmd):
	packet = IP(dst="localhost")/ICMP(id=0x0001, seq=0x1)/cmd
	send(packet)
	print("done")

execute(args.command)
