import pygame as pg
from controls import *

sc = pg.display.set_mode((1920, 1080))



while 1:
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        sys.exit()
        print(1)
    maincontrol()
