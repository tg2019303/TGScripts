import win32con
import win32gui
import time
from os import system, chdir
hwnd = win32gui.FindWindow('ConsoleWindowClass', 'jupyter')
txt = win32gui.GetWindowText(hwnd)
print(hwnd, txt)
if hwnd:
    out = win32gui.ShowWindow(hwnd, win32con.SW_HIDE)  # SHOWNORMAL)
    print(hwnd, out)
    if out == 0:
        out = win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
else:
    # pass
    chdir(r'C:\Users\Administrator\Desktop\Scripts')
    system('start jupyter-notebook')
    time.sleep(5)
    hwnd = win32gui.FindWindow('ConsoleWindowClass', None)
    win32gui.SetWindowText(hwnd, 'jupyter')
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
# system(r'C:\Users\SEEWO\AppData\Local\Google\Chrome\Application\chrome.exe  localhost:8888/tree#')
# url='localhost:8888/tree#'
# webbrowser.open(url)
