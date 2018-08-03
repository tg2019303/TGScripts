from __future__ import print_function
from builtins import input
import random
try:
    import colorama
    colorama.init()
except ImportError:
    pass

RANGE=list('123456789')
CHANCE=10
SEQ=4
MSG='Welcome to the number guessing game.\nCurrent setting of the game is %d chances for you to guess a %d digits.'%(CHANCE,SEQ)
MSG2='Invalid input!'
print('\033[5;33m%s\033[1;37m'%MSG)
def isvalid(num):
    if num==list('exit') or num==['q']:
        print('Let me tell you, it\'s '+''.join(cnum))
        exit()
    for i in num:
        if not i in RANGE:
            return False
    if len(set(num))!=SEQ or len(num)!=SEQ:
        return False
    return True

def judge(c,u):
    a=b=0
    for i in range(SEQ):
        if c[i]==u[i]:
            a+=1
    for i in c:
        if i in u:
            b+=1
    return a,b-a
def main():
    global cnum
    cnum=random.sample(RANGE,k=SEQ)
    for i in range(CHANCE):
        unum=list(input('num: '))
        while not isvalid(unum):
            print('\033[1;35m%s\033[1;37m'%MSG2)
            unum=list(input('num: '))
        a,b=judge(cnum,unum)
        print('  ',a,'A',b,'B',sep='',end='   ')
        if a==SEQ:
            print('You win!')
            return
        if CHANCE-1-i==0:
            print('It is ',''.join(cnum))
            return
        print(CHANCE-1-i,'chances left')
GOING=True
while GOING:
    main()
    GOING=bool(input('Again?'))
