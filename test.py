#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:47:40 2021

@author: bertiethorpe
"""

#### ASCII GRAPHICS OF ROTATING TORUS ####


import os
import pygame as pg
import numpy as np

TEXT = (255,255,255)
BACKGROUND = (0,0,0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 600, 600
FPS = 60

pixel_width = 15
pixel_height = 15

x_pixel = 0
y_pixel = 0
k = 0

screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height
screen_size = screen_width * screen_height

pg.init()

screen = pg.display.set_mode(RES)
clock = pg.time.Clock()
pg.display.set_caption('Torus')
font = pg.font.SysFont('Arial', 15, bold=True)

def textdisplay(char, x, y):
    text = font.render(str(char), True, TEXT)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

running = True

while running:
    clock.tick(FPS)
    
    screen.fill(BACKGROUND)
    
    output = ['+'] * screen_size
    
    for i in range(screen_height):
        y_pixel += pixel_height
        for j in range(screen_width):
            x_pixel += pixel_width
            textdisplay(output[k], x_pixel, y_pixel)
            k += 1
        x_pixel = 0
    y_pixel = 0
    k = 0
    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()

               
