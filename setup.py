import cx_Freeze as cx_f
import sys
import os

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"


os.environ['TCL_LIBRARY'] = r'D:\Git\mingw64\lib\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Git\mingw64\lib\tk8.6'

executables = [cx_f.Executable("__init__.py")]

cx_f.setup(name = "run", executables=executables)

