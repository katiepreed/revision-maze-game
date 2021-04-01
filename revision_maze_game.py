import pygame
import time
import random
import csv
import math
from dijkstra import dijkstra
from merge import merge_sort
from enum import Enum
from pygame import mixer

# Icons made by Freepik www.flaticon.com
# https://www.freepik.com

# Music: https://www.bensound.com

# global variables
width = 1024  # of screen
height = 768  # of screen
FPS = 60  # frames per second
max_questions = 100  # maximum number of questions
# the higher the probability the more dispersed they will be
# the lower the number the higher the probability
# e.g 1/10 > 1/100
probability = 25  # probability of getting a 1 when generating a question
top_left = (302, 89)
width_line = 2
# the width and height of the maze
maze_width_and_height = 600


class ColourSchemes(Enum):
    BLACK_AND_WHITE = 0
    VIBRANT = 1
    MELLOW = 2
    RANDOM = 3


class Characters(Enum):
    PIXELS = 0
    BUTTERFLY = 1
    SAKURA = 2
    SNOW = 3
    PIRATE = 4
    MARIO = 5
    SEAL = 6
    SHARK = 7


def set_colour_scheme(new_scheme):
    global menu_colours

    # main, game_button, setting_button, leader_board, solution_button, hs_button, return_button, settings, sound_button, bg_button, character_button, background, sound, lb, levels_button, level, options, enemy, school, subject, continue

    if new_scheme == ColourSchemes.BLACK_AND_WHITE:
        menu_colours = (
            (0, 0, 0), (72, 72, 72), (94, 94, 94), (133, 133, 133), (128, 128, 128), (60, 60, 60), (34, 34, 34),
            (0, 0, 0),
            (87, 87, 87), (148, 148, 148), (87, 87, 87), (148, 148, 148), (188, 188, 188), (10, 10, 10),
            [(78, 78, 78), (100, 100, 100), (130, 130, 130), (50, 50, 50)], (0, 0, 0), (87, 87, 87), (148, 148, 148),
            (67, 67, 67), (0, 0, 0), (47, 47, 47), (56, 56, 56))
    elif new_scheme == ColourSchemes.VIBRANT:
        menu_colours = (
            (18, 207, 247), (217, 247, 18), (247, 147, 18), (185, 18, 247), (247, 18, 94), (72, 247, 18),
            (217, 247, 18),
            (185, 18, 247), (247, 147, 18), (17, 107, 255), (143, 207, 6), (18, 207, 247), (247, 147, 18),
            (185, 18, 247),
            [(217, 247, 18), (18, 207, 247), (247, 147, 18), (185, 18, 247)], (17, 255, 73), (17, 84, 255),
            (247, 147, 18),
            (185, 18, 247), (195, 247, 71), (129, 71, 247), (241, 56, 253))
    elif new_scheme == ColourSchemes.MELLOW:
        menu_colours = (
            (255, 221, 62), (155, 223, 82), (238, 122, 241), (91, 182, 248), (255, 221, 62), (182, 142, 255),
            (69, 98, 227), (240, 158, 242), (170, 224, 112), (136, 204, 253), (253, 213, 28), (123, 141, 244),
            (34, 190, 193), (255, 161, 37), [(255, 234, 89), (139, 207, 254), (242, 139, 255), (255, 180, 63)],
            (170, 224, 112), (182, 142, 255), (126, 220, 91), (248, 226, 31), (137, 207, 255), (255, 161, 37),
            (252, 218, 80))
    elif new_scheme == ColourSchemes.RANDOM:
        menu_colours = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                         (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                         (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                         (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))],
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


def set_character(character):
    global character_list

    if character == Characters.PIXELS:
        character_list = ["square_o.png", "square.png", "square_co.png", "square_s.png"]
    elif character == Characters.BUTTERFLY:
        character_list = ["butterfly.png", "spider.png", "spider_c.png", "spider_s.png"]
    elif character == Characters.SAKURA:
        character_list = ["geta.png", "sakura.png", "sakura_c.png", "sakura_s.png"]
    elif character == Characters.SNOW:
        character_list = ["snow.png", "sun.png", "sun_c.png", "sun_s.png"]
    elif character == Characters.PIRATE:
        character_list = ["galleon.png", "crossbone.png", "crossbone_c.png", "crossbone_s.png"]
    elif character == Characters.MARIO:
        character_list = ["mario.png", "mario1.png"]
    elif character == Characters.SEAL:
        character_list = ["seal.png", "fish.png"]
    elif character == Characters.SHARK:
        character_list = ["nemo.png", "shark.png", "shark_c.png", "shark_s.png"]


set_colour_scheme(ColourSchemes.MELLOW)
set_character(Characters.PIXELS)

# initalise Pygame
# first line helps stop the time lag
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Revision maze game")
clock = pygame.time.Clock()

# creating a font
# you create an object on which you call the render method
big_font = pygame.font.Font("fonts/circus.ttf", 100)
small_font = pygame.font.Font("fonts/circus.ttf", 55)
medium_small_font = pygame.font.Font("fonts/circus.ttf", 40)
very_small_font = pygame.font.Font("fonts/circus.ttf", 30)
new_font = pygame.font.Font("fonts/font.otf", 17)

# load the image
question_image = pygame.image.load("images/question (2).png")
question_correct_image = pygame.image.load("images/check.png")
question_wrong_image = pygame.image.load("images/close.png")


