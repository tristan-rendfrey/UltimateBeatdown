import time
import random

import battler
import specialLibrary
from classLibrary import *

def fighterSelect():

	characterSelect= [Socrates, Pythagoreas, Alexander, Leonidas, Confucius, Laozi, SunTzu, QinShiHuang, Virgil, Cicero, Scipio, Augustus, Hatshepsut, Imhotep, Ramesses, Akhenaten]
	
	print("Choose the fighters!\n(Select by entering the corresponding number.)")
	i = 0
	for charac in characterSelect:
		print(charac.name+" "+str(i))
		i += 1
	print("")

	#a = int(input("Player 1: "))
	#b = input("Player 2: ")
	
	while True:
		try:
			a = int(input("Player 1: "))
		except ValueError:
      			 print('Input needs to be a number.')
		else:
			if 0 <= a < (len(characterSelect)):
				break
			else:
				print('Does not correspond to a character!')
	while True:
		try:
                        b = int(input("Player 2: "))
		except ValueError: 
			print('Input needs to be a number.')
		else:
			if 0 <= b < (len(characterSelect)):
				break
			else:
				print('Does not correspond to a character!')

	prophets = [characterSelect[int(a)], characterSelect[int(b)]]
	#prophets = [specialSelect[a], specialSelect[b]]
	return prophets


def singleSelect():

	characterSelect= [Socrates, Pythagoreas, Alexander, Leonidas, Confucius, Laozi, SunTzu, QinShiHuang, Virgil, Cicero, Scipio, Augustus, Hatshepsut, Imhotep, Ramesses, Akhenaten]
	
	time.sleep(1)
	print("Choose your fighter!\n")
	i = 0
	for charac in characterSelect:
		print(charac.name+" "+str(i))
		i += 1
	print("")
	a = input("Player 1: ")

	prophet = characterSelect[int(a)]
	#prophets = [specialSelect[a], specialSelect[b]]
	return [prophet, characterSelect]


def generalSelect():
	
	characterSelect= [Socrates, Pythagoreas, Alexander, Leonidas, Confucius, Laozi, SunTzu, QinShiHuang, Virgil, Cicero, Scipio, Augustus, Hatshepsut, Imhotep, Ramesses, Akhenaten]
	
	return characterSelect

def runBattle(prophets,mode):

	for t in range(100):

		#run positioning
		randInt0 = random.uniform(0,1)
		randInt1 = random.uniform(0,1)
		
		initiative0 = (prophets[0].speed + prophets[0].smarts) * (randInt0)
		initiative1 = (prophets[1].speed + prophets[1].smarts) * (randInt1) 

		if initiative1 > initiative0:
			Atkr = prophets[1]
			Defr = prophets[0]
		else:
                	Atkr = prophets[0]
                	Defr = prophets[1]
		if mode == 1:
			print(Atkr.name+" attacks!")
			time.sleep(1)
			print(Defr.name+" must defend!")
			time.sleep(1)

		#run battle
		mods = battler.modifiers(Atkr, Atkr.speed, Atkr.smarts, Defr, Defr.speed, Defr.smarts, mode)
		AtkrMod = mods[0]
		DefrMod = mods[1]

		time.sleep(1.0)
		#run attack
		victor = battler.attack(Atkr, Atkr.attack, AtkrMod, Defr, Defr.defense, DefrMod, mode)
		if mode == 1:
			if victor == Atkr:
				print(victor.name+" lands the attack!")
			elif victor == Defr:
				print(victor.name+" defends and counters!")
			time.sleep(1.0)

		#update health
		if victor == prophets[0]:
			injured = prophets[1]
		else:
			injured = prophets[0]

		injured.health = battler.damageManager(injured.health, victor.health, victor.power, injured.name, victor.name, injured.speed, victor.speed, injured.smarts, victor.smarts, mode)

		if mode == 1:
			print(injured.name+" has %.1f health left!" %injured.health)
			print(victor.name+" still has %.1f health!\n" %victor.health)
			print("\n")
			time.sleep(1.0)

		if injured.health <= 0:
			if mode != 2:
				print(victor.name+" wins!!!\n")
				time.sleep(1.25)
			#reset health
			prophets[0].health = 50.0
			prophets[1].health = 50.0

			return victor
			break

	
