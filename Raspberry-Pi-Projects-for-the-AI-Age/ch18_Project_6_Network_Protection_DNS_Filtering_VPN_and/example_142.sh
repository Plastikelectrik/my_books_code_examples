#!/bin/bash
# $1 is -A (add) or -D (delete)
iptables -t nat "$1" POSTROUTING \
    -s 10.8.0.0/24 -o eth0 -j MASQUERADE
