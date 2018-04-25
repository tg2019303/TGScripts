import pygame,time
from pygame.locals import *
pygame.init()
DIS=pygame.display.set_mode((200,200))
DIS.fill((255,255,255))
pygame.display.update()
while True:
     #keystate = pygame.key.get_pressed()
          
     #print(keystate[K_SPACE])
     for event in pygame.event.get():
          s=pygame.event.event_name(event.type)
          
          if event.type==pygame.KEYDOWN:
               pass
               print(pygame.key.name(event.key),end=' ')
          print(s,event.dict)
     time.sleep(0.2)

