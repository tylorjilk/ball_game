import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second setting
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 450
DISPLAY_CAPTION = 'Color Switcher'

COLORS = {
	0	:	(255, 255, 255), # WHITE
	1	:	( 0, 0,0), # BLACK
	2	:	( 0, 255, 255), # AQUA
	3	:	( 0, 0, 255), # BLUE
	4	:	(255, 0, 255), # FUCHSIA
	5	:	(128, 128, 128), # GRAY
	6	:	( 0, 128, 0), # GREEN
	7	:	( 0, 255, 0), # LIME
	8	:	(128, 0, 0), # MAROON
	9	:	( 0, 0, 128), # NAVY_BLUE
	10	:	(128, 128, 0), # OLIVE
	11	:	(128, 0, 128), # PURPLE
	12	:	(255, 0, 0), # RED
	13	:	(192, 192, 192), # SILVER
	14	:	( 0, 128, 128), # TEAL
	15	:	(255, 255, 0) # YELLOW
}

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	counter = 0
	numColors = len(COLORS)

	# set up the window
	DISPLAYSURF = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
	pygame.display.set_caption(DISPLAY_CAPTION)

	while True:
		COLOR = updateBackgroundColor(counter, numColors)
		DISPLAYSURF.fill(COLOR)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fpsClock.tick(FPS)
		counter += 1
		if counter%(numColors*10) == 0:
			counter = 0
		
def updateBackgroundColor(counter, numColors):
	c = (counter/10)%numColors
	return COLORS[c]
		
	
if __name__ == '__main__':
	main()