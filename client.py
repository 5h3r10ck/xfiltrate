#!/usr/bin/env python3

#Client should be on the host machine

from scapy.all import *
import os


recv = sniff(filter="icmp", count=10)
print("recv")
print("done")