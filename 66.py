import win32api
import win32gui
import win32con

h = win32api.GetCursorPos()
t = win32gui.FindWindow(None, '安卓打包说明.txt - 记事本')
# y = win32gui.FindWindow(None, "Win32Api")
# print(y)
print(t)
print(h)
menu = win32gui.GetMenu(t)
menu1 = win32gui.GetSubMenu(menu,1)  #第二个子菜单
cmd_ID = win32gui.GetMenuItemID(menu1, 13)  # 第14个选项
print(1)
win32gui.PostMessage(t,win32con.WM_COMMAND, cmd_ID, 0)
print(2)