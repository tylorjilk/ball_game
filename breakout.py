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

class Ball:
	def __init__(self, x, y, vx, vy, col, rad):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.color = col
		self.radius = rad

class Paddle:
	def __init__(self, x, y, wid, ht, col):
		self.x = x
		self.y = y
		self.width = wid
		self.height = ht
		self.color = col

ball = Ball(bc.ballX, bc.ballY, bc.ballVX, bc.ballVY, bc.ballColor, bc.ballRadius)
paddle = Paddle(bc.paddleX, bc.paddleY, bc.paddleWidth, bc.paddleHeight, bc.paddleColor)

def main():
	pygame.init()
	fpsClock = pygame.time.Clock()

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
	ball.vx = random.uniform(bc.ballVXMin, bc.ballVXMax)
	if bool(random.getrandbits(1)):
		ball.vx = -ball.vx
	ball.vy = random.uniform(bc.ballVYMin, bc.ballVYMax)
	if bool(random.getrandbits(1)):
		ball.vy = -ball.vy

def drawBall(DISPLAYSURF):
	pygame.draw.circle(DISPLAYSURF, ball.color, (int(ball.x), int(ball.y)), ball.radius)

def drawPaddle(DISPLAYSURF):
	pygame.draw.rect(DISPLAYSURF, paddle.color, (paddle.x, paddle.y, paddle.width, paddle.height))

def checkBallPath():
	checkDisplayEdges()
	checkPaddleCollision()

def moveBall():
	ball.x += ball.vx
	ball.y += ball.vy
	
def checkDisplayEdges():
	# Check right edge
	if (ball.x + ball.radius + ball.vx >= bc.DISPLAY_WIDTH):
		ball.vx = -ball.vx
	# Check left edge
	if (ball.x - ball.radius + ball.vx <= 0):
		ball.vx = -ball.vx
	# Check top edge
	if (ball.y - ball.radius + ball.vy <= 0):
		ball.vy = -ball.vy
	# Check bottom edge
	if (ball.y + ball.radius + ball.vy >= bc.DISPLAY_HEIGHT):
		ball.vy = -ball.vy
	
def checkPaddleCollision():
	# Check top edge
	if (ball.y + ball.radius <= paddle.y and ball.y + ball.radius + ball.vy >= paddle.y and ball.x + ball.vx <= paddle.x + paddle.width and ball.x + ball.vx >= paddle.x):
		ball.vy = -ball.vy
	# Check right edge
	if (ball.x - ball.radius >= paddle.x + paddle.width and ball.x + ball.vx - ball.radius <= paddle.x + paddle.width and ball.y + ball.vy >= paddle.y and ball.y + ball.vy <= paddle.y + paddle.height):
		ball.vx = -ball.vx
	# Check left edge
	if (ball.x + ball.radius <= paddle.x and ball.x + ball.vx + ball.radius >= paddle.x and ball.y + ball.vy >= paddle.y and ball.y + ball.vy <= paddle.y + paddle.height):
		ball.vx = -ball.vx
	# Check bottom edge
	if (ball.y - ball.radius >= paddle.y + paddle.height and ball.y - ball.radius + ball.vy <= paddle.y + paddle.height and ball.x + ball.vx >= paddle.x and ball.x + ball.vx <= paddle.x + paddle.width):
		ball.vy = -ball.vy

if __name__ == '__main__':
	main()