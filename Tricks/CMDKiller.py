import os,time,sys
t=0
b=0
for a in ('\\','C:\\','D:\\','E:\\'):
     for i in os.walk(a):
          for j in i[2]:
               try:
                    s=os.path.join(i[0],j)
                    print(s)
                    #time.sleep(0.03)
                    #print(s+'-------------'+str(int(t))+'%')
                    #sys.stdout.seek(0)
                    sys.stdout.write('■'*int(b/100000*30))
                    sys.stdout.flush()
                    os.system('cls')
                    #t+=1.1**(-t)
                    b+=1
                    if t>100:
                         t=0
               except Exception:
                    pass
print(b)
time.sleep(10)
