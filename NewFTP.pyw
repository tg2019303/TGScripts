import pygame
from pygame.locals import *
from os import popen,environ
from win32gui import FindWindow
#import win32gui,win32con
#pygame.init()
size=75
startx,starty=0,500
name_dict={(0,0):'zm',
           (0,1):'cjun',
           (0,2):'xmh',
           (1,0):'zxs',
           (1,1):'zjx',
           (1,2):'ysh',
           (2,0):'zjp',
           (2,1):'sxm',
           }
show_dict={(0,0):'语文',
           (0,1):'数学',
           (0,2):'英语',
           (1,0):'物理',
           (1,1):'化学',
           (1,2):'地理杨',
           (2,0):'地理周',
           (2,1):'美术',
           }
def get_grid(x,y):
    print(x,y)
    return(y//size,x//size)
def launch(name):
    if name!='':
        popen('start explorer ftp://%s:123@6.163.193.243'%name)
    else:
        popen('start explorer ftp://6.163.193.243')
    pygame.quit()
def main():
    hwnd=FindWindow(None,'oh-my-ftp')
    if hwnd:
        pygame.quit()
        return
    environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(startx,starty)
    #DIS=pygame.display.set_mode((1,1),NOFRAME)
    pygame.display.set_caption('oh-my-ftp')
    #hwnd=win32gui.FindWindow(None,'oh-my-ftp')
    #a,b,c,d=win32gui.GetWindowRect(hwnd)
    #win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,startx,starty,3*size,3*size,win32con.SWP_NOSIZE)
    DIS=pygame.display.set_mode((3*size,3*size),NOFRAME)
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(DIS,(9,68,134,10),(i*size,j*size,size,size))
            pygame.draw.rect(DIS,(13,140,235,10),(i*size,j*size,size,size),10)
    pygame.display.update()
    pygame.font.init()
##    FontObj=pygame.font.Font('simhei.ttf',20)
    FontObj=pygame.font.SysFont('stliti',24)
##    FontObj.set_italic(True)
    for i in range(3):
        for j in range(3):
            name=show_dict.get((i,j),'')
            #print(name)
            txt=FontObj.render(name,True,(255,255,255))
            rect=txt.get_rect()
            rect.center=(j*size+size/2,i*size+size/2)
            #print(rect)
            DIS.blit(txt,rect)
    BG=pygame.image.load('bg.jpg')
    BG=pygame.transform.scale(BG,(3*size,3*size))
    BG.set_alpha(45)
    DIS.blit(BG,(0,0))        
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                name=(name_dict.get(get_grid(*event.pos),''))
                launch(name)
                return
            if event.type==QUIT:
                pygame.quit()
                return
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    return
                elif 49<=event.key<=57:
                    #print(event.key)
                    num=event.key-49
                    name=(name_dict.get((num//3,num%3),''))
                    launch(name)
                    return
        pygame.time.wait(100)
if  __name__ =='__main__':
    main()
