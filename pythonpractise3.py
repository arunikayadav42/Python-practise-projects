import random 

class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy(23, 24)
enemy1.getAtk();

'''		

	playerhp = 260;
	enemyatkl = 60;
	enemyatkh = 80;

while playerhp > 0:
	global playerhp
	dmg = random.randrange(enemyatkl, enemyatkh)
	playerhp = playerhp - dmg

	if playerhp <= 30:
		playerhp = 30

	print("Enemy strikes for",dmg,"points of damage.Current HP is",playerhp)

	if playerhp > 30:
		continue	

	print("You have low health.You've been teleported to the nearest inn.")
	break
'''