#!/usr/bin/python3
import sys,os
from scapy.all import srp, Ether,ARP,conf

colors={
    "Danger":"\033[0;31m",
    "Warning":"\033[1;33m",
    "Success":"\033[0;32m",
    "NC":"\033[0m",
    "Primary":"\033[0;34m"
}


def check_root():
    global colors
    message=colors['Danger']+"Run It as Root"+colors['NC']
    if os.geteuid()!=0:
        print(message)
        return 1    
    return 0

def take_input():
    global colors
    ip=''
    iface=''
    try:
        iface=input(colors['Primary']+"Enter The interface you want to use : "+colors['NC'])
        ip=input(colors['Primary']+"Enter the ranges of ip : "+colors['NC'])
        pass
    except KeyboardInterrupt:
        print(colors['Danger']+"\nKeyBoard Interrupt!!\nExiting"+colors['NC'])
        exit()
    return iface,ip

def scan(iface,ip):
    conf.verb=0
    ans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=2,iface=iface)[0]
    for rcv in ans:
        print(colors['Success']+" "+str(rcv[1].psrc)+" - "+str(rcv[1].hwsrc)+" "+colors['NC'])
        pass


def main():
    if not check_root():
        iface,ip=take_input()
        try:
            scan(iface,ip)
            pass
        except KeyboardInterrupt:
            print(colors['Danger']+"\nKeyBoard Interrupt!!\nExiting"+colors['NC'])
            exit()
            

if __name__ == "__main__":
    main()
    pass


        

