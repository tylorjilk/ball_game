import pygame, sys, random
from pygame.locals import *
import breakout_constants as bc

"""
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
"""

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()
	#ball = pygame.Ball()

	# set up the window
	DISPLAYSURF = pygame.display.set_mode((bc.DISPLAY_WIDTH, bc.DISPLAY_HEIGHT), 0, 32)
	pygame.display.set_caption(bc.DISPLAY_CAPTION)
	initializeBallValues()
	drawBall(DISPLAYSURF)
	drawPaddle(DISPLAYSURF)

	while True:
		DISPLAYSURF.fill(bc.WHITE)
		checkBallPath()
		moveBall()
		drawBall(DISPLAYSURF)
		drawPaddle(DISPLAYSURF)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fpsClock.tick(bc.FPS)

def initializeBallValues():
	bc.ballVX = random.uniform(bc.ballVXMin, bc.ballVXMax)
	if bool(random.getrandbits(1)):
		bc.ballVX = -bc.ballVX
	bc.ballVY = random.uniform(bc.ballVYMin, bc.ballVYMax)
	if bool(random.getrandbits(1)):
		bc.ballVY = -bc.ballVY

def drawBall(DISPLAYSURF):
	pygame.draw.circle(DISPLAYSURF, bc.ballColor, (int(bc.ballX), int(bc.ballY)), bc.ballRadius)

def drawPaddle(DISPLAYSURF):
	pygame.draw.rect(DISPLAYSURF, bc.paddleColor, (bc.paddleX, bc.paddleY, bc.paddleWidth, bc.paddleHeight))

def checkBallPath():
	checkDisplayEdges()
	checkPaddleCollision()

def moveBall():
	bc.ballX += bc.ballVX
	bc.ballY += bc.ballVY
	
def checkDisplayEdges():
	# Check right edge
	if (bc.ballX + bc.ballRadius + bc.ballVX >= bc.DISPLAY_WIDTH):
		bc.ballVX = -bc.ballVX
	# Check left edge
	if (bc.ballX - bc.ballRadius + bc.ballVX <= 0):
		bc.ballVX = -bc.ballVX
	# Check top edge
	if (bc.ballY - bc.ballRadius + bc.ballVY <= 0):
		bc.ballVY = -bc.ballVY
	# Check bottom edge
	if (bc.ballY + bc.ballRadius + bc.ballVY >= bc.DISPLAY_HEIGHT):
		bc.ballVY = -bc.ballVY
	
def checkPaddleCollision():
	

if __name__ == '__main__':
	main()