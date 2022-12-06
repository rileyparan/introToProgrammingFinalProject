# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - tutorial reference (source)
# https://data-flair.training/blogs/python-tetris-game-pygame/ - tetris game (source)
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 - tetris game (m - source)

import pygame 
import random 

# represents the corresponding shades of light onto the blocks 
# randomly chosen 
colors = [
        (255,0,0),
        (134,1,175),
        (0,0,0),
        (0,0,254),
        (0,255,0),
        (80,34,22),
        (180,34,22),
        (180,34,122),

]

# represents the line of blocks about where they'll be placed onto the grid 
# randomly chosen and picked 
class Figure: 
        x = 0 
        y = 0 

        figures = [
                [[1,5,9,13], [0,1,2,3]],
                [[1,2,5,9], [0,4,5,6], [1,5,9,10], [4,5,1,2]], 
                [[1,2,3,7], [4,5,6,8], [2,6,10,11], [0,4,5,6]],
                [[1,4,5,6], [1,5,9,6], [4,5,6,9], [1,5,6,9]],
                [[1,2,5,6]]
        ]
# defining a function = self / x / y 
# basically being able to randomize between shapes and colors 
# able to rotate the shapes 

        def __init__(self,x,y): 
                self.x = x
                self.y = y
                self.type = random.randint(0, len(self.figures) - 1)
                self.color = random.randint(1, len(colors) - 1)
                self.rotation = 0
                # giving the ability to turn the shapes in random positions and rotating the figures each time 
        def image(self): 
                return self.figures[self.type][self.rotation]
        def rotation(self): 
                self.rotation = (self.rotation + 1) % len(self.figures[self.type]) 
# initializing "tetris" with variables 
# field - data field to store the data and methods for defining behaviors 
        class Tetris: 
                score = 0 
                state = "begin" 
                height = 0 
                width = 0
                y = 60
                x = 100 
                field = []
                level = 3 
                zoom = 20
                figure  = None 

# calls and creates a framework with height x width 
# also creates new lines within the frame of the game 
        def __init__(self,height,width): 
                self.height = height
                self.width = width 
                self.field = []
                self.score = 0 
                self.state = "start"
                for i in range(height):
                        new_line = []
                for j in range(width): 
                        new_line.append(0)
                self.field.append(new_line)
        
        
# creates and puts the new block at the new position (at the coordinates of 3,0)
        def new_figure(self): 
                self.figure = Figure(3,0)
# checks if able to move or rotate the certain shape 
# if piece moves down and intersects = reached bottom (freezes the piece on the grid)
        def intersects(self): 
                intersection = False
                for i in range(4):
                        for j in range(4):
                                if i * 4 + j in self.figure.image():
                                        if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                                                intersection = True
                return intersection

