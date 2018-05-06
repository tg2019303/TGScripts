import random

RANGE=list('123456789')
CHANCE=10
SEQ=4
MSG='Welcome to the number guessing game.\nCurrent setting of the game is %d chances for you to guess a %d digits.'%(CHANCE,SEQ)
i,j=5,0
print('\033[5;3%d;4%dm%s\033[0m'%(i,j,MSG))
def isvalid(num):
    for i in num:
        if not i in RANGE:
            return False
    if len(set(num))!=SEQ or len(num)!=SEQ:
        return False
    return True

def gen_num():
    nums=random.sample(RANGE,k=SEQ)
    return nums

def judge(c,u):
    a=b=0
    for i in range(SEQ):
        if c[i]==u[i]:
            #print(c,u,end=' ')
            a+=1
    for i in c:
        if i in u:
            b+=1
    return a,b-a
def main():
    cnum=gen_num()
    for i in range(CHANCE):
        unum=list(input('num: '))
        while not isvalid(unum):
            print('Invalid input!')#,end=' ')
            unum=list(input('num: '))
        a,b=judge(cnum,unum)
        print('  ',a,'A',b,'B',sep='',end='   ')
        if a==SEQ:
            print('You win!')
            return bool(input('Again?'))
        if CHANCE-1-i==0:
            print('It is ',''.join(cnum))
            return bool(input('Again?'))
        print(CHANCE-1-i,'chances left')

while main():
    pass
