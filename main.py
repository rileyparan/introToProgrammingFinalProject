# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - tutorial reference 
# https://data-flair.training/blogs/python-tetris-game-pygame/ - tetris game 
import pygame 
import random 

# Global functions - variables created outside of a function 
s_width = 800 
s_height = 700 
play_width = 300 
        # 300/10  = 30 width per piece 
play_height = 600 
        # 600/20 = 30 height per piece 
piece_size = 30
        # shapes of the pieces  

# represents top left position of the play area - drawing pieces/collisions
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height - 50 

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

# colors of the corresponding pieces  
shapeColors = [(0,275,0), (275,0,0), (0,275,275), (275,275,0), (275,150,0), (0,0,275), (135,0,135)]

# this class assigns the shape, color, rotation of the pieces created
# the library "random" assigns random shapes/colors to the specific pieces 
class Piece: 
        x = 0 
        y = 0 
        t = 0 
        def __init__(self,x,y,width,height,t,color,block,field): 
                self.x = x 
                self.y = y 
                self.width=width
                self.height=height
                self.rotation = 0
                self.type = t
                self.color = color
                self.block= block(x,y)
                self.field=field
                
        def image(self):
            return shapes[self.type][self.rotation]
                
# index of 'rotating' an image by angle  
        def rotate(self): 
                self.rotation = (self.rotation + 1) % len(shapes[self.type])
# returns the rotated 'images' onto screen 
        def image(self): 
                return shapes [self.type][self.rotation]
# creates new pieces      
        def new_piece(self): 
                self.piece = Piece(3,0,random.randint(0,len(shapes)-1))
        def next_piece(self): 
                # creates the next piece to show up on screen  
                self.nextPiece = Piece(3,0,random.randint(0,len(shapes)-1))

# examines if pieces touch ceiling of board 
# also decides if end of game 
        def intersects (self): 
                intersection = False 
                for i in range(4): 
                        for j in range(4):
                                if i * 4 + j in self.block.image(): 
                                        if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field[i + self.block.y][j + self.block.x] > 0:
                                                intersection = True
                return intersection 

#checks if the pieces form any row 
# if the statement is true, increases the score and the line erases 
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

# places the next block next to main to show to player 
def draw_next_piece(self,screen): 
        font = pygame.font.SysFont("TIMESNEWROMAN", 25)
        label = font.render("Next Shape", 1, (130,130,130))
        
        sx = top_left_x + play_width + 50
        sy = top_left_y + play_height/2 - 100
        
        format = self.nextPiece.image()
        for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in self.nextPieceimage():
                        pygame.draw.rect(screen, shapeColors[self.nextPiece.color],(sx + j*30, sy + i*30, 30, 30), 0)

# moves the pieces down a unit 
def go_down (self): 
        self.block.y += 1
        if self.intersects():
                self.block.y -= 1
                self.freeze()
