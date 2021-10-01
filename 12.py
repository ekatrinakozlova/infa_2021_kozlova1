import pygame
from pygame.draw import *
from math import *
pygame.init()

def oval(x0, y0, r, h=1.0, rot=0, color = (255, 255, 255), obv = 0):
    points = []
    nPoints = int(max(r, r * h))
    rot = rot * pi / 180
    k = 2 * pi / nPoints
    for i in range(0, nPoints):
        alfa = i * k
        x = r * cos(alfa)
        y = r * sin(alfa) * h
        if rot != 0:
            x, y = x * cos(rot) - y * sin(rot), x * sin(rot) + y * cos(rot)
        x += x0
        y += y0
        points.append([x, y])
    return polygon(screen, color, points, obv)

mountains = [(0, 340), (100, 150), (170, 300), (220, 200), (400, 440), (500, 160), (550, 190), (600, 90), (600, 600), (0, 1000), (0, 340)]
grass = [(0, 500), (5, 505), (20, 500), (35, 490), (60, 480), (350, 500), (355, 550), (360, 590), (360, 595), (600, 600), (600, 1000),
                                  (0, 1000), (0, 500)]
FPS = 30
screen = pygame.display.set_mode((600, 1000))
color = (255, 255, 255)
rect(screen, (135, 206, 235), (0, 0, 794, 1123))
polygon(screen, (169, 169, 169), mountains)
for i in range(len(mountains) - 1):
    line(screen, (0, 0, 0), mountains[i], mountains[i + 1], 1)

polygon(screen, (144, 238, 144), grass)
circle(screen, (50, 205, 50), (500, 780), 100)
ellipse(screen, color, (80, 650, 180, 70))
oval(230, 625, 60, 0.45, 90, color)
ellipse(screen, color, (215, 540, 60, 35))
circle(screen, (238, 0, 238), (242, 553), 12)
oval(100, 700, 30, 0.5, 90, color)
oval(100, 760, 30, 0.5, 90, color)
oval(140, 730, 30, 0.5, 90, color)
oval(140, 790, 30, 0.5, 90, color)
oval(205, 700, 30, 0.5, 90, color)
oval(205, 760, 30, 0.5, 90, color)
oval(230, 710, 30, 0.5, 90, color)
oval(230, 770, 30, 0.5, 90, color)
ellipse(screen, color, (90, 785, 30, 20))
ellipse(screen, color, (130, 810, 30, 20))
ellipse(screen, color, (195, 785, 30, 20))
ellipse(screen, color, (220, 795, 30, 20))
polygon(screen, color, [(215, 550), (210, 520), (225, 550)])
polygon(screen, color, [(220, 550), (225, 520), (230, 550)])
circle(screen, (0, 0, 0), (245, 553), 5)

def flower(x, y, wigth, angle):
    oval(x, y, 10 * wigth, 0.5, angle, color)
    oval(x, y, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x+10, y+5, 10 * wigth, 0.5, angle, color)
    oval(x+10, y+5, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x-10, y+5, 10 * wigth, 0.5, angle, color)
    oval(x-10, y+5, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x, y+7, 10 * wigth, 0.5, angle, (255, 255, 0))
    oval(x+13, y+10, 10 * wigth, 0.5, angle, color)
    oval(x+13, y+10, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x-13, y + 10, 10 * wigth, 0.5, angle, color)
    oval(x-13, y + 10, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x-7, y + 13, 10 * wigth, 0.5, angle, color)
    oval(x-7, y + 13, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
    oval(x+5, y + 15, 10 * wigth, 0.5, angle, color)
    oval(x+5, y + 15, 10 * wigth, 0.5, angle, (0, 0, 0), 1)
flower(510, 700, 1, 0)
flower(450, 710, 1, -30)
flower(460, 750, 1, 0)
flower(520, 800, 1, +30)
flower(550, 730, 1, +15)
flower(570, 780, 1, +10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
