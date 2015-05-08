#MP7.py

import classes

class MP7(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'MP7', firepower = 45, tracking = 1, splash = 1, ammo = 12, rate = 6)