#ArrowVolley.py

import classes

class ArrowVolley(classes.Weapon):
	def __init__(self):
		classes.Weapon.__init__(self, owner = None, name = 'ArrowVolley', firepower = 7 , tracking = 1, splash = 5, ammo = 1, rate = 1)
