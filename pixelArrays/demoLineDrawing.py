#demoLineDrawing.py
#an example of a picture drawn with pygame commands

## This first section is boilerplate.  This code should be in your script, unchanged.

# make sure pygame is loaded, even though it likely is from whatever is calling this array
import pygame
# call in CONFIG.py for the color definitions
import CONFIG

# make sure pygame is initialized
pygame.init()

## END BOILERPLATE

class pixelArray():
	'''
	This is an example of a pixelArray object.  This would be used in the game as your player portrait
	'''

	def __init__(self):

		# First, define any colors we may need, if they are not already in CONFIG.py
		self.LIGHT_GREY = (150,150,150)
		self.YELLOW = (255,255,0)

		# ake a surface that we will draw pixels on.  It can be any size, but it will be re-formed to be 64x64 in the game.
		# Here, I used 19x23 as my size, because that is the size of the pixel art I am using for my picture
		self.surf = pygame.Surface((64,64))

		# fill the surface with a light grey background.  We could do any color here really, I just chose light grey
		self.surf.fill(self.LIGHT_GREY)

		# let the pixelArray know what pixels should be what color
		self.illustratePicture()

	def illustratePicture(self):
		'''
		creates the picture with a series of pygame calls
		'''
		pygame.draw.circle(self.surf, self.YELLOW, (32,32), 28, 0)		#outside circle, filled in yellow
		rect = pygame.Rect(10,5,44,49)
		pygame.draw.arc(self.surf, CONFIG.BLACK, rect, 3.66, 5.76, 1)		#circle that will form the mouth, colored black
		pygame.draw.line(self.surf, CONFIG.BLACK, (18,14), (18,24), 1)	#left eye, in black
		pygame.draw.line(self.surf, CONFIG.BLACK, (45,14), (45,24), 1)	#rigth eye, in black

