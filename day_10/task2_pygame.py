import numpy as np
import pygame as pg
from pprint import pprint
from time import sleep

GRID_WIDTH = 40
GRID_HEIGHT = 6
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

grid = [["." for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]

pg.init()

x = 1
cycle = 0
special_n = 20
special_cycle = 40
crt = np.full((6, 40), ".")

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((0, 0, 0))

CELL_SIZE = 20

def print_crt():
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            x = i * CELL_SIZE
            y = j * CELL_SIZE

            s = pg.display.get_surface()
            rect = pg.Rect(x, y, CELL_SIZE, CELL_SIZE)

            color = pg.Color("Red") if crt[j][i] == "#" else (0, 0, 0)
            s.fill(color, rect)
    pg.display.flip()

def update_crt():
    sprite = [i + x for i in [-1, 0, 1]]
    row = cycle // 40
    col = cycle % 40

    if col in sprite:
        crt[row][col] = "#"

    print_crt()

with open("day_10/data.txt", "r") as f:
    program = [i.strip().split() for i in f.readlines()]

running, draw = True, True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if draw:
        for line in program:
            update_crt()
            cycle+=1
            if line[0] != "noop":
                update_crt()
                x += int(line[1])
                cycle+=1
            sleep(0.01)
        draw = False
    
        

