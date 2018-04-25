import os
task_list=['QQMusic.exe','EasiNote.exe',\
           'cmd.exe',\
           'py.exe /t',\
           'pyw.exe /t'
           ]
for i in task_list:
    a=os.popen('taskkill /f -im %s'%i).read()
