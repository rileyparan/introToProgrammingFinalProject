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

# format of the shapes 
shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

# colors of the corresponding blocks 
shapeColors = [(0,275,0), (275,0,0), (0,275,275), (275,275,0), (275,150,0), (0,0,275), (135,0,135)]

class Piece (object): 
        def __init__(self, x, y, shape):
                self.x = x
                self.y = y
                self.shape = shape
                self.color = shapeColors[shapes.index(shape)]
                self.rotation = 0