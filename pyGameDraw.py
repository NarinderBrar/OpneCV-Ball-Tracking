import pygame
import sys

import numpy as np
import zmq


ctx = zmq.Context()

sub = ctx.socket(zmq.SUB)
sub.connect('tcp://localhost:5556')
sub.setsockopt(zmq.SUBSCRIBE, b'')

sub.RCVTIMEO = 1000

pygame.init()

fps=300

fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((600,338))
pygame.display.set_caption("Keyboard_Input")
White=(0,0,0)

x=10
y=10

while True:
    sur_obj.fill(White)
    pygame.draw.circle(sur_obj, (255,255,0), (x, y), 15, 1)
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    try:
        msg = sub.recv_json()
    except zmq.error.Again:
        continue
    
    x = msg[0]['x']
    y = msg[0]['y']

    pygame.display.update()
    fpsclock.tick(fps)