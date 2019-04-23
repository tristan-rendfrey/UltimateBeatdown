import time
import random
import math

def Socrates(smarts, mode):

###
#The Hoplite: random chance to gain intellect during combat.
###
	if smarts <= 9.5:
		riddle = random.randint(1,4)
		question = random.randint(1,4)
		if question == riddle:
			if mode == 1:
				#dialogues.socrates()
				time.sleep(0.5)
				print("SOCRATES:\"I should no sooner retreat from philosophy, than a hoplite from battle!\"")
				time.sleep(1.0)
				print("Socrates gained an intelligence boost!")
			smarts += 2.5
	return smarts

def Pythagoreas(winningPower, mode):
###
#Theorem: roll a six sided die three times. if 3, 4, or 5 are rolled, add 1 to power. if all three are rolled, multiply winning power by 2  
###
	#could be a loop, but isn't for now
	leg1 = random.randint(1,6)
	leg2 = random.randint(1,6)
	leg3 = random.randint(1,6)

	hypo = 0
	if leg1 == (3 or 4 or 5):
		winningPower += 1
		hypo += 1
		if mode == 1:
			time.sleep(0.5)
			#dialogues.pythagoreas(1)
			print("PYTHAGOREAS:\"a squared plus b squared...\"")
			time.sleep(1.0)
		if leg2 == (3 or 4 or 5):
			winningPower += 1
			hypo += 1
			if mode == 1:
				#dialogues.pythagoreas(2)
				time.sleep(0.5)
				print("\"...equals c squared!\"")
				time.sleep(0.5)
			if leg3 == (3 or 4 or 5):
				winningPower += 1
				hypo += 1
				if mode == 1:
					#dialogues.pythagoreas(2)
					time.sleep(0.5)
					print("\"You know my theorem...\"")
				if hypo == 3:
					winningPower *= 3
					if mode == 1:
						#dialogues.pythagoreas(3)
						time.sleep(1.0)
						print("\"...but can you prove it?\"")
						time.sleep(1.0)

	return winningPower

def Alexander(winningPower, speed, mode):
###
#Companion Cavalry: when Alexander would do 8.5 or more damage, add 1 to his speed
###
	if speed <= 9.0:
		if winningPower >= 8.5:
			speed += 1.0
			if mode == 1:
				#dialogues.alexander()
				time.sleep(0.5)
				print("ALEXANDER:\"Nothing outruns my army.\"")
				time.sleep(0.5)
				print("Alexander got a speed boost from his cavalry!")
	return speed 

def Leonidas(winningPower, health, mode):

#Thermopylae: Leonidas does +3 damage if he has less than 20 health, and x2 damage below 10. 

	if health <= 10:
		if mode == 1:
			time.sleep(0.5)
			print("\"This! Is! Sparta!\"")
			time.sleep(1.0)
		winningPower *= 2
	
	elif health <= 20:
		if mode == 1:
			time.sleep(0.5)
			print("\"Tonight, we dine in hell!\"")
			time.sleep(1.0)
		winningPower += 3

	return winningPower

def Confucius(winningPower, health, mode):

#The Righteous Path: Confucius gains health when he is dealt  more than 10 damage.

	coin = random.randint(1,2)
	if coin == 1:
		if winningPower >= 10.0:
			if mode == 1:
				time.sleep(0.5)
				print("CONFUCIUS:\"You will learn to respect your elders.\"")
				print("Confucius gained 10 health!\n")
				time.sleep(1.0)
			health += 10
	return health

def Laozi(winningPower, mode):
	nirvana = random.randint(1,4)
	peace = random.randint(1,4)
	if nirvana == peace:
		if mode == 1:
			time.sleep(0.5)
			print("Laozi becomes one with the Tao!!")
			time.sleep(1)
		winningPower /= 2.0
	return winningPower

def SunTzu(winningPower, health, mode):

#The Art of War: Sun Tzu does x2 damage when his health is below 10, and halves incoming damage when his health is above 35. 

	rollDialogue = random.randint(1,6)
	artOfWar = random.randint(1,6)
	if rollDialogue == artOfWar:
		if mode == 1:
			time.sleep(0.5)
			print("SUN TZU\"Appear weak when you are strong, and strong when you are weak.\"")
			time.sleep(1.0)
	if health >= 35.0:
		winningPower /= 2.0
	if health <= 10:
		winningPower *= 2.0
	return winningPower 

def QinShiHuang(winningPower, mode):

#Subjugate: Qin Shi Huang does double crit damage.

	if mode == 1:
		time.sleep(0.5)
		print("\"Welcome to the empire of Qin. Kneel before your emperor.\"")
		time.sleep(1.0)
		print("The critical hit does 5 extra damage!")
	winningPower += 5.0
	return winningPower	

def Empire(mode):

#Triumph of Aeneas: Romans have a higher chance of critical damage hits.

	affinity = random.randint(1,4)
	divinity = random.randint(1,4)
	if affinity == divinity:	
		if mode == 1:
			time.sleep(0.5)
			print("\"Observe the grandeur of the Roman empire.\"")
			time.sleep(1.0)
	return [affinity, divinity]

def Republic(winningPower, mode):

#Res Publica: Romans absorb would-be crit damage.

	if mode == 1:
		time.sleep(0.5)
		print("\"The republic is stronger than you will ever be.\"")
		time.sleep(1.0)
	winningPower = (-1)*(winningPower / 4.0)
	return winningPower
	
def Egypt(injHealth, name,  mode):

#The eternal dynasty: random chance for +10 health gain on hit.

	kingdom = random.randint(1,4)
	pharaoh = random.randint(1,4)
	if kingdom == pharaoh:
		if mode == 1:
			time.sleep(0.5)
			print("\"This kingdom has survived a thousand years. It will not die now.\"")
			time.sleep(0.5)
			print("%s  gains 10 health!" %name)
			time.sleep(0.5)
		injHealth += 10
	return injHealth

def Ramesses(attack, mode):

#The New Kingdom: Ramesses can rally the Egyptian army for +5 attack power

	rally = random.randint(1,4)
	rule = random.randint(1,4)
	if rally == rule:
		if mode == 1:
			time.sleep(1)
			print("Ramesses rallies the Egyptian army!")
			time.sleep(1)
		attack += 5.0
	return attack

#def Imhotep(imhotep, phase, mode):
#the original polymath: Imhotep multiplies the effect of an item
#no items are yet implemented, so Imhotep uses Egypt


