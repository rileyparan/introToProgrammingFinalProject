# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - tutorial
import pygame 
import random 

# Global functions - variables created outside of a function 
s_width = 800 
s_height = 700 
play_width = 300 
        # 300/10  = 30 width per block 
play_height = 600 
        # 600/20 = 30 height per block 
block_size = 30
        # shapes of the blocks 

# represents top left position of the play area - drawing blocks/collisions
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS 
        # multiple lists inside of lists 
        # the periods represent a 5x5 grid - 0's represent the physical block 

# two rotations
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
# one rotation 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
# two rotations 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
# one rotation 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
# four rotations 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
# four rotations 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
# four rotations 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# list (index 0-6) that holds all potential blocks  
shapes = [S, Z, I, O, J, L, T]
# colors of the corresponding blocks 
shapeColors = [(0,275,0), (275,0,0), (0,275,275), (275,275,0), (275,150,0), (0,0,275), (135,0,135)]

class Piece (object): 
        def __init__(self, x, y, shape):
                self.x = x
                self.y = y
                self.shape = shape
                self.color = shapeColors[shapes.index(shape)]
                self.rotation = 0