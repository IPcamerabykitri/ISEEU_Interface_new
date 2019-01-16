import os
import subprocess

cmd = '''awk '("TCP" "IPv4" "ICMP" && $3=="192.168.65.132") {print $3, $4, $5 > "ip.txt"}' date.txt'''
subprocess.check_call(cmd,shell=True)
