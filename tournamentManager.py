import simulateCombat
import random

def Ladder(player, opponents):
	wins = 0
	victor = player
	for opponent in opponents:
		if player == opponent:
			continue
		print(opponent.name+" challenges "+player.name+"!")
		if player == victor:
			match = [player,opponent]
			victor = simulateCombat.runBattle(match,1)
		
		if player != victor:
			print(player.name+" won "+str(wins)+" of the matches!")
			break
		wins += 1

def Bracket(opponents):
	#generate match seeding
	matches = []
	x = len(opponents)
	while x > len(matches):
		ranInt = random.randint(1,100) % x
		if ranInt not in matches:
			matches.append(ranInt)

	#run tournament
	winners = []
	lastIndex = int(len(opponents) - 1)
	pairs = int(len(opponents)/2)
	print("Begin!\n")
	for i in range(0,pairs):
		#pair off matches
		pair = [opponents[matches[i]],opponents[matches[lastIndex-i]]]
		print(pair[0].name+" vs. "+pair[1].name)
		#run combat (set argument to 0 for quick resolve)
		victor = simulateCombat.runBattle(pair,0)
		if victor == pair[0]:
			winners.append(pair[0])
		elif victor == pair[1]:
			winners.append(pair[1])
		else:
			print("A draw!\n")
	return winner

def BracketStats(opponents):
	#generate match seeding
	matches = []
	x = len(opponents)
	while x > len(matches):
		ranInt = random.randint(1,100) % x
		if ranInt not in matches:
			matches.append(ranInt)
	#run tournament
	winners = []
	lastIndex = int(len(opponents) - 1)
	pairs = int(len(opponents)/2)
	for i in range(0,pairs):
		#pair off matches
		pair = [opponents[matches[i]],opponents[matches[lastIndex-i]]]
		#run combat (set argument to 0 for quick resolve)
		victor = simulateCombat.runBattle(pair,0)
		if victor == pair[0]:
			winners.append(pair[0])
		elif victor == pair[1]:
			winners.append(pair[1])
		else:
			print("A draw!\n")
	return winners
