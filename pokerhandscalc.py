#!/home/pi/software/bin/python3
import cgi, cgitb
import base64
import os
import subprocess

cgitb.enable()
form = cgi.FieldStorage()

def main():
	
	listCard = "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "th", "jh", "qh", "kh", "ah", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "tc", "jc", "qc", "kc", "ac","2s", "3s","4s", "5s", "6s", "7s", "8s", "9s", "ts", "js", "qs", "ks", "as", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "td", "jd", "qd", "kd", "ad"
	cardDic = {}

	for i in listCard:
		cardDic[str(listCard.index(i))] = i

	print("Content-type: text/html\n\n")

	cards = form.getvalue('cards')
	bbutton = form.getvalue('bbutton')

	def startPage():
		print("<html>\n")
		print("<head>\n")
		print("<title>Poker combination calculator</title>\n")
		print("</head>\n")
		print("<body>")
		print("<h1>Choose 5 cards. Press \"Check Poker Hand\" to determine the hand category. Press \"Clear\" to reset.</h1>")
		print("<form method=\"post\" action=\"../cgi-bin/pokerhandscalc.py/\">")	
		print("<div>\n")
		for i in range (len(listCard)):

			cardPath = '../cards/' + listCard[i] + '.png'

			print("<input type='checkbox' name='cards' value=" + listCard[i] + ">\n")
			print("<img src=" + cardPath + " width = \"37\" height = \"53\">")
			
			if (i + 1) < (len(listCard)):

				if listCard[i][1] != listCard[i + 1][1]:
					print("</div>\n")
					print("<div>\n")
		print("<div> <input name=\"bbutton\" type=\"submit\" value=\"Check Poker Hand\"/> <input name=\"bbutton\" type=\"submit\" value=\"Clear\"/> </div>")
		print("</form>\n")
		print("")
		print("</body>\n")
		print("</html>\n")

	def findCategory(cards) :
	
		if isStraightFlush(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a STRAIGHT FLUSH!</h1>")
			piInfo()
			
			return 'SF'
		elif isFourOfAKind(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a FOUR OF A KIND!</h1>")
			piInfo()
				
			return '4K'
		elif isFullHouse(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a FULL HOUSE!</h1>")
			piInfo()

			return 'FH'
		elif isFlush(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a FLASH!</h1>")
			piInfo()

			return 'FL'
		elif isStraight(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a STRAIGHT!</h1>")
			piInfo()

			return 'ST'
		elif isThreeOfAKind(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a THREE OF A KIND!</h1>")
			piInfo()

			return '3K'
		elif isTwoPair(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a TWO PAIR!</h1>")
			piInfo()

			return '2P'
		elif isOnePair(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a ONE PAIR!</h1>")	
			piInfo()

			return '1P'
		elif isHighCard(cards):
			cardsPrint(cards)
			print("<h1>Your Poker Hand represents a HIGH CARD!</h1>")
			piInfo()

			return 'HC'

	def isStraightFlush(cards):
		rankList=[]
		valueList=[]

		for i in range (len(cards)):

			rankList.append(cards[i][1])
			valueList.append(cards[i][0])

		rmvDuplicates = list(dict.fromkeys(rankList))
		
		if ("2" in valueList and "3" in valueList and "4" in valueList and "5" in valueList and "6" in valueList  and ((len(rmvDuplicates)) == 1)) or ("3" in valueList and "4" in valueList and "5" in valueList and "6" in valueList and "7" in valueList  and ((len(rmvDuplicates)) == 1)) or ("4" in valueList and "5" in valueList and "6" in valueList and "7" in valueList and "8" in valueList  and ((len(rmvDuplicates)) == 1)) or ("5" in valueList and "6" in valueList and "7" in valueList and "8" in valueList and "9" in valueList  and ((len(rmvDuplicates)) == 1)) or ("6" in valueList and "7" in valueList and "8" in valueList and "9" in valueList and "t" in valueList  and ((len(rmvDuplicates)) == 1)) or ("7" in valueList and "8" in valueList and "9" in valueList and "t" in valueList and "j" in valueList  and ((len(rmvDuplicates)) == 1)) or ("8" in valueList and "9" in valueList and "t" in valueList and "j" in valueList and "q" in valueList  and ((len(rmvDuplicates)) == 1)) or ("9" in valueList and "t" in valueList and "j" in valueList and "q" in valueList and "k" in valueList  and ((len(rmvDuplicates)) == 1)) or ("t" in valueList and "j" in valueList and "q" in valueList and "k" in valueList and "a" in valueList  and ((len(rmvDuplicates)) == 1)):
		
			return True
		else: return False

	def isFourOfAKind(cards) :
		rankList=[]

		for i in range (len(cards)):

			rankList.append(cards[i][0])

		if (rankList.count(rankList[0]) == 4) or (rankList.count(rankList[1]) == 4):
			return True
		else: return False

	def isFullHouse(cards) :
		rankList= []

		for i in range (len(cards)):

			rankList.append(cards[i][0])

		

		if (rankList.count(rankList[0]) == 3 or rankList.count(rankList[1]) == 3 or rankList.count(rankList[2]) == 3 or rankList.count(rankList[3]) == 3 or rankList.count(rankList[4]) == 3) and (rankList.count(rankList[0]) == 2 or rankList.count(rankList[1]) == 2 or rankList.count(rankList[2]) == 2 or rankList.count(rankList[3]) == 2 or rankList.count(rankList[4]) == 2):
			return True
		else: return False

	def isFlush(cards):
		rankList= []

		for i in range (len(cards)):

			rankList.append(cards[i][1])

		if (rankList.count(rankList[0]) == 5):
			return True
		else: return False

	def isStraight(cards):
		cardValList = []

		for i in range (len(cards)):

			cardValList.append(cards[i][0])

		if ("2" in cardValList and "3" in cardValList and "4" in cardValList and "5" in cardValList and "6" in cardValList ) or ("3" in cardValList and "4" in cardValList and "5" in cardValList and "6" in cardValList and "7" in cardValList ) or ("4" in cardValList and "5" in cardValList and "6" in cardValList and "7" in cardValList and "8" in cardValList ) or ("5" in cardValList and "6" in cardValList and "7" in cardValList and "8" in cardValList and "9" in cardValList ) or ("6" in cardValList and "7" in cardValList and "8" in cardValList and "9" in cardValList and "t" in cardValList ) or ("7" in cardValList and "8" in cardValList and "9" in cardValList and "t" in cardValList and "j" in cardValList ) or ("8" in cardValList and "9" in cardValList and "t" in cardValList and "j" in cardValList and "q" in cardValList ) or ("9" in cardValList and "t" in cardValList and "j" in cardValList and "q" in cardValList and "k" in cardValList ) or ("t" in cardValList and "j" in cardValList and "q" in cardValList and "k" in cardValList and "a" in cardValList ):
			return True
		else: return False

	def isThreeOfAKind(cards) :
		cardValList = []

		for i in range (len(cards)):

			cardValList.append(cards[i][0])

		if (cardValList.count(cardValList[0]) == 3 or cardValList.count(cardValList[1]) == 3 or cardValList.count(cardValList[2]) == 3):
			return True
		else: return False

	def isTwoPair(cards) :
		cardValList = []

		for i in range (len(cards)):

			cardValList.append(cards[i][0])

		rmvDuplicates = list(dict.fromkeys(cardValList))

		if (len(rmvDuplicates) == 3):
			return True
		else: return False

	def isOnePair(cards) :
		cardValList = []

		for i in range (len(cards)):

			cardValList.append(cards[i][0])

		rmvDuplicates = list(dict.fromkeys(cardValList))

		if (len(rmvDuplicates) == 4):
			return True
		else: return False

	def isHighCard(cards) :
		if not isOnePair(cards) and not isTwoPair(cards) and not isThreeOfAKind(cards) and not isStraight(cards) and not isFlush(cards) and not isFullHouse(cards) and not isFourOfAKind(cards) and not isStraightFlush(cards):
			return True
		else: return False

	def cardsPrint(cards):
		cardValueFromLowToHigh = "23456789tjqka"
		temp =""

		for i in range (len(cards)):
			for j in range (i+1, len(cards)):
				if(cardValueFromLowToHigh.index(cards[i][0]) > cardValueFromLowToHigh.index(cards[j][0])):
					temp = cards[i]
					cards[i] = cards[j]
					cards[j] = temp
		

		for i in range (len(cards)):
				cardPath = '../cards/' + cards[i] + '.png'

				print("<img src=" + cardPath + " width = \"37\" height = \"53\">")
	startPage()

	if bbutton == "Check Poker Hand" and cards and len(cards) == 5:
		findCategory(cards)

	if cards and len(cards) != 5:
		print("You have chosen wrong amount of cards.")

def piInfo():
	print("<div>")
	print(subprocess.check_output("date", shell=True, text=True))
	print("</div>")
	print("<div>")
	print(subprocess.check_output("ps ax | grep nginx", shell=True, text=True))
	print("</div>")
	print("<div>")
	print(subprocess.check_output("uname -a", shell=True, text=True))
	print("</div>")
	print("<div>")	
	print(subprocess.check_output("cat /sys/class/net/eth0/address", shell=True, text=True))
	print("</div>")
	print("<div>")
	print(subprocess.check_output("cat /proc/cpuinfo | tail -5", shell=True, text=True))
	print("</div>")
	print("<div>")
	print(subprocess.check_output("ifconfig | grep netmask", shell=True, text=True))
	print("</div>")
	
if __name__ == "__main__" :
   main( )