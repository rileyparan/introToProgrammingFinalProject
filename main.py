######################################################################################################################################
# https://www.techwithtim.net/tutorials/game-development-with-python/tetris-pygame/tutorial-1/ - youtube tutorial reference (source)
# https://data-flair.training/blogs/python-tetris-game-pygame/ - tetris game referencce (source)
# https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318 - tetris game (m - source)
# https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FExamples%2Fclasses%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FExamples- classes Mr. Cozort 
# https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FgameTutorials%2Fmain%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2FgameTutorials - main.py Mr. Cozort
######################################################################################################################################

# imported necessary libraries 
        # pygame for visual, random for randomizing blocks and colors 
import pygame
import random

# represents colors for blocks (randomly chosen)
colors = [
    # RED 
    (255,0,0),
    # BLACK
    (0, 0, 0),
    # BLUE 
    (0,0,254),
    # GREEN
    (0,255,0),
    # BROWN
    (150,75,0),
    #TURQUOISE
    (64, 224,208),
    #ORANGE
    (255,165,0),
    #PINK
    (255,105,180), 
    #YELLOW
    (255,255,0), 
    #VIOLET 
    (134,1,175),
]

# represents blocks - upon how they're placed upon the grid 
        # 1,5,9,13 is a vertical line = 4,5,6,7 is a horizontal line 
class Block:
    x = 0
    y = 0

    blocks = [
        [[1,5,9,13], [0,1,2,3]],
        [[1,2,5,9], [0,4,5,6], [1,5,9,10], [4,5,1,2]], 
        [[1,2,3,7], [4,5,6,8], [2,6,10,11], [0,4,5,6]],
        [[1,4,5,6], [1,5,9,6], [4,5,6,9], [1,5,6,9]],
        [[1,2,5,6]]
    ]
# randomize between shapes and colors - able to rotate the blocks 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.randint(1, len(colors) - 1)
        self.type = random.randint(0, len(self.blocks) - 1)
        self.rotation = 0
# gives the ability to turn the shapes in random positions and rotate the figures each time
    def image(self):
        return self.blocks[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.blocks[self.type])

# initializing "Tetris"
class Tetris:
    SCORE = 0
    state = "begin"
    height = 0
    width = 0
    x = 100
    y = 60
    #     data field to store the data and methods for defining behaviors 
    field = []
    zoom = 19
    block = None
    level = 2

# calls and creates a framework (height x width)
# new lines within the frame of the game 
    def __init__(self, height, width):
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

# creates and puts the NEW BLOCK at the new position (coordinates 3,0)
    def new_block(self):
        self.block = Block(3, 0)

# checks to see if it touches the top of board (TRUE = ends the game)
    def intersects(self):
        intersection = False
        # at 4(limit) because set the level at 3 (decide to change the level #)
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

# destroys blocks upon intersection (bottom block to top)
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

# similiar to "go_down", but moves the block entirely to bottom
    def go_space(self):
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

# allows to move the block down a unit 
    def go_down(self):
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

# runs once the block reaches the bottom floor 
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
        # new row formed 
        self.break_lines()
        # creates new blocks 
        self.new_block()
        # if any blocks go to the top and touch the top of the board, automatically ends the game with "GAMEOVER"
        if self.intersects():
            self.state = "GAMEOVER"

# allows to move the block either left or right 
    def go_totheside(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

# allows to rotate the block 90 degrees clockwise/counter-clockwise
# freely choose which direction you want to rotate 
    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation


# initializing pygame
pygame.init()

# background colors 
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = (400, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("TETRIS BY RILEY PARAN")

# updating board, checking status, check to see if key pressed 
# creating loop
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

press_down = False

# creates a new block if there is no moving block 
while not done:
    if game.block is None:
        game.new_block()
    counter += 1
    if counter > 100000:
        counter = 0
# moving block constantly with time until "s" key is pressed
    if counter % (fps // game.level // 2) == 0 or press_down:
        if game.state == "start":
            game.go_down()
# this checks to see which letter key is pressed and to run exactly for it's purpose
# referenced from videogame format 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.rotate()
            if event.key == pygame.K_a:
                game.go_totheside(-1)
            if event.key == pygame.K_d:
                game.go_totheside(1)
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                press_down = False
# background color 
    screen.fill(WHITE)

# updating the game board 
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

# updating the game board (new moving block)
    if game.block is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.block.image():
                    pygame.draw.rect(screen, colors[game.block.color],
                                     [game.x + game.zoom * (j + game.block.x) + 1,
                                      game.y + game.zoom * (i + game.block.y) + 1,
                                      game.zoom - 2, game.zoom - 2])
# settings for the letters in game 
    font = pygame.font.SysFont('TIMESNEWROMAN', 25, True, False)
    font1 = pygame.font.SysFont('TIMESNEWROMAN', 65, True, False)
    text = font.render("SCORE: " + str(game.score), True, BLACK)
    text_game_over = font1.render("GAME OVER", True, (255, 125, 0))
    text_game_over1 = font1.render("PRESS ESC", True, (255, 215, 0))
# when game finishes, GAMEOVER
    screen.blit(text, [0, 0])
    if game.state == "GAMEOVER":
        screen.blit(text_game_over, [10, 200])
        screen.blit(text_game_over1, [23, 265])

# runs at maximum FPS 
    pygame.display.flip()
    clock.tick(fps)
# deactivates pygame library 
pygame.quit()