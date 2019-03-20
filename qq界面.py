'''QQ界面'''

import win32gui
import win32con, time, random
print("qq")
while True:
    qq_win = win32gui.FindWindow("TXGuiFoundation","QQ")
    if qq_win:
        win32gui.ShowWindow(qq_win,win32con.SW_HIDE)
        time.sleep(0.5)
        win32gui.ShowWindow(qq_win,win32con.SW_SHOW)
        time.sleep(0.5)
        x,y = random.randint(1,800),random.randrange(500)
        win32gui.SetWindowPos(qq_win,win32con.HWND_TOPMOST,x,y,300,300,win32con.SWP_SHOWWINDOW)
