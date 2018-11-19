"""
This file contains constants to be used for breakout.py
"""

# Display Settings
FPS = 60 # frames per second setting
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 450
DISPLAY_CAPTION = 'Breakout'

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
ballVX = 0
ballVY = 0
ballRadius = 10 # radius of the ball, in pixels
ballX = DISPLAY_WIDTH/2
ballY = DISPLAY_HEIGHT/2
ballColor = TEAL
ballVXMax = 15
ballVYMax = 15
ballVXMin = 10
ballVYMin = 10

# Paddle constants
paddleYOffset = 10
paddleWidth = 35
paddleHeight = 10
paddleX = DISPLAY_WIDTH/2 - paddleWidth/2
paddleY = DISPLAY_HEIGHT - paddleYOffset - paddleHeight
paddleColor = FUCHSIA