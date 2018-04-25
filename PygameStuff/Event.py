import pygame,time,direction
from pygame.locals import *
pygame.init()
DIS=pygame.display.set_mode((200,200))
DIS.fill((255,255,255))
pygame.display.update()
direction.add_pattern('IKJL')
while True:
     #keystate = pygame.key.get_pressed()
          
     #print(keystate[K_SPACE])
     for event in pygame.event.get():
          s=pygame.event.event_name(event.type)
          
          if event.type==pygame.KEYDOWN:
               for k,i in direction.get_key_direction(event).items():
                    print(k,i)
               print('-'*20)
               #print(pygame.key.name(event.key),end=' ')
          #print(s,event.dict)
     time.sleep(0.2)

