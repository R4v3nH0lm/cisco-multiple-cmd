from Exscript.protocols import SSH2
from Exscript import Account
import socket
import os
import datetime

account = Account('Username', 'Password') 
date = str(datetime.date.today())

with open('cmd_list', 'r+') as cmd_list:
    commands = cmd_list.readlines()
    commands = [line[:-1] for line in commands]
    print "Running these commands %s" % commands

with open('hostfile', 'r+') as hosts_file:
    devices = hosts_file.readlines()
    devices = [line[:-1] for line in devices]
    for device in devices:
        if '#' not in device:
            print "On device %s" % device

with open('hostfile', 'r+') as hosts_file:
    for host in hosts_file:
        if '#' not in host:
            ipaddress = socket.gethostbyname(host.strip())
            conn = SSH2() 
            conn.connect(ipaddress)
            conn.login(account)
            conn.execute('terminal length 0')
            for cmd in commands:
                conn.execute(cmd)
                output = conn.response
                print output
            print "**Device %s complete**" % host
