import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys
import pyfiglet
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
  import pyfiglet
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install pysocks && pip install bs4 && pip install pystyle')
  os.system("pip install pyfiglet")
  os.system('clear')
  print(f"\033[1;35mChúc bạn sử dụng tool vui vẻ 😍")
  sleep(1)
  print(f"\033[1;36mVui \033[1;33mLòng \033[1;31mChờ \033[1;39m5s \033[1;35mĐể\033[1;32mLoad \033[1;34mTool...🤑🔫💸")
  sleep(5)
  
  
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
                 \033[1;34m██████╗ ██╗  ██╗██╗   ██╗ ██████╗  ██████╗                                            
                 \033[1;31m██████╔╝███████║██║   ██║██║   ██║██║                         
                 \033[1;35m██╔═══╝ ██╔══██║██║   ██║██║   ██║██║                           
                 \033[1;36m██║     ██║  ██║╚██████╔╝╚██████╔╝╚██████╗                      
                 \033[1;31m╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ 
\033[1;97mTool By: \033[1;32mPhuoc Code      \033[1;97mPhiên Bản: \033[1;32m2.1     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36m@phuocan.9999\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps:\033[1;32m//www.tiktok.com\033[1;31m/@_tinhyeu_k
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.001)

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool TDS   \033[1;35m            ║           ")
	print("\033[1;35m╚══════════════════════╝           ")
	print(f"\033[1;36m[\033[1;32m*\033[1;97m] \033[1;36m1 \033[1;97m: \033[1;36mTool TDS TikTok Auto Click \033[1;32m[Online]")
	print(f"\033[1;36m[\033[1;32m*\033[1;97m] \033[1;36m2 \033[1;97m: \033[1;36mTool TDS TikTok Cookie (DT sẽ kh dùng dc) \033[1;32m[PC,Mobile]")
	print(f"\033[1;36m[\033[1;32m*\033[1;97m] \033[1;36m2.1 \033[1;97m: \033[1;36mTool TDS TikTok FB \033[1;32m[Online]")
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool Beta   \033[1;35m        ║          ")
	print("\033[1;35m╚══════════════════════╝           ")
	print(f"\033[1;36m[\033[1;32m*\033[1;97m] \033[1;36m3 \033[1;97m: \033[1;36mTool Đoán TX ( đoán 7/3) \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4 \033[1;97m: \033[1;36mTool Buff FL + Tym \033[1;32m[Online]")
	print(f"\033[1;36m[\033[1;32m*\033[1;97m] \033[1;36m5 \033[1;97m: \033[1;36mTool Spam Sms No Call \033[1;32m[lỏ]")
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool Buff FB  \033[1;35m      ║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6 \033[1;97m: \033[1;36mTool Buff View Str Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7 \033[1;97m: \033[1;36mTool Buff Reaction Pro5 \033[1;32m[off]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8 \033[1;97m: \033[1;36mTool Machineliker FB \033[1;32m[off]")
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool TTC  \033[1;35m      ║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m9 \033[1;97m: \033[1;36mTool TTC FB \033[1;32m[online]")
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool Tiện ích\033[1;35m      ║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m10 \033[1;97m: \033[1;36mTool Tải Clip Tiktok \033[1;32m[online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m11 \033[1;97m: \033[1;36mTool ??? \033[1;32m[off]")
	print("\033[1;35m╔══════════════════════╗         ")
	print("\033[1;35m║  \033[1;32mTool FB\033[1;35m      ║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m12 \033[1;97m: \033[1;36mTool Reg Page Pro5 \033[1;32m[off]")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1':
		# Thành Công
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/tdstikv2.py').text)
	elif chon == '2':
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/tdstikcookie.py').text)
	elif chon == '3':
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/Taixiu.py').text)
	elif chon == '4':
		exec(requests.get('https://raw.githubusercontent.com/Cacdume-wq/cac/refs/heads/main/cd%20/sdcard/pkkkk.py').text)
	elif chon == '5':
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/spamsms.py').text)
	elif chon == '6':
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/strpro5.py').text)
	elif chon == '7':
		sys.exit("")
	elif chon == '8':
		sys.exit("")
	elif chon == '9':
		exec(requests.get('https://raw.githubusercontent.com/Cacdume-wq/cac/refs/heads/main/kkk.py').text)
	elif chon == '10':
		exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/l-n/refs/heads/main/snap.py').text)
	elif chon == '11':
		sys.exit("")
	elif chon == '12':
		sys.exit("")
	elif chon == '2.1':
		exec(requests.get('https://raw.githubusercontent.com/Cacdume-wq/cac/refs/heads/main/songcho.py').text)
		
	else:
		sys.exit("")
