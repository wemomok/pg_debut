import pygame as pg
from sys import *

def maincontrol():
    for e in pg.event.get():
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                exit()
