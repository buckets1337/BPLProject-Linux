#PARHANATANK.py

import classes

class PARHANATANK(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'PARHANATANK', firepower = 4, tracking = 5, splash = 3, ammo = 7, rate = 7)