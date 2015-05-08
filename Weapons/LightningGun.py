#LightningGun.py

import classes

class LightningGun(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'LightningGun', firepower = 4, tracking = 2, splash = 1, ammo = 6, rate = 3)
