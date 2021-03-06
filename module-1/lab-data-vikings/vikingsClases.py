from random import randrange

# Soldier
class Soldier:
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength

	def attack(self):
		return self.strength

	def receiveDamage(self, damage):
		self.health = self.health - damage


# Viking
class Viking(Soldier):
	def __init__(self, name, health, strength):
		self.name = name
		self.health = health
		self.strength = strength
	
	def receiveDamage(self, damage):
		self.health = self.health - damage

		if self.health > 0:
			return "{} has received {} points of damage".format(self.name, damage)
		else:
			return "{} has died in act of combat".format(self.name)
			

	def battleCry(self):
		return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength

	def receiveDamage(self, damage):
		self.health = self.health - damage

		if self.health > 0:
			return "A Saxon has received {} points of damage".format(damage)
		else:
			return "A Saxon has died in combat"
			
	

# War Bonus
class War:
	def __init__(self, Viking, Saxon):
		self.Viking = Viking
		self.Saxon = Saxon

	def addViking(self, viking):
		self.Viking.append(viking)

	def addSaxon(self, saxon):
		self.Saxon.append(saxon)

	def vikingAttack(self):
		self.Saxon[randrange(len(self.Saxon) - 1)].receiveDamage(self.Viking[randrange(len(Viking) - 1)].strength)

	def saxonAttack(self):
		self.Viking[randrange(len(self.Viking) - 1)].receiveDamage(self.Saxon[randrange(len(Saxon) - 1)].strength)

	def showStatus(self):
		if len(self.Saxon) == 0:
			return "Vikings have won the war of the century!"
		elif len(self.Viking) == 0:
			return "Saxons have fought for their lives and survive another day..."
		else:
			return "Vikings and Saxons are still in the thick of battle."