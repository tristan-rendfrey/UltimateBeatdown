import time
import random
import specialLibrary

def modifiers(attacker, atkSpeed, atkSmarts, defender, defSpeed, defSmarts, mode):
	#get attacker and defender modifier
	
	#god's intervention, yet to be decidede
	smite = 0.0 
	armor = 0.0

	#determine possible skill boost
	skillMod= random.randint(1,10)
	atkSkill = random.randint(1,10) 
	defSkill = random.randint(1,10)

	if skillMod == atkSkill:
		if mode == 1:
			print("A flawless attack!!")
		smite = 10.0
	elif skillMod == defSkill:
		if mode == 1:
			print("Perfectly defended!!")
		armor = 10.0

	#determine battle random modifiers 
	atkModNum = random.uniform(.25,1)
	defModNum = random.uniform(.25,1)

	#calculate modifiers
		
	atkModifier = (atkModNum * (atkSpeed + atkSmarts) ) + smite
	defModifier = (defModNum * (defSpeed + defSmarts) ) + armor

	return [atkModifier, defModifier]
	
def attack(attacker, atkr, atkMod, defender, defr, defMod, mode):

	if attacker.name == 'Ramesses':
		atkr = specialLibrary.Ramesses(atkr, mode)

	atkPower = atkr + atkMod
	defPower = defr + defMod

	if mode == 1:
		time.sleep(0.5)
		print("attacking power:")
		print('%.3f' % atkPower)
		time.sleep(0.5)
		print("defending power:")
		print('%.3f' % defPower)
		time.sleep(0.5)

	if atkPower > defPower:
		return attacker
	else:
		return defender	

def damageManager(injHealth, winningHealth, winningPower, injured, victor, injSpeed, winningSpeed, injSmarts, winningSmarts, mode):

	#run character specials (that do not require power calculation)
	if injured == 'Socrates':
		injSmarts = specialLibrary.Socrates(injSmarts, mode)
	if victor == 'Socrates':
                winningSmarts = specialLibrary.Socrates(winningSmarts, mode)

	#roll damage modifier
	damageMod = random.randint(1,6)
	winningPower += damageMod

	#run character special modifiers (to power)
	if victor == 'Pythagoreas':
		winningPower = specialLibrary.Pythagoreas(winningPower, mode)	
	if victor == 'Alexander':
		winningSpeed = specialLibrary.Alexander(winningPower, winningSpeed, mode)
	if victor == 'Leonidas':
		winningPower = specialLibrary.Leonidas(winningPower, winningHealth, mode)
	if injured == 'Laozi':
		winningPower = specialLibrary.Laozi(winningPower, mode)
	if victor == 'Sun Tzu':
		winningPower = specialLibrary.SunTzu(winningPower, winningHealth, mode)
	if injured == 'Sun Tzu':
		winningPower = specialLibrary.SunTzu(winningPower, injHealth, mode)
	
	#calculate character modifiers (crit dependent)
	#calculate crit too
	if victor == ("Augustus"):
		crits = specialLibrary.Empire(mode)
		divinity = crits[1]
		affinity = crits[0]
	if victor == ("Virgil"):
		crits = specialLibrary.Empire(mode)
		divinity = crits[1]
		affinity = crits[0]	
	else:
		divinity = random.randint(1,8)
		affinity = random.randint(1,8)

	if divinity == affinity:
		if mode == 1:
			time.sleep(1)
			print("A critical hit!")
		winningPower *= 2.0
		
		if injured == ('Cicero' or 'Scipio'):
			winningPower = specialLibrary.Republic(winningPower, mode)
		if victor == 'Qin Shi Huang':
			winningPower = specialLibrary.QinShiHuang(winningPower, mode)


	#calculate damage and resistance
	damage = winningPower + ( ((winningSpeed)*(1/2)) + ((winningSmarts)*(1/3)) )
	resistance = ( ((injSpeed)*(1/4)) + ((injSmarts)*(1/4)) )

	if (damage - resistance) < 0:
		if mode == 1:
			print("Absorbed %.1f damage!\n" %(resistance - damage))
			time.sleep(1.0)	
	else:
		if mode == 1:
			print("%.1f damage!\n" %(damage - resistance))
			time.sleep(1.0)

	#run health based special abilities
	if injured == 'Confucius':
		health = specialLibrary.Confucius(winningPower, injHealth, mode)
	if injured == ('Akhenaten'):
		injHealth = specialLibrary.Egypt(injHealth, injured, mode) 
	if injured == ('Hatshepsut'):
		injHealth = specialLibrary.Egypt(injHealth, injured, mode)
	if injured == ('Imhotep'):
		injHealth = specialLibrary.Egypt(injHealth, injured, mode)

	newHealth = injHealth - damage + resistance
	if newHealth < 0:
		newHealth = 0
	return newHealth
