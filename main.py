# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - tutorial reference 
# https://data-flair.training/blogs/python-tetris-game-pygame/ - tetris game 
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
        [[4, 5, 9, 10], [2, 1, 5, 4]],
        [[6, 7, 5, 10], [0, 1, 5, 6]],
        [[12, 8, 5, 9], [0, 4, 5, 6], [1, 5, 9, 10], [5, 6, 7, 9]],
        [[1, 0, 4, 8], [4, 5, 6, 10], [2, 6, 10, 9], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 6], [4, 5, 6, 2], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

# colors of the corresponding blocks 
shapeColors = [(0,275,0), (275,0,0), (0,275,275), (275,275,0), (275,150,0), (0,0,275), (135,0,135)]

# this class assigns the shape, color, rotation of the pieces created
# the library "random" assigns random shapes/colors to the specific pieces 
class Piece: 
        x = 0 
        y = 0 
        t = 0 
        def __init__(self,x,y,t): 
                self.x = x 
                self.y = y 
                self.rotation = 0
                self.type = t
                self.color = t 
# index of 'rotating' an image by angle  
        def rotate(self): 
                self.rotation = (self.rotation + 1) % len(shapes[self.type])
# returns the rotated 'images' onto screen 
        def image(self): 
                return shapes [self.type][self.rotation]
# creates new blocks     
        def new_piece(self): 
                self.piece = Piece(3,0,random.randint(0,len(shapes)-1))
        def next_piece(self): 
                # creates the next block to show up on screen  
                self.nextPiece = Piece(3,0,random.randint(0,len(shapes)-1))

# examines if blocks touch ceiling of board 
# also decides if end of game 
        def intersects (self): 
                intersection = False 
        