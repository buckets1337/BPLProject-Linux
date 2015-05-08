# WaterGun.py
# a sample weapon definition.  This one is really weak, though


import classes

class WaterGun(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'WaterGun', firepower = 2, tracking = 2, splash = 2, ammo = 3, rate = 1)