# first class functions
# passing functions as variables
class Maze:
    def __init__(self, x, y, width_cell, num_cols_and_rows, with_enemy, file):
        # data structures
        # arrays are fixed in size
        # all of these are lists
        self.grid_list = []  # contains all the top left coordinates of each square in the grid
        self.question_cells = []  # contains coordinates of all the questions
        # dictionary that contains all the possible locations the player can travel to
        # key: coordinate of current the current cell
        # values: coordinate of cells that you aren't behind a wall/ grid and are next to current cell
        # value: cells you can travel to
        # in path we're creating an edge (graphs)
        self.num_cols_and_rows = num_cols_and_rows
        self.path = {}
        self.file = file
        self.draw_grid(x, y, width_cell, self.num_cols_and_rows)
        self.make_maze(x, y, width_cell)  # call build the maze  function
        self.with_enemy = with_enemy

        if with_enemy:
            self.remove_dead_ends(width_cell)

    # making a grid made of individual cells by drawing white lines
    def draw_grid(self, x, y, w, num_cols_and_rows):
        # changing the colour of the screen
        screen.fill(menu_colours[0])

        # there are 20 rows
        for i in range(num_cols_and_rows):
            # I have to initialise x within this function because I change the x-coordinate in the for loop
            x = top_left[0]

            # there are 20 squares per row
            for j in range(num_cols_and_rows):
                # line(surface, color, start_pos, end_pos, width)
                # draw the top of each cell
                pygame.draw.line(screen, menu_colours[9], [x, y], [x + w, y], width_line)
                # draw the right side of each cell
                pygame.draw.line(screen, menu_colours[9], [x + w, y], [x + w, y + w], width_line)
                # draw the bottom of the cell
                pygame.draw.line(screen, menu_colours[9], [x + w, y + w], [x, y + w], width_line)
                # draw the left of the cell
                pygame.draw.line(screen, menu_colours[9], [x, y + w], [x, y], width_line)
                # add the coordinate of the left top corner of cell to the grid list
                self.grid_list.append((x, y))
                # add width of the cell to x coordinate to draw the new cell at the next coordinate
                x += w

            # add width of cell to y to draw the next row
            y += w

    def up(self, x, y, w, line):
        if line:
            # draw a rectangle twice the height of the current cell (2*w), making sure it doesn't overlap the lines (- width_line)
            # the new y-coordinate is above the current y-coordinate
            pygame.draw.rect(screen, menu_colours[6], (x + width_line, y, w - width_line, width_line), 0)
        else:
            pygame.draw.rect(screen, menu_colours[6],
                             (x + width_line, y - w + width_line, w - width_line, (2 * w) - width_line), 0)
            # to animate the wall being removed
            pygame.display.update()

        new_pos = (x, y - w)
        if new_pos not in self.path:
            # adding coordinates to dictionary to show that this path is available to travel
            self.path[new_pos] = [(x, y)]
        else:
            self.path[new_pos].append((x, y))

        # reverse connection
        self.path[(x, y)].append((x, y - w))

    def down(self, x, y, w, line):
        # new y-coordinate is bellow the current y-coordinate
        # draw rectangle twice as wide (2*w)
        if line:
            pygame.draw.rect(screen, menu_colours[6], (x + width_line, y + w, w - width_line, width_line), 0)
        else:
            pygame.draw.rect(screen, menu_colours[6],
                             (x + width_line, y + width_line, w - width_line, (2 * w) - width_line),
                             0)
        pygame.display.update()

        new_pos = (x, y + w)
        if new_pos not in self.path:
            # adding coordinates to dictionary to show that this path is available to travel
            self.path[new_pos] = [(x, y)]
        else:
            self.path[new_pos].append((x, y))

        # reverse connection
        self.path[(x, y)].append((x, y + w))

    def left(self, x, y, w, line):
        if line:
            pygame.draw.rect(screen, menu_colours[6], (x, y + width_line, width_line, w - width_line), 0)
        else:
            pygame.draw.rect(screen, menu_colours[6],
                             (x - w + width_line, y + width_line, (2 * w) - width_line, w - width_line), 0)

        pygame.display.update()

        new_pos = (x - w, y)
        if new_pos not in self.path:
            # adding coordinates to dictionary to show that this path is available to travel
            self.path[new_pos] = [(x, y)]
        else:
            self.path[new_pos].append((x, y))

        # reverse connection
        self.path[(x, y)].append((x - w, y))

    def right(self, x, y, w, line):
        if line:
            pygame.draw.rect(screen, menu_colours[6],
                             (x + + w, y + width_line, width_line, w - width_line), 0)
        else:
            pygame.draw.rect(screen, menu_colours[6],
                             (x + width_line, y + width_line, (2 * w) - width_line, w - width_line), 0)
        pygame.display.update()

        # path is a dictionary
        # key = new cell , value = current cell
        new_pos = (x + w, y)
        if new_pos not in self.path:
            self.path[new_pos] = [(x, y)]
        else:
            self.path[new_pos].append((x, y))
        # reverse connection
        # we are making it into an undirected graph: applies to all if loops
        # this relies on the fact that a key of the grid already exists
        # adding the next cell i will visit as a value to the key of the current cell
        self.path[(x, y)].append((x + w, y))

    def single_cell(self, x, y, w):
        # draw a single cell
        pygame.draw.rect(screen, menu_colours[5],
                         (x + width_line, y + width_line, w - (2 * width_line), w - (2 * width_line)),
                         0)
        pygame.display.update()

    def draw_question_cell(self, x, y, w, surface, image):
        # change the size
        image = pygame.transform.scale(image, (w - (width_line), w - (width_line)))
        # draw the picture to the screen
        surface.blit(image, (x + width_line, y + width_line))

    def backtracking_cell(self, x, y, w):
        # a little confused about what this does
        pygame.draw.rect(screen, menu_colours[6],
                         (x + width_line, y + width_line, w - (2 * width_line), w - (2 * width_line)),
                         0)
        pygame.display.update()  # has visited cell

    def make_maze(self, x, y, w):
        sec_1 = 0.1
        sec_2 = 0.05
        questions_list = Q_and_a(self.file)
        # initialise stack
        # contain coordinates of cells so that it can be popped when pygame gets stuck
        backtracking_stack = Coord_Stack()
        # drawing the starting position of maze
        self.single_cell(x, y, w)
        # add coordinates of starting cell into stack
        backtracking_stack.push([x, y])

        # add the coordinates of starting cell into visited list
        visited = [(x, y)]  # visited cells

        # I'm creating an entry for the first cell
        # key = starting cell
        # value = []
        self.path[(x, y)] = []

        # while the stack is not empty (there are cells that haven't been visited)
        while (backtracking_stack.size()) > 0:
            # slow program now a bit
            time.sleep(float(sec_1))
            cell = []  # cell list
            # using if loop to see which cells (up, down, left, or right) next to current cell are available
            # they are available if they are not in th visited list and if they are in the grid list

            # right cell available?
            if (x + w, y) not in visited and (x + w, y) in self.grid_list:
                cell.append("right")  # if yes add to cell list

            # left cell available?
            if (x - w, y) not in visited and (x - w, y) in self.grid_list:
                cell.append("left")

            # down cell available?
            if (x, y + w) not in visited and (x, y + w) in self.grid_list:
                cell.append("down")

            # up cell available?
            if (x, y - w) not in visited and (x, y - w) in self.grid_list:
                cell.append("up")

            # if the cell list isn't empty (meaning there are available cells next to current cell)
            if len(cell) > 0:
                # select one of the available cell randomly
                cell_chosen = random.choice(cell)

                if cell_chosen == "right":
                    # if right cell was chosen draw a rectangle twice the size of current cell to the right
                    self.right(x, y, w, False)

                    # make this cell the current cell by incrementing the x-value
                    x += w
                    # add to visited list
                    visited.append((x, y))
                    # place current cell on to stack
                    backtracking_stack.push([x, y])

                elif cell_chosen == "left":
                    # draw cell to the left
                    self.left(x, y, w, False)

                    x = x - w
                    visited.append((x, y))
                    backtracking_stack.push([x, y])

                elif cell_chosen == "down":
                    self.down(x, y, w, False)

                    y = y + w
                    visited.append((x, y))
                    backtracking_stack.push([x, y])

                elif cell_chosen == "up":
                    self.up(x, y, w, False)

                    y = y - w
                    visited.append((x, y))
                    backtracking_stack.push([x, y])

            else:
                # if no cells are available pop one from the stack
                # and make the x and y coordinates equal to the previous coordinate i think
                coordinate = backtracking_stack.pop()
                x = coordinate[0]
                y = coordinate[1]
                # use single_cell function to show backtracking image
                # first single cell colours the current cell a different colour
                # then the backtracking cell colours the current cell to the same colour as all the other cells
                self.single_cell(x, y, w)
                # slow program down a bit
                time.sleep(float(sec_2))
                # change colour to identify backtracking path
                self.backtracking_cell(x, y, w)

            skip_button = Button(pygame.Rect(800, 20, 100, 40), " SKIP", menu_colours[9], 0)
            skip_button.draw(very_small_font)

            # every time a player presses a button in the game, it is an event
            for event in pygame.event.get():
                # every time you click down it is a mousebuttondown event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checking the collisions
                    if skip_button.rectangle.collidepoint(event.pos):
                        sec_1 = 0
                        sec_2 = 0

        # to cover the skip button
        pygame.draw.rect(screen, menu_colours[0], (800, 20, 100, 50), 0)

        # make the maze the maze first and then have a loop that goes through a set number of times: q through grid_list
        # choose a random coordinate in grid_list
        # check there isn't a question already on it
        # add the question on to it.

        q = 0
        temporary_list = []
        while q != (self.num_cols_and_rows // 3) * 2:
            coord = random.choice(self.grid_list)
            if questions_list.empty():
                break
            elif coord not in temporary_list and coord != top_left:
                self.question_cells.append([coord, questions_list.dequeue()])
                temporary_list.append(coord)
                q += 1

        # create a question list that holds x and y coordinates of the question squares
        # if random number == 1 , then append to question list the coordinates of that cell
        # iterate through tha list to call question_cell to draw the question rectangle.
        for i in range(len(self.question_cells)):
            self.draw_question_cell(self.question_cells[i][0][0], self.question_cells[i][0][1], w, screen,
                                    question_image)

    def find_dead_ends(self, node, dead_ends, visited):
        # node is one item in a graph: cell
        visited.append(node)

        # list of connected nodes
        connected_nodes = self.path[node]

        # it is a dead end if only one cell connects to it
        if len(connected_nodes) == 1:
            dead_ends.append(node)

        # for each item in connected nodes list
        for other_node in connected_nodes:
            if not other_node in visited:
                # recursion
                self.find_dead_ends(other_node, dead_ends, visited)

    def remove_dead_ends(self, w):
        dead_ends = []
        visited = []
        self.find_dead_ends(top_left, dead_ends, visited)

        # list of the coordinates of the question
        q_coords = []
        for question in self.question_cells:
            q_coords.append(question[0])

        for node in dead_ends:
            x = node[0]
            y = node[1]

            # research functional programming

            neighbouring_unconnected_cells = []

            # right cell available?
            if (x + w, y) in self.path and (x + w, y) not in self.path[node]:
                neighbouring_unconnected_cells.append("right")  # if yes add to cell list

            # left cell available?
            if (x - w, y) in self.path and (x - w, y) not in self.path[node]:
                neighbouring_unconnected_cells.append("left")

            # down cell available?
            if (x, y + w) in self.path and (x, y + w) not in self.path[node]:
                neighbouring_unconnected_cells.append("down")

            # up cell available?
            if (x, y - w) in self.path and (x, y - w) not in self.path[node]:
                neighbouring_unconnected_cells.append("up")

            chosen = random.choice(neighbouring_unconnected_cells)

            if chosen == "right":
                self.right(x, y, w, True)
            elif chosen == "left":
                self.left(x, y, w, True)
            elif chosen == "up":
                self.up(x, y, w, True)
            elif chosen == "down":
                self.down(x, y, w, True)


# class for buttons
class Button:
    def __init__(self, rectangle, text, fill_colour, width_of_border):
        self.rectangle = rectangle
        self.text = text
        self.fill_colour = fill_colour
        self.width_of_border = width_of_border

    def draw(self, font):
        # drawing the rectangle with the colour and information given in the parameters of the object
        pygame.draw.rect(screen, self.fill_colour, self.rectangle, self.width_of_border)
        # drawing the text on top
        # what is self.rectangle.x
        # how does it know what part of rectangle is the x-coordinate
        draw_text(self.text, font, (self.rectangle.x, self.rectangle.y), (255, 255, 255))

    def draw_pic(self, pic, width, height, font, x, y, colour):
        # drawing the rectangle with the colour and information given in the parameters of the object
        pygame.draw.rect(screen, self.fill_colour, self.rectangle, self.width_of_border)
        draw_text(self.text, font, (self.rectangle.x, self.rectangle.y), colour)

        # drawing the picture on top
        # load the image
        picture = pygame.image.load("images/" + pic)
        # change the size
        picture = pygame.transform.scale(picture, (width, height))
        # draw the picture to the screen
        screen.blit(picture, (x, y))

    def draw_separate(self, font):
        # drawing the rectangle with the colour and information given in the parameters of the object
        pygame.draw.rect(screen, self.fill_colour, self.rectangle, self.width_of_border)

        rect_coord = (self.rectangle.x, self.rectangle.y)
        rect_width = self.rectangle.w

        # split the question into a list of words separated by spaces
        words = self.text.split(" ")
        # size() determines the amount of space needed to render text
        # it returns the dimensions needed to render the text (width, height)
        # so space = the the first item of (width, height), which = the width of the space
        space = font.size(' ')[0]

        # assign x and y to the relevant numbers in pos
        x, y = rect_coord

        # for each word in the word list
        for word in words:
            # displaying text
            # this creates a new surface with text drawn already onto it
            # the True part is called aliasing
            # If true, the characters will have smooth edges
            text_surface = font.render(word, True, (255, 255, 255))
            # get the width and the height of each letter in the list
            word_width, word_height = text_surface.get_size()
            # if the x-coordinate of word + width of word is >= the coordinate of the right corner of question box then ...
            if x + word_width >= (rect_width + rect_coord[0]):
                # Reset the x to the value of the coordinate of the left corner of rectangle
                x = rect_coord[0]
                # Start on new row by adding 42 to the y-coordinate
                y += 32
            # draw the letter to the screen
            screen.blit(text_surface, (x, y))
            # increase the x-coordinate by the width of the letter + space
            x += word_width + space

    # I  would love to make a border on buttons when mouse hovers over it
    def draw_border(self):
        pass


# player class
class Player:
    def __init__(self, maze, x, y, w, with_enemy, screenshot, enemy_list, file, username):
        # attributes
        self.x = x
        self.y = y
        self.w = w
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.movement_timer = 0
        self.answering_question = False
        self.current_question_button = None
        self.current_question = None
        self.answers = []
        self.maze = maze
        self.points = 0
        self.with_enemy = with_enemy
        self.screenshot = screenshot
        self.enemy_list = enemy_list
        self.answered_q = []
        self.file = file
        self.username = username

    def update(self, level, click, with_enemy):
        # timer makes sure that once the player has pressed a key they can only move again after 10 frames
        # for each frame it will remove 1 from movement_timer
        # self.check_for_question()

        if self.answering_question:
            # check answer here
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                # if you press on one of the answers then it returns the game
                i = 0
                for button in self.answers:
                    if button.rectangle.collidepoint((mx, my)):
                        if self.current_question.correct_answer == i:
                            sound_effect("yay.wav")
                            self.points += 1
                            new_image = question_correct_image
                        else:
                            sound_effect("wrong.wav")
                            new_image = question_wrong_image

                        # drawing the new question picture onto the screen
                        self.answering_question = False
                        self.maze.draw_question_cell(self.x, self.y, self.w, self.screenshot, new_image)

                        # taking all the answered questions and putting them into a list
                        q = self.maze.question_cells[self.current_question_cell_index]
                        self.answered_q.append(q)

                        del self.maze.question_cells[self.current_question_cell_index]
                        if len(self.maze.question_cells) == 0 and self.with_enemy == True:
                            sound_effect("game_complete.wav")

                            # adding points to file
                            file = open("files/scores.csv", "a")
                            # Append text (username + level + score (at some point)) at the end of file
                            file.write(
                                "\n" + self.username + "," + str(int(self.points)) + "," + str(level) + "," + str(
                                    with_enemy))
                            file.close()
                            # run main
                            main(self.username)

                    i += 1

        self.movement_timer -= 1

        if self.movement_timer <= 0 and not self.answering_question and click % 2 != 0:
            moved = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                new_pos = (self.x - self.w, self.y)
                # if the new position in the possible exists for the current cell, then we will do the movement
                # think about way to make this more efficient
                if new_pos in self.maze.path[(self.x, self.y)]:
                    self.x -= self.w
                    self.left = True
                    self.right = False
                    moved = True

            elif keys[pygame.K_RIGHT]:
                new_pos = (self.x + self.w, self.y)
                if new_pos in self.maze.path[(self.x, self.y)]:
                    self.x += self.w
                    self.right = True
                    self.left = False
                    moved = True

            elif keys[pygame.K_UP]:
                new_pos = (self.x, self.y - self.w)
                if new_pos in self.maze.path[(self.x, self.y)]:
                    self.y -= self.w
                    self.up = True
                    self.down = False
                    moved = True

            elif keys[pygame.K_DOWN]:
                new_pos = (self.x, self.y + self.w)
                if new_pos in self.maze.path[(self.x, self.y)]:
                    self.y += self.w
                    self.up = False
                    self.down = True
                    moved = True

            if moved:
                self.movement_timer = 10
                self.check_for_question()
                if not self.with_enemy:
                    if new_pos == top_left:
                        sound_effect("game_complete.wav")
                        # adding points to file
                        file = open("files/scores.csv", "a")
                        # Append text (username + level + score (at some point)) at the end of file
                        file.write("\n" + self.username + "," + str(int(self.points)) + "," + str(level) + "," + str(
                            with_enemy))
                        file.close()
                        # run main
                        main(self.username)

    def check_for_question(self):
        x = top_left[0]
        y = top_left[1]

        for i in range(len(self.maze.question_cells)):
            question_cell = self.maze.question_cells[i]
            if (self.x, self.y) == question_cell[0]:
                self.answering_question = True
                self.current_question_cell_index = i
                # question_cell[1].question : we are accessing the question attribute from the object
                self.current_question_button = Button(pygame.Rect(x + 12, y + 12, 575, 150), question_cell[1].question,
                                                      menu_colours[13], 0)
                # the whole current question
                self.current_question = question_cell[1]
                # creates an answer list that refreshes for every question
                self.answers = []
                # i is index of each answer
                # question_cells is a list where:
                # question_cell[0] = coordinate
                # question_cell[1] = question object: Question(question, answers, correct answer = )
                # question_cell[1] = Question(column[0], column[1:5], int(column[5])) where column = line in file
                for y_coord in range(4):
                    self.answers.append(Button(pygame.Rect(x + 12, (y + 82) + (y_coord + 1) * 100, 575, 75),
                                               question_cell[1].answers[y_coord], menu_colours[8], 0))

    def check_for_enemy(self):
        for enemy in self.enemy_list:
            if (self.x, self.y) == (enemy.x, enemy.y):
                sound_effect("game_over.wav")

                self.answered_q += self.maze.question_cells
                self.maze.question_cells = []

                for question in self.answered_q:
                    self.maze.question_cells.append([question[0], question[1]])

                for i in range(len(self.maze.question_cells)):
                    self.maze.draw_question_cell(self.maze.question_cells[i][0][0], self.maze.question_cells[i][0][1],
                                                 self.w, self.screenshot, question_image)

                self.points = 0
                self.answered_q = []

                return True

    # method to draw movement
    def draw(self, solution):

        draw_text("Points: " + str(int(self.points)), small_font, (55, 205), (255, 255, 255))

        # character
        playerIMG = pygame.image.load("images/" + character_list[0])
        # change the size
        playerIMG = pygame.transform.scale(playerIMG, (self.w - width_line, self.w - width_line))
        # draw the picture
        screen.blit(playerIMG, (self.x + width_line, self.y + width_line))

        # drawing solution
        if solution == True:
            path = dijkstra(self.maze.path, (self.x, self.y), top_left)
            for node in path:
                pygame.draw.circle(screen, (240, 107, 204), (node[0] + (self.w // 2), node[1] + (self.w // 2)), 5)

        if self.answering_question:
            # drawing white background to question
            pygame.draw.rect(screen, (255, 255, 255),
                             (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 0)
            # drawing the question button
            self.current_question_button.draw_separate(medium_small_font)
            # drawing the answer buttons
            for button in self.answers:
                button.draw_separate(very_small_font)


class EnemyMovementMode(Enum):
    RANDOM = 0
    CHASE = 1
    SCATTER = 2


# the enemy class contains the different behaviour  that the enemies have in pacman
# there are three distinct modes an enemy can be in: chase, scatter, random
class Enemy:
    def __init__(self, maze, player, x, y, w):
        # attributes
        self.x = x
        self.y = y
        self.w = w
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.movement_timer = 0
        self.mode_timer = 0
        self.last_pos = (x, y)
        self.maze = maze
        self.player = player
        self.mode = EnemyMovementMode.RANDOM
        self.num_enemies = 0
        # corners = top left, top right, bottom left, bottom right
        self.corners = [(top_left[0], top_left[1] - 50), (top_left[0] + 610, top_left[1] - 50),
                        (top_left[0], top_left[1] + 610), (top_left[0] + 610, top_left[1] + 610)]
        self.scatter_coord = random.choice(self.corners)
        self.pic = character_list[1]

    def update(self, click, help_click):
        self.movement_timer -= 1
        if self.movement_timer <= 0 and not self.player.answering_question and click % 2 != 0 and help_click % 2 != 0:
            # making a list of all possible valid exits
            exits = []
            current_cell = self.maze.path[(self.x, self.y)]
            for new_pos in ((self.x - self.w, self.y), (self.x + self.w, self.y), (self.x, self.y - self.w),
                            (self.x, self.y + self.w)):
                if new_pos in current_cell:
                    exits.append(new_pos)
            if self.last_pos in exits:
                exits.remove(self.last_pos)

            if self.mode == EnemyMovementMode.CHASE and len(self.maze.question_cells) > 1:
                self.mode = EnemyMovementMode.RANDOM

            # I could have use dijkstra's algorithm but decided not to
            if self.mode == EnemyMovementMode.RANDOM:
                # chooses a random exit
                chosen_exit = random.choice(exits)
                self.pic = character_list[1]
            else:
                if self.mode == EnemyMovementMode.CHASE:
                    target = (self.player.x, self.player.y)
                    self.pic = character_list[2]
                elif self.mode == EnemyMovementMode.SCATTER:
                    target = self.scatter_coord
                    self.pic = character_list[3]

                closest_distance = 9999
                for exit in exits:
                    distance = math.hypot(target[0] - exit[0], target[1] - exit[1])
                    if distance < closest_distance:
                        closest_distance = distance
                        chosen_exit = exit

            self.last_pos = (self.x, self.y)
            # assign two variables in one line
            self.x, self.y = chosen_exit[0], chosen_exit[1]

            if self.mode == EnemyMovementMode.RANDOM:
                self.movement_timer = 60
            elif self.mode == EnemyMovementMode.SCATTER:
                self.movement_timer = 20
            elif self.mode == EnemyMovementMode.CHASE:
                self.movement_timer = 60

    def draw(self, w):
        if not self.player.answering_question:
            enemyIMG = pygame.image.load("images/" + self.pic)
            # change the size
            enemyIMG = pygame.transform.scale(enemyIMG, (w - width_line, w - width_line))
            # draw the picture
            screen.blit(enemyIMG, (self.x + width_line, self.y + width_line))

    def pick_mode(self):
        if len(self.maze.question_cells) == 1:
            self.mode = EnemyMovementMode.CHASE
        else:
            if self.mode == EnemyMovementMode.RANDOM and random.randint(0, 1000) == 0:
                self.mode = EnemyMovementMode.SCATTER
            elif self.mode == EnemyMovementMode.SCATTER and random.randint(0, 800) == 0:
                self.mode = EnemyMovementMode.RANDOM
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    def check_mode(self):
        if self.mode == EnemyMovementMode.RANDOM:
            return "random"
        elif self.mode == EnemyMovementMode.SCATTER:
            return "scatter"
        elif self.mode == EnemyMovementMode.CHASE:
            return "chase"


# class for the coordinates
# for functions use stack terminology
# using a class to represent an abstract data type: stack
# you need to write the algorithm for each of the functions within this class
# algorithm: initialise object, call method for specific thing you want to do, go through what method does
# in design section include a diagram and explain what a graph is and why you are using it.
class Coord_Stack:
    def __init__(self):
        self.items = []

    # adds an element on the top of the stack
    def push(self, item):
        self.items.append(item)

    # removes an element from the top of the stack and returns it
    def pop(self):
        return self.items.pop()

    # returns the element of the top of the stack without removing it
    def peek(self):
        return self.items[len(self.items) - 1]

    # returns the size of the stack
    def size(self):
        return len(self.items)


class Q_and_a:
    def __init__(self, file_name):
        self.file_name = file_name
        self.question_list = []
        # with open means it will automatically close
        with open("files/"+file_name) as file:
            reader = csv.reader(file)
            # it will read each line in the file and put it into a list in reader
            for column in reader:
                question = Question(column[0], column[1:5], int(column[5]))
                self.question_list.append(question)
            # shuffles the list
            #  question_list will be used as a queue
            random.shuffle(self.question_list)

    def empty(self):
        # if empty it will return True
        return len(self.question_list) == 0

    def dequeue(self):
        # removes and returns the first item
        return self.question_list.pop(0)


class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer


# drawing characters and background function
def redraw_game_window(screenshot, player, enemy_list, w, with_enemy, solution, click, level, help_click):
    x = top_left[0]
    y = top_left[1]

    # loading the background
    screen.blit(screenshot, (0, 0))

    if not with_enemy:
        # exit image
        exit = pygame.image.load("images/exit.png")
        # change the size
        exit = pygame.transform.scale(exit, (w - (3 * width_line), w - (3 * width_line)))
        # draw the picture to the screen to the left corner, where the exit will always be
        screen.blit(exit, (x + width_line, y + width_line))

    # an instance (man) is using the method draw within a redrawGameWindow function to draw the movement of the character
    player.draw(solution)

    for enemy in enemy_list:
        enemy.draw(w)

    if click % 2 == 0:
        high_score(level, with_enemy)

    if help_click % 2 == 0:
        help(with_enemy)

    pygame.display.update()


# drawing text
def draw_text(text, font, rect_coord, colour):
    space = font.size(" ")[0]

    x, y = rect_coord
    words = text.split(" ")
    for word in words:
        # displaying text
        # this creates a new surface with text drawn already onto it
        # the True part is called aliasing, if true, the characters will have smooth edges
        text_surface = font.render(word, True, (colour))
        word_width, word_height = text_surface.get_size()
        # draw letter to the screen
        screen.blit(text_surface, (x, y))
        x += word_width + space


def main(username):
    running = True
    while running:

        screen.fill(menu_colours[0])

        # return button
        return_button = Button(pygame.Rect(23, 22, 160, 75), " Logout", (220, 40, 34), 0)
        return_button.draw(small_font)

        # drawing main menu
        # last two values are the x, y coordinates
        draw_text("main menu", big_font, (320, 100), (255, 255, 255))

        # buttons
        # first two numbers are the coordinates (left, top, width, height)
        game_button = Button(pygame.Rect(256, 250, 502, 108), "     Game", menu_colours[1], 0)
        settings_button = Button(pygame.Rect(256, 410, 502, 108), "   settings", menu_colours[2], 0)
        leader_board_button = Button(pygame.Rect(256, 570, 502, 108), " Leader board", menu_colours[3], 0)

        game_button.draw(big_font)
        settings_button.draw(big_font)
        leader_board_button.draw(big_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")

                # checking the collisions
                if game_button.rectangle.collidepoint(event.pos):
                    options(username)
                elif settings_button.rectangle.collidepoint(event.pos):
                    settings()
                elif leader_board_button.rectangle.collidepoint(event.pos):
                    leader_board()
                elif return_button.rectangle.collidepoint(event.pos):
                    login()

        # update the display window each loop
        pygame.display.update()
        # clock.tick(69)


def game(width_cell, num_cols_and_rows, level, with_enemy, file, username):
    x = top_left[0]
    y = top_left[1]
    solution = False
    click = 1
    help_click = 1

    # calling the main functions
    # 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell, 4th value = number of columns and rows
    maze = Maze(x, y, width_cell, num_cols_and_rows, with_enemy, file)

    # initialising objects from the button class
    # first two numbers are the coordinates (left, top, width, height)
    hs_button = Button(pygame.Rect(50, 480, 160, 70), "  High scores", menu_colours[5], 0)
    solution_button = Button(pygame.Rect(50, 610, 160, 70), "   Solution", menu_colours[8], 0)
    help_button = Button(pygame.Rect(50, 350, 160, 65), "     HELP", (212, 50, 50), 0)
    return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)

    if not with_enemy:
        solution_button.draw(very_small_font)

    # calling the drawing method from the button class
    hs_button.draw(very_small_font)
    help_button.draw(very_small_font)
    return_button.draw(small_font)

    # taking a screenshot
    # has to be after the creation of the maze
    screenshot = screen.copy()

    # make a list of enemies and characters
    enemy_list = []

    # creating an instance of the player class
    # make sure to change the width and height for picture of character
    # (x,y,width,height)
    # x,y coordinates are where the picture is drawn
    player = Player(maze, x + (num_cols_and_rows - 1) * width_cell, y + (num_cols_and_rows - 1) * width_cell,
                    width_cell, with_enemy, screenshot, enemy_list, file, username)
    if with_enemy:
        for i in range(level + 3):
            # the x and y coordinates are in the centre of the maze
            enemy_list.append(Enemy(maze, player, x + (int(num_cols_and_rows / 2) * width_cell),
                                    y + (int(num_cols_and_rows / 2) * width_cell), width_cell))

    running = True
    while running:

        # to change modes
        if with_enemy:
            mode = enemy_list[0].pick_mode()

            for i in range(len(enemy_list) - 1):
                enemy_list[i + 1].set_mode(mode)

        # keep running at the at the right speed
        # slows down player movement
        clock.tick(FPS)

        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checking the collisions
                if return_button.rectangle.collidepoint(event.pos):
                    sound_effect("click.wav")
                    main(username)
                elif solution_button.rectangle.collidepoint(event.pos) and not with_enemy:
                    sound_effect("click.wav")
                    solution = True
                elif hs_button.rectangle.collidepoint(event.pos):
                    sound_effect("click.wav")
                    click += 1
                elif help_button.rectangle.collidepoint(event.pos):
                    sound_effect("click.wav")
                    help_click += 1

        # update the display window each loop
        pygame.display.update()

        # calling the update method in the player class on the object man
        player.update(level, click, with_enemy)

        # for enemy restart
        if player.check_for_enemy():
            for enemy in enemy_list:
                enemy.x = x + (int(num_cols_and_rows / 2) * width_cell)
                enemy.y = y + (int(num_cols_and_rows / 2) * width_cell)

        for enemy in enemy_list:
            enemy.update(click, help_click)

        # redraw_game_window(screenshot, player, enemy)
        redraw_game_window(screenshot, player, enemy_list, width_cell, with_enemy, solution, click, level, help_click)


def settings():
    running = True
    while running:
        screen.fill(menu_colours[7])

        # drawing main menu
        # last two values are the x, y coordinates
        draw_text("Settings", big_font, (350, 100), (255, 255, 255))

        # initialising objects from the button class
        # first two numbers are the coordinates (left, top, width, height)
        sound_button = Button(pygame.Rect(256, 240, 502, 118), "     Music", menu_colours[8], 0)
        bg_button = Button(pygame.Rect(256, 390, 502, 118), "  Background", menu_colours[9], 0)
        character_button = Button(pygame.Rect(256, 540, 502, 118), "  Character", menu_colours[10], 0)
        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)

        # calling the drawing method from the button class
        sound_button.draw(big_font)
        bg_button.draw(big_font)
        character_button.draw(big_font)
        return_button.draw(small_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")

                # checking the collisions
                if sound_button.rectangle.collidepoint(event.pos):
                    sound()
                elif bg_button.rectangle.collidepoint(event.pos):
                    background()
                elif return_button.rectangle.collidepoint(event.pos):
                    running = False
                elif character_button.rectangle.collidepoint(event.pos):
                    character()

        # update the display window each loop
        pygame.display.update()


def background():
    running = True
    while running:
        colour = menu_colours[11]
        colour2 = menu_colours[1]
        screen.fill(colour)

        # drawing main menu
        # last two values are the x, y coordinates
        draw_text("Background", big_font, (325, 50), (255, 255, 255))

        pygame.draw.rect(screen, (255, 255, 255), (170, 200, 700, 500), 3)

        # initialising objects from the button class
        # first two numbers are the coordinates (left, top, width, height)
        black_and_white = Button(pygame.Rect(260, 265, 220, 170), " Black and White", colour2, 3)
        mellow = Button(pygame.Rect(260, 486, 220, 170), " Mellow", colour2, 3)
        vibrant = Button(pygame.Rect(556, 265, 220, 170), " Vibrant", colour2, 3)
        random = Button(pygame.Rect(556, 486, 220, 170), " Random", colour2, 3)
        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)

        # calling the drawing method from the button class
        black_and_white.draw_pic("bw.png", 80, 80, very_small_font, 330, 330, (0, 0, 0))
        mellow.draw_pic("mellow.png", 80, 80, small_font, 330, 554, (0, 0, 0))
        vibrant.draw_pic("vibrant.png", 80, 80, small_font, 624, 330, (0, 0, 0))
        random.draw_pic("random.png", 80, 80, small_font, 624, 554, (0, 0, 0))
        return_button.draw(small_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")
                if return_button.rectangle.collidepoint(event.pos):
                    running = False
                elif black_and_white.rectangle.collidepoint(event.pos):
                    set_colour_scheme(ColourSchemes.BLACK_AND_WHITE)
                elif mellow.rectangle.collidepoint(event.pos):
                    set_colour_scheme(ColourSchemes.MELLOW)
                elif vibrant.rectangle.collidepoint(event.pos):
                    set_colour_scheme(ColourSchemes.VIBRANT)
                elif random.rectangle.collidepoint(event.pos):
                    set_colour_scheme(ColourSchemes.RANDOM)

        # update the display window each loop
        pygame.display.update()


def sound():
    on = "on.png"
    off = "off.png"
    pic_p = off
    pic_h = off
    pic_d = off
    pic_i = off

    running = True
    while running:
        colour = menu_colours[12]
        colour2 = menu_colours[1]
        screen.fill(colour)

        # everytime the mouse is presses down, its coordinates are stored in mx and my
        mx, my = pygame.mouse.get_pos()

        # drawing main menu
        # last two values are the x, y coordinates
        draw_text("Music", big_font, (400, 50), (255, 255, 255))

        pygame.draw.rect(screen, (255, 255, 255), (170, 200, 700, 500), 3)
        # initialising objects from the button class
        # first two numbers are the coordinates (left, top, width, height)
        peaceful = Button(pygame.Rect(260, 265, 220, 170), " Peaceful", colour2, 3)
        happy = Button(pygame.Rect(260, 486, 220, 170), " Happy", colour2, 3)
        dramatic = Button(pygame.Rect(556, 265, 220, 170), " Dramatic", colour2, 3)
        inspiring = Button(pygame.Rect(556, 486, 220, 170), " Inspiring", colour2, 3)
        no = Button(pygame.Rect(750, 50, 200, 40), "    NO MUSIC", (0, 0, 0), 0)
        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)

        # calling the drawing method from the button class
        peaceful.draw_pic(pic_p, 100, 100, small_font, 310, 330, (0, 0, 0))
        happy.draw_pic(pic_h, 100, 100, small_font, 310, 554, (0, 0, 0))
        dramatic.draw_pic(pic_d, 100, 100, small_font, 604, 330, (0, 0, 0))
        inspiring.draw_pic(pic_i, 100, 100, small_font, 604, 554, (0, 0, 0))
        no.draw(very_small_font)
        return_button.draw(small_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")

                # checking the collisions
                if return_button.rectangle.collidepoint(event.pos):
                    running = False
                elif peaceful.rectangle.collidepoint(event.pos):
                    pic_p = on
                    pic_h = off
                    pic_d = off
                    pic_i = off
                    # background music
                    mixer.music.load("sound/peaceful.wav")
                    # the background music will play on a loop
                    mixer.music.play(-1)
                elif happy.rectangle.collidepoint(event.pos):
                    pic_p = off
                    pic_h = on
                    pic_d = off
                    pic_i = off
                    # background music
                    mixer.music.load("sound/happy.wav")
                    # the background music will play on a loop
                    mixer.music.play(-1)
                elif dramatic.rectangle.collidepoint(event.pos):
                    pic_p = off
                    pic_h = off
                    pic_d = on
                    pic_i = off
                    # background music
                    mixer.music.load("sound/dramatic.wav")
                    # the background music will play on a loop
                    mixer.music.play(-1)
                elif inspiring.rectangle.collidepoint((mx, my)):
                    pic_p = off
                    pic_h = off
                    pic_d = off
                    pic_i = on
                    # background music
                    mixer.music.load("sound/inspiring.wav")
                    # the background music will play on a loop
                    mixer.music.play(-1)
                elif no.rectangle.collidepoint((mx, my)):
                    pygame.mixer.music.stop()
                    pic_p = off
                    pic_h = off
                    pic_d = off
                    pic_i = off

        # update the display window each loop
        pygame.display.update()


def character():
    running = True
    while running:
        colour = menu_colours[21]
        colour2 = menu_colours[1]
        screen.fill(colour)

        # drawing main menu
        # last two values are the x, y coordinates
        draw_text("Character", big_font, (325, 50), (255, 255, 255))

        pygame.draw.rect(screen, (255, 255, 255), (170, 200, 700, 500), 3)

        # initialising objects from the button class
        # first two numbers are the coordinates (left, top, width, height)
        pixels = Button(pygame.Rect(224, 265, 150, 150), "    Original", colour2, 3)
        butterfly = Button(pygame.Rect(648, 265, 150, 150), "  Butterfly", colour2, 3)
        snow = Button(pygame.Rect(436, 265, 150, 150), "     Snow", colour2, 3)
        sakura = Button(pygame.Rect(224, 486, 150, 150), "     Sakura", colour2, 3)
        pirate = Button(pygame.Rect(436, 486, 150, 150), "    Pirate", colour2, 3)
        seal = Button(pygame.Rect(648, 486, 150, 150), "  Clownfish", colour2, 3)
        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)

        # calling the drawing method from the button class
        pixels.draw_pic("square_o.png", 60, 60, very_small_font, 275, 310, (0, 0, 0))
        butterfly.draw_pic("butterfly.png", 60, 60, very_small_font, 699, 310, (0, 0, 0))
        snow.draw_pic("snow.png", 60, 60, very_small_font, 487, 310, (0, 0, 0))
        sakura.draw_pic("geta.png", 60, 60, very_small_font, 275, 544, (0, 0, 0))
        pirate.draw_pic("galleon.png", 60, 60, very_small_font, 487, 554, (0, 0, 0))
        seal.draw_pic("nemo.png", 60, 60, very_small_font, 699, 554, (0, 0, 0))
        return_button.draw(small_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")
                if return_button.rectangle.collidepoint(event.pos):
                    running = False
                elif pixels.rectangle.collidepoint(event.pos):
                    set_character(Characters.PIXELS)
                elif butterfly.rectangle.collidepoint(event.pos):
                    set_character(Characters.BUTTERFLY)
                elif snow.rectangle.collidepoint(event.pos):
                    set_character(Characters.SNOW)
                elif sakura.rectangle.collidepoint(event.pos):
                    set_character(Characters.SAKURA)
                elif pirate.rectangle.collidepoint(event.pos):
                    set_character(Characters.PIRATE)
                elif seal.rectangle.collidepoint(event.pos):
                    set_character(Characters.SHARK)

        # update the display window each loop
        pygame.display.update()


def sound_effect(music):
    sound_effect = mixer.Sound("sound/"+music)
    sound_effect.play()


def format():
    with open("files/scores.csv") as file:
        reader = csv.reader(file)
        # it will read each line in the file and put it into a list in reader
        list_user = []

        for column in reader:
            # removing unnecessary brackets etc
            user = str(column)
            user = user.replace('[', '')
            user = user.replace(']', '')
            user = user.replace("'", "")

            # splitting the column into a list of info
            user = user.split(",")
            list_user.append(user)

    file.close()
    return list_user


def high_score(level, with_enemy):
    # get a list of users
    sorted_user = format()
    # list of player scores from that level
    level_user = []

    for user in sorted_user:
        if str(user[2]).split() == str(level).split() and str(user[3]).split() == str(with_enemy).split():
            level_user.append(user)

    pygame.draw.rect(screen, menu_colours[17],
                     (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 0)
    pygame.draw.rect(screen, (0, 0, 0),
                     (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 3)

    # formatting
    header_text = " "
    header_text += "%-9s" % "Rank"
    header_text += "%-12s" % "Player"
    header_text += "%-64s" % "Points"

    draw_text(header_text, small_font, (320, 110), (0, 0, 0))

    # the y-coordinate
    count = 200
    # count of names
    name_count = 1

    level_user = merge_sort(level_user)

    for i in level_user:
        # this if statement shows how many names appear on the screen: 10
        if name_count < 11:

            # drawing the text to the surface
            rank = small_font.render(str(name_count), True, (255, 255, 255))
            user = small_font.render(i[0], True, (255, 255, 255))
            points = small_font.render(i[1], True, (255, 255, 255))

            screen.blit(rank, (350, count))
            screen.blit(user, (500, count))
            screen.blit(points, (780, count))

            count += 40
            name_count += 1
        else:
            break


def help(with_enemy):
    pygame.draw.rect(screen, (212, 50, 50),
                     (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 3)

    draw_text(" How to play: ", small_font, (320, 110), (255, 255, 255))

    if with_enemy:
        draw_text(" 1. answer all the questions to complete the game", new_font, (320, 200), (255, 255, 255))
        draw_text(" 2. There are 3 modes:", new_font, (320, 250), (255, 255, 255))
        draw_text("     -  random: random movement", new_font, (320, 280), (255, 255, 255))
        draw_text("     -  scatter (green/blue): enemies moves quickly ", new_font, (320, 320), (255, 255, 255))
        draw_text("        to corners of maze", new_font, (320, 350), (255, 255, 255))
        draw_text("     -  chase (purple): enemies will chase you when ", new_font, (320, 390), (255, 255, 255))
        draw_text("        you only have 1 question left.", new_font, (320, 420), (255, 255, 255))
        draw_text(" 3. when you collide with an enemy all progress", new_font, (320, 470), (255, 255, 255))
        draw_text("    will be lost !!!!", new_font, (320, 500), (255, 255, 255))


    elif not with_enemy:
        draw_text(" 1. find the exit of the maze.", new_font, (320, 200), (255, 255, 255))
        draw_text(" 2. answer as many questions correctly as you can", new_font, (320, 250), (255, 255, 255))
        draw_text(" 3. you should only click solution if you are", new_font, (320, 300), (255, 255, 255))
        draw_text("    really stuck !!!", new_font, (320, 330), (255, 255, 255))


def leader_board():
    list_user = format()
    lb_user = {}

    # using a dictionary to tally up the points for each player
    for user in list_user:
        if user[0] in lb_user:
            lb_user[user[0]] += int(user[1])
        else:
            lb_user[user[0]] = int(user[1])

    # adding all values from the dictionary to the list
    sorted_user = []
    for i in lb_user:
        sorted_user.append([i, lb_user[i]])

    # sorting the list
    sorted_user = merge_sort(sorted_user)

    pygame.draw.rect(screen, (20, 124, 100),
                     (top_left[0], top_left[1], maze_width_and_height + 2, maze_width_and_height + 2), 0)
    running = True
    while running:
        screen.fill(menu_colours[13])

        # everytime the mouse is presses down, its coordinates are stored in mx and my

        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)
        return_button.draw(small_font)

        # leader board image
        LB = pygame.image.load("images/LB.png")
        # change the size
        LB = pygame.transform.scale(LB, (700, 500))
        # draw the picture to the screen to the left corner, where the exit will always be
        screen.blit(LB, (200, 200))

        # formatting
        header_text = " "
        header_text += "%-9s" % "Rank"
        header_text += "%-12s" % "Player"
        header_text += "%-64s" % "Points"

        draw_text("Leader board", big_font, (300, 50), (255, 255, 255))
        draw_text(header_text, small_font, (250, 250), (0, 0, 0))

        count = 340
        name_count = 1

        for user in sorted_user:
            # this if statement shows how many names appear on the screen: 10
            if name_count < 11:
                num = str(user[1])

                # drawing the text to the surface
                rank = very_small_font.render(str(name_count), True, (255, 0, 0))
                user = very_small_font.render(str(user[0]), True, (255, 0, 0))
                points = very_small_font.render(num, True, (255, 0, 0))

                screen.blit(rank, (300, count))
                screen.blit(user, (450, count))
                screen.blit(points, (700, count))

                count += 34
                name_count += 1
            else:
                break

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # every time you click down it is a mousebuttondown event
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")
                if return_button.rectangle.collidepoint(event.pos):
                    running = False

        # update the display window each loop
        pygame.display.update()


def levels(with_enemy, file, username):
    colours = menu_colours[14]
    # buttons list contains all of the buttons for levels
    buttons_list = []
    # the number written on each button = n
    n = 1
    # y-coordinates (229, 354, 479, 604)
    # x-coordinates (262, 412, 562, 712)
    for y in range(229, 605, 125):
        for x in range(262, 713, 150):
            # creating an object from the Button class and appending it to the list
            # in the button class:  pygame.Rect(x, y, 75, 75) = rectangle
            # in the button class: str(n) = text
            # in the button class: colour = colour
            buttons_list.append(Button(pygame.Rect(x, y, 75, 75), " " + str(n), random.choice(colours), 0))
            n += 1

    running = True
    while running:
        screen.fill(menu_colours[15])

        draw_text("Levels", big_font, (420, 50), (255, 255, 255))

        # return button
        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)
        return_button.draw(small_font)

        # for each button in the buttons list
        # we call the draw method from the Button class on each button object from the buttons list
        for button in buttons_list:
            button.draw(small_font)

        # every time a player presses a button in the game, it is an event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # mousebuttondown = everytime the button is clicked down
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")
                # for each button in button_list
                # if the coordinates of my mouse are the same as one the buttons
                # then I will run the game loop
                for i in range(len(buttons_list)):
                    if buttons_list[i].rectangle.collidepoint(event.pos):
                        # initial value for w = 60 but it gets smaller each time
                        # initial value for num cols and num rows = 10 but increases by 1 for each level
                        if with_enemy:
                            game(int(600 / (i + 10)), 10 + i, i + 1, with_enemy, file, username)
                        else:
                            game(int(600 / (i + 10)), 10 + i, i + 1, with_enemy, file, username)

                if return_button.rectangle.collidepoint(event.pos):
                    running = False

        pygame.display.update()


def options(username):
    enemy = False
    file = "cs.csv"

    running = True
    while running:
        screen.fill(menu_colours[16])  # fill the whole screen with a colour

        with_enemy_button = Button(pygame.Rect(100, 250, 370, 70), " " + "With enemies", menu_colours[17], 0)
        with_enemy_button.draw(small_font)

        without_enemy_button = Button(pygame.Rect(100, 350, 370, 70), " Without enemies", menu_colours[17], 0)
        without_enemy_button.draw(small_font)

        Maths_button = Button(pygame.Rect(560, 250, 370, 70), "   Maths", menu_colours[19], 0)
        Maths_button.draw(small_font)

        CS_button = Button(pygame.Rect(560, 350, 370, 70), " Computer Science", menu_colours[19], 0)
        CS_button.draw(small_font)

        Physics_button = Button(pygame.Rect(560, 450, 370, 70), "    Physics", menu_colours[19], 0)
        Physics_button.draw(small_font)

        continue_button = Button(pygame.Rect(330, 610, 370, 70), "  Continue", menu_colours[20], 0)
        continue_button.draw(small_font)

        return_button = Button(pygame.Rect(50, 50, 75, 75), " R", menu_colours[6], 3)
        return_button.draw(small_font)

        draw_text("Options:", big_font, (350, 80), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")

                # checking the collisions
                if with_enemy_button.rectangle.collidepoint(event.pos):
                    enemy = True
                elif without_enemy_button.rectangle.collidepoint(event.pos):
                    enemy = False
                elif Maths_button.rectangle.collidepoint(event.pos):
                    file = "maths.csv"
                elif CS_button.rectangle.collidepoint(event.pos):
                    file = "cs.csv"
                elif Physics_button.rectangle.collidepoint(event.pos):
                    file = "physics.csv"
                elif continue_button.rectangle.collidepoint(event.pos):
                    levels(enemy, file, username)
                elif return_button.rectangle.collidepoint(event.pos):
                    running = False

        # updates the screen to show changes
        pygame.display.update()


def login():
    image = pygame.image.load("images/BG_maze.png")
    image = pygame.transform.scale(image, (width, height))

    running = True
    while running:
        # draw the picture to the screen
        screen.blit(image, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (110, 90, 800, 600), 0)
        pygame.draw.rect(screen, (0, 0, 0), (110, 90, 800, 600), 4)

        login = Button(pygame.Rect(300, 300, 370, 70), " " + " login", menu_colours[19], 0)
        login.draw(small_font)

        make_account = Button(pygame.Rect(300, 450, 370, 70), " make account", menu_colours[19], 0)
        make_account.draw(small_font)

        draw_text("Revision Maze Game", big_font, (160, 100), (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_effect("click.wav")

                # checking the collisions
                if login.rectangle.collidepoint(event.pos):
                    type_in(True)
                elif make_account.rectangle.collidepoint(event.pos):
                    type_in(False)

        # updates the screen to show changes
        pygame.display.update()


def type_in(login):
    image = pygame.image.load("images/BG_maze.png")
    image = pygame.transform.scale(image, (width, height))

    username_text = ""
    password_text = ""
    colour1 = (0, 0, 0)
    colour2 = (0, 0, 0)

    users = []
    file = open("files/users.txt", "r")
    for line in file:
        user = line.split(",")
        users.append(user)
    file.close()

    taken = False
    active = False
    button = "username"
    text = ""

    running = True
    while running:
        # draw the picture to the screen
        screen.blit(image, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (110, 90, 800, 600), 0)
        pygame.draw.rect(screen, (0, 0, 0), (110, 90, 800, 600), 4)

        # text button
        pygame.draw.rect(screen, menu_colours[19], (420, 220, 400, 80), 0)
        username = Button(pygame.Rect(420, 220, 400, 80), " " + username_text, colour1, 4)
        username.draw(small_font)

        # text button
        pygame.draw.rect(screen, menu_colours[19], (420, 420, 400, 80), 0)
        password = Button(pygame.Rect(420, 420, 400, 80), " " + password_text, colour2, 4)
        password.draw(small_font)

        # confirm button
        confirm_button = Button(pygame.Rect(400, 580, 200, 70), " Confirm", (100, 200, 200), 0)
        confirm_button.draw(small_font)

        # return button
        return_button = Button(pygame.Rect(23, 22, 75, 75), " R", (0, 0, 0), 0)
        return_button.draw(small_font)

        draw_text("Username: ", small_font, (200, 230), (0, 0, 0))
        draw_text("Password: ", small_font, (200, 430), (0, 0, 0))

        draw_text(text, small_font, (280, 110), (255, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if button == "username":
                        # if the user wants to remove a letter
                        if event.key == pygame.K_BACKSPACE:
                            username_text = username_text[:-1]
                        else:
                            # add the character typed in by the user to user_text
                            username_text = str(username_text + event.unicode)
                    if button == "password":
                        # if the user wants to remove a letter
                        if event.key == pygame.K_BACKSPACE:
                            password_text = password_text[:-1]
                        else:
                            # add the character typed in by the user to user_text
                            password_text = str(password_text + event.unicode)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if username.rectangle.collidepoint(event.pos):
                    button = "username"
                    colour1 = (240, 255, 0)
                    colour2 = (0, 0, 0)
                    active = True
                    sound_effect("click.wav")
                elif password.rectangle.collidepoint(event.pos):
                    button = "password"
                    colour2 = (240, 255, 0)
                    colour1 = (0, 0, 0)
                    active = True
                    sound_effect("click.wav")
                else:
                    colour1 = (0, 0, 0)
                    colour2 = (0, 0, 0)
                    active = False

                if confirm_button.rectangle.collidepoint(event.pos):
                    if login:
                        for user in users:
                            if str(user[0]) == str(username_text):
                                taken = True
                                password = user[1].split("/")
                                password = str(password[0])
                                break
                            elif str(user[0]) != str(username_text):
                                taken = False
                                password = ""

                        if taken:
                            if password_text.split() == password.split():
                                sound_effect("click.wav")
                                main(str(username_text))
                            else:
                                sound_effect("wrong.wav")
                                text = "wrong password"

                        if not taken:
                            if str(password_text) != str(password):
                                sound_effect("wrong.wav")
                                text = "username does not exist"

                    if not login:

                        for user in users:
                            if str(user[0]) == str(username_text):
                                taken = True
                                text = "username Taken"
                                break
                            elif str(user[0]) != str(username_text):
                                taken = False

                        if not taken:
                            # adding points to file
                            file = open("files/users.txt", "a")
                            # Append text (username + level + score (at some point)) at the end of file
                            file.write("\n" + username_text + "," + password_text)
                            file.close()
                            sound_effect("click.wav")
                            running = False
                        elif taken:
                            sound_effect("wrong.wav")

                if return_button.rectangle.collidepoint(event.pos):
                    running = False

        # updates the screen to show changes
        pygame.display.update()


login()
