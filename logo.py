import os, sys, time
from time import sleep
rst="\033[0m"
b="\033[1;30m"
r="\033[1;31m"
g="\033[1;32m"
yl="\033[1;33m"
bl="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
def ani(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def logo ():
  os.system("clear")
  #change ascii or names
  os.system("""echo '  ░█████╗░██╗░░██╗██╗░░██╗██╗░░░██╗░█████╗░██╗░░░██╗
  ██╔══██╗██║░██╔╝╚██╗██╔╝██║░░░██║██╔══██╗██║░░░██║
  ███████║█████═╝░░╚███╔╝░╚██╗░██╔╝███████║██║░░░██║
  ██╔══██║██╔═██╗░░██╔██╗░░╚████╔╝░██╔══██║██║░░░██║
  ██║░░██║██║░╚██╗██╔╝╚██╗░░╚██╔╝░░██║░░██║╚██████╔╝
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░
----------------------------------------------------
  ╔════════════════════════════════════════════════╗
  ║            [✓] TOOL NAME : ANONFILE            ║
  ║            [✓] GITHUB : AKXVAU                 ║
  ║            [✓] FACEBOOK : AKX.THE.PSYCHO       ║
  ║            [✓] TELEGRAM : AKXVAU               ║
  ║            [✓] INSTAGRAM : AKXVAU              ║
  ║            [✓] EMAIL : ADMIN@ITZAKX.ML         ║
  ╚════════════════════════════════════════════════╝\n----------------------------------------------------'|lolcat""")
  #your slogan
  ani(r+"\t<"+bl+"p"+r+">"+g+" MAKE GOOGLE YOUR BEST FRIEND :) "+r+"<"+bl+"/p"+r+">")
  #welcome voice
  os.system("termux-tts-speak Welcome Mohammad Alamin ")
  os.system("echo '----------------------------------------------------'| lolcat")
  
logo ()  
