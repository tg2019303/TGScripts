import untitled,sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication
class Exam(QMainWindow):
     def __init__(self):
          super().__init__()
          #self.setupUi(None)
          self.show()
def go():
     timer = QtCore.QTimer(md.lcdNumber )
     timer.timeout.connect(dec)
     timer.start(1000)
def dec():
     num=md.lcdNumber.intValue()
     print (num)
##     if num<=0:
##          timer.stop()
     md.lcdNumber.display(num-1)
def timee():
     num=md.lcdNumber.intValue()
     #print (num)
     md.lcdNumber.display(num-1)
     
     while num>0:
          print (num)
          num-=1
          time.sleep(0.1)
          md.lcdNumber.display(num)
          print(md.lcdNumber.update())
app=QApplication(sys.argv )
ex=Exam()
md=untitled.Ui_MainWindow()
md.setupUi(ex)
md.Btn.clicked.connect(go)
sys.exit (app.exec_())
