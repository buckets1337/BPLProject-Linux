#ccinator.py

import classes

class ccinator(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'ccinator', firepower = 3, tracking = 5, splash = 2, ammo = 6, rate = 2)
