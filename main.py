import pygame as pg
from lib import Create_BackGround, Draw_Icon
from setting import *

#########################

pg.init()
win = pg.display.set_mode((win_size[0], win_size[1]))

DI = Draw_Icon.draw_icon(win)

DI.Desktop_Add_Icon(0, 0, 'Images/konlimelogo5.png')

DS =  DI.desktop_icons # Desktop Icons



#########################

def Draw_Icon():
    for i in range(0, len(DI.desktop_icons)):
        win.blit(DS[i][2], (DS[i][0] * 50, DS[i][1] * 50))
        pass

#########################

fps_p = int(fps / 60 * 20)

run = True
while run:
    pg.time.delay(fps_p)
    for i in pg.event.get():
        if(i.type == pg.QUIT):
            run = False

    ##########Draw Display###########

    Create_BackGround.Draw(win)

    Draw_Icon()

    pg.display.update()

    #################################

