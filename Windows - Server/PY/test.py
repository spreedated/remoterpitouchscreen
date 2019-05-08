import os
from pywinauto import application
from pywinauto import mouse
import win32api

# (?i) case-insensitive mode ON
# (?-i) case-insensitive mode OFF

mousex, mousey = win32api.GetCursorPos()
app = application.Application().connect(title_re='(?i).*test.*atOm')
Form1 = app.window(title_re='(?i).*test.*atOm')
Form1.type_keys('ADB{SPACE}{ENTER}')

mouse.move(coords=(mousex, mousey))

# print(str(x) + '\t' + str(y) )
