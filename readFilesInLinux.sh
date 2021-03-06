#!/usr/bin/python3
hosts = '/etc/hosts'
title = 'Current IPv4 Hosts'

def print_current(textfile, message):
    print(message)
    print('-' * len(message))
    f = open(textfile, 'r')
    for line in f:
        if ':' not in line:
            if len(line.strip()) > 0:
                print(line.rstrip())
    f.close()
print_current(hosts, title)