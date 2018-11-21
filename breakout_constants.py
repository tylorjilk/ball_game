"""
This file contains constants to be used for breakout.py
"""

# Display Settings
FPS = 60 						# frames per second setting
DISPLAY_WIDTH = 800				# Width of the display window, in pixels
DISPLAY_HEIGHT = 500			# Height of the display window, in pixels
DISPLAY_CAPTION = 'Breakout'	# Caption of the display window (a string)

#Colors
WHITE = (255, 255, 255),
BLACK = ( 0, 0,0),
AQUA = ( 0, 255, 255),
BLUE = ( 0, 0, 255),
FUCHSIA = (255, 0, 255),
GRAY = (128, 128, 128),
GREEN = ( 0, 128, 0),
LIME = ( 0, 255, 0),
MAROON = (128, 0, 0),
NAVY_BLUE = ( 0, 0, 128),
OLIVE = (128, 128, 0),
PURPLE = (128, 0, 128),
RED = (255, 0, 0),
SILVER = (192, 192, 192),
TEAL = ( 0, 128, 128),
YELLOW = (255, 255, 0)

# Ball constants
ballVX = 0 					# Initial x velocity
ballVY = 0 					# Initial y velocity
ballRadius = 10 			# radius of the ball, in pixels
#ballX = DISPLAY_WIDTH/2		# Initial x position
ballY = DISPLAY_HEIGHT/2	# Initial y position
ballX = 700
ballColor = TEAL			# Color of the ball
ballVXMax = 5				# Max x velocity magnitude
ballVYMax = 8				# Max y velocity magnitude
ballVXMin = 3				# Min x velocity magnitude
ballVYMin = 5				# Min y velocity magnitude

# Paddle constants
paddleYOffset = 20			# Distance from bottom of paddle to bottom of screen
paddleWidth = 100			# Width of paddle
paddleHeight = 20			# Height of paddle
paddleX = DISPLAY_WIDTH/2 - paddleWidth/2				# Initial x position
paddleY = DISPLAY_HEIGHT - paddleYOffset - paddleHeight	# Initial y position
paddleColor = FUCHSIA		# Color of the paddle