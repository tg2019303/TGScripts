import pygame
from pygame.locals import *
from os import popen,environ
from win32gui import FindWindow,ShowWindow,SetWindowPos
import direction
import win32con
#pygame.init()
size=75
size2=30
startx,starty=0,500
pas_dict={'zzx':'1234'}
class NameManager:
    usrs=['zm','cjun','xmh','zxs','zjx','ysh','zjp','cj','zzx']
    names=['语文','数学','英语','物理','化学','地理杨','地理周','历史','钟志兴']
    page=0
    maxpage=len(usrs)//8
    def get_usr(self,i):
        num=self.page*8+i
        if not 0<=i<=7:
            return ''
        return self.usrs[num] if num<len(self.usrs) else ''
    def get_name(self,i):
        num=self.page*8+i
        if not 0<=i<=7:
            return ''
        return self.names[num] if num<len(self.names) else ''
    def pagedown(self):
        self.page=min(self.maxpage,self.page+1)
    def pageup(self):
        self.page=max(0,self.page-1)
def get_grid_num(x,y):
    print(x,y)
    return((y//size)*3+x//size)
def launch(name):
    name1=name+':'+pas_dict.get(name,'123')+'@' if name else ''
    popen('start explorer ftp://%s6.163.193.243'%name1)
    #pygame.quit()
def main():
    environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(startx,starty)
    DIS=pygame.display.set_mode((3*size,3*size),NOFRAME)
    #pygame.event.set_grab(True)
    MINI=False
    MOVING=False
    hwnd=FindWindow(None,'oh-my-ftp')
    if hwnd:
        pygame.quit()
        SetWindowPos(hwnd,win32con.HWND_TOPMOST,startx,starty,3*size,3*size,win32con.SWP_NOSIZE)
        #ShowWindow(hwnd,10)#win32con.SW_SHOWNORMAL
        print('here')
        return
    pygame.display.set_caption('oh-my-ftp')
    hwnd=FindWindow(None,'oh-my-ftp')
    #hwnd=win32gui.FindWindow(None,'oh-my-ftp')
    #a,b,c,d=win32gui.GetWindowRect(hwnd)
    #win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,startx,starty,3*size,3*size,win32con.SWP_NOSIZE)
    #DIS=pygame.display.set_mode((3*size,3*size),NOFRAME)
    BGSurf=pygame.surface.Surface((3*size,3*size))
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(BGSurf,(9,68,134,10),(i*size,j*size,size,size))
            pygame.draw.rect(BGSurf,(13,140,235,10),(i*size,j*size,size,size),10)
    BG=pygame.image.load('bg.jpg')
    BG=pygame.transform.scale(BG,(3*size,3*size))
    BG.set_alpha(45)
    BGSurf.blit(BG,(0,0))        
    pygame.font.init()
    FontObj=pygame.font.SysFont('stliti',24)
    mgr=NameManager()
##    FontObj.set_italic(True)
    def draw_text():
        DIS.blit(BGSurf,(0,0))
        for n in range(8):
            i,j=n//3,n%3
            name=mgr.get_name(n)
            txt=FontObj.render(name,True,(255,255,255))
            rect=txt.get_rect()
            rect.center=(j*size+size/2,i*size+size/2)
            DIS.blit(txt,rect)
        pygame.display.update()
    draw_text()
    def mini():
        environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(0,5*size)
        pygame.display.set_mode((size2,size2),NOFRAME)
        
        pygame.draw.rect(DIS,(9,68,134,10),(0,0,size2,size2))
        pygame.draw.rect(DIS,(13,140,235,10),(0,0,size2,size2),4)
        pygame.display.update()
        pygame.event.get([MOUSEMOTION,MOUSEBUTTONUP])
        return 0,5*size
    def maxi():
        environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(startx,starty)
        DIS=pygame.display.set_mode((3*size,3*size),NOFRAME)
        draw_text()
    while True:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    start_pos=event.pos
            if event.type==MOUSEBUTTONUP:
                if event.button==1:
                    print(event.pos)
                    x0,y0=event.pos
                    
                    if MINI==True :
                        if MOVING==False:
                            print(event.pos,'======')
                            maxi()
                            MINI=False
                        else:
                            MOVING=False
                            pygame.mouse.set_pos(0,0)
                    else:
                        if (x0<3 or x0>size*3-3 or y0<3 or y0>size*3-3):
                            continue
                        x,y=direction.get_mouse_direction(start_pos,event.pos)
                        if y==1:
                            mgr.pageup()
                            draw_text()
                        elif y==-1:
                            mgr.pagedown()
                            draw_text()
                        elif x==-1 and MINI==False:
                            MINI=True
                            #x,y=startx,starty
                            x,y=mini()
                        else:
                            name=mgr.get_usr(get_grid_num(*event.pos))
                            launch(name)
                            MINI=True
                            x,y=mini()
                            #return
                elif event.button==3:
                    pygame.quit()
                    return
                elif event.button==5:
                    mgr.pagedown()
                    draw_text()
                elif event.button==4:
                    mgr.pageup()
                    draw_text()
            if event.type==MOUSEMOTION:
                if MINI==True:
                    MOVING=True
                    x0,y0=event.pos
                    if x0<2:x-=size2//2
                    elif x0>size2-2:x+=size2//2
                    if y0<2:y-=size2//2
                    elif y0>size2-2:y+=size2//2
                    x+=event.rel[0]
                    y+=event.rel[1]
                    SetWindowPos(hwnd,win32con.HWND_TOPMOST,x,y,size2,size2,win32con.SWP_NOSIZE)
                    pygame.event.get([MOUSEMOTION,MOUSEBUTTONUP])
                    print (event.rel,(x,y))
            if event.type==QUIT:
                pygame.quit()
                return
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    return
                elif 49<=event.key<=57:
                    num=event.key-49
                    name=(mgr.get_usr(num))
                    launch(name)
                    MINI=True
                    x,y=mini()
                    #return
                elif event.key==280:
                    mgr.pageup()
                    draw_text()
                elif event.key==281:
                    mgr.pagedown()
                    draw_text()
            elif event.type==ACTIVEEVENT:
                if event.gain==0 and event.state==2 and MINI==False:
                    #print(event.state)
                    mini()
                    MINI=True
                    for i in pygame.event.get(ACTIVEEVENT):#VIDEOEXPOSE):
                        print(i)
            #elif event.type==VIDEOEXPOSE:
                if MINI==True and event.gain==1 and event.state==6:
                    print('---------',event)
                    maxi()
                    MINI=False
                    pygame.event.get(MOUSEBUTTONUP)
                #el
            #else:
                #print(event.__dict__)

        pygame.time.wait(20)
if  __name__ =='__main__':
    main()
