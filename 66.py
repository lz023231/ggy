import win32api
import win32gui
import win32con

h = win32api.GetCursorPos()   #鼠标坐标
handle = win32gui.FindWindow(None, '安卓打包说明.txt - 记事本')
# y = win32gui.FindWindow(None, "Win32Api")
# print(y)
print(handle)
print(h)
menu = win32gui.GetMenu(handle)   #定位窗口
menu1 = win32gui.GetSubMenu(menu,1)  #选择第二个子菜单
cmd_ID = win32gui.GetMenuItemID(menu1, 13)  # 选择第14个选项
win32gui.PostMessage(handle,win32con.WM_COMMAND, cmd_ID, 0)   #执行

