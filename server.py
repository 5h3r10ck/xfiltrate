# C2 Server

#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--command", help="execute command")
parser.add_argument("-t", "--transfer", help="transfer files")

args = parser.parse_args()

