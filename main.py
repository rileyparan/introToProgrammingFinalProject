# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - tutorial reference (source)
# https://data-flair.training/blogs/python-tetris-game-pygame/ - tetris game (source)
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 - tetris game (m - source)
# https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FExamples%2Fclasses%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FExamples- classes Mr. Cozort 

import pygame 
import random 

# represents the corresponding shades of light onto the blocks 
# randomly chosen 
colors = [
        # RED 
        (255,0,0),
        # VIOLET
        (134,1,175),
        # BLACK
        (0,0,0),
        # BLUE
        (0,0,254),
        # GREEN
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
                self.y = y
                self.x = x
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
        SCORE = 0 
        state = "begin" 
        height = 0 
        width = 0
        y = 60
        x = 100 
        field = []
        level = 3 
        zoom = 25
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
        
        
# creates and puts the NEW BLOCK at the new position (at the coordinates of 3,0)
        def new_figure(self): 
                self.figure = Figure(3,0)
 
# checks to see if it touches the top of board, if true it ends the game 
        def intersects(self): 
                intersection = False
                # at 4 (limit) because I set the level at 3 (if i decide to change the level #)
                for i in range(4):
                        for j in range(4):
                                if i * 4 + j in self.figure.image():
                                        if i + self.figure.y > self.height - 1 or \
                                                j + self.figure.x > self.width - 1 or \
                                                j + self.figure.x < 0 or \
                                                self.field[i + self.figure.y][j + self.figure.x] > 0:
                                                intersection = True
                return intersection

# destorys the blocks upon intersection (bottom block to top)
# checks to see if the blocks form in any row 
# if true, ups the score by 1 and erases the line 
        def break_lines(self):
                lines = 0
                for i in range(1, self.height):
                        zeros = 0
                for j in range(self.width):
                        if self.field[i][j] == 0:
                                zeros += 1
                        if zeros == 0:
                                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
                self.score += lines ** 2
# similiar to "go_down," but moves the block entirely down to the bottom
        def go_space(self): 
                while not self.intersects(): 
                        self.figure.y +=1
                self.figure.y -=1
                self.freeze()
# allows to move the block down a unit 
        def go_down(self): 
                self.figure.y +=1
                if self.intersects(): 
                        self.figure.y -=1
                        self.freeze()

# runs once the block reaches the bottom floor
        def freeze(self): 
                for i in range(4): 
                        for j in range(4):
                                if i * 4 + j in self.figure.image(): 
                                        self.field[i+self.figure.y][j+self.figure.x] = self.figure.color 
                # new row formed
                self.break_lines()
                # creates new blocks
                self.new_figure()
                # if any blocks go to the top and touch the top of the board, automatically ends game with "GAMEOVER"
                if self.intersects():
                        self.state = "GAMEOVER"

# allows to move the block either left or right 
        def go_totheside(self, dx): 
                old_x = self.figure.x
                self.figure.x = dx 
                if self.intersects(): 
                        self.figure.x = old_x

# allows to rotate the block 90 degrees clockwise/counter-clockwise 
# freely choose which direction you want to rotate
        def rotate(self): 
                old_rotation = self.figure.rotation
                self.figure.rotate()
                if self.intersects(): 
                        self.figure.rotation = old_rotation     

# initializing pygame 
pygame.init() 

# background colors 
GRAY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)

SIZE = (400,800)


pygame.display.set_caption("TETRIS BY RILEY PARAN")
screen = pygame.display.set_mode(SIZE)

done = False
fps = 25
game = Tetris(20,10)
clock = pygame.time.Clock()
counter = 0 

font = pygame.font.SysFont('TIMESNEWROMAN', 30, True, False)
font1 = pygame.font.SysFont('TIMESNEWROMAN', 70, True, False)
text_game_over = font1.render("GAME OVER", True, (255,125,0))
text_game_over1 = font1.render("PRESS ESC", True, (255,215,0))
text = font.render("SCORE: " + str(game.score), True, BLACK)

press_down = False 

