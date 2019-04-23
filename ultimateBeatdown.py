import datetime
import time
import simulateCombat
import tournamentManager

time.sleep(0.5)
print("\n Welcome to ULTIMATE BEATDOWN! \n")
time.sleep(0.5)

for n in range(1,1000):
	print("Select battle mode:")	
	form = ["arena", "story","tournament","ladder"]
	userForm = input("`arena`, `tournament`,`ladder`, `exit`: ")	
	if userForm == "story":
		print("\n")
		time.sleep(0.5)
		print("Coming soon!\n")
		time.sleep(0.5)
		continue
	
	if userForm == "tournament":
		print("\n")
		time.sleep(0.5)
		#run tournament
		characters = simulateCombat.generalSelect()
		i = 1
		while len(characters) > 1:
			print("Round "+str(i))
			characters = tournamentManager.Bracket(characters)
			i += 1
		continue

	if userForm == "tournament stats":
		print("Running tournament in statistics mode")
		startDT = datetime.datetime.now()
		print (str(startDT))
		champions = []
		print(".", end =" ")
		for n in range(1,33):
			characters = simulateCombat.generalSelect()
			print(".", end =" ")
			i = 1
			while len(characters) > 1:
				characters = tournamentManager.BracketStats(characters)
				i += 1
				print(".", end =" ")
			if len(characters) == 1:
				champions.append(characters)
				print(".", end =" ")
		for champion in champions:
			print("\n")
			print(champion[0].name)
			print(champions.count(champion))
		endDT = datetime.datetime.now()
		print (str(endDT))
		continue
	
	elif userForm == "ladder":
		print("\n")
		time.sleep(0.5)
		#run ladder
		characters = simulateCombat.singleSelect()
		player = characters[0]
		opponents = characters[1]
		victor = player
		while victor == player:
			victor = tournamentManager.Ladder(player, opponents)
		continue
	
	elif userForm == "arena":
		mode = 1 #verbose output
		print("\n")
		#run basic arena combat		
		prophets = simulateCombat.fighterSelect()

		print("\n")
		time.sleep(1)
		print("Get ready...")
		time.sleep(1)
		print("BATTLE!\n")
		time.sleep(1)

		print(prophets[0].longName+" vs. "+prophets[1].longName+"\n")
		time.sleep(1)		
		simulateCombat.runBattle(prophets, mode)

		print("BATTLE SIMULATION COMPLETE\n")

	elif userForm == "exit":
		break
	else:
		continue

