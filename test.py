# all of the tkinter involved imports
import tkinter as tk
from tkinter import filedialog
# from tkinter.colorchooser import askcolor
from tkinter import ttk
# import tkinter.scrolledtext as tkst
import tkinter.font
# from uuid import uuid4

# end of tkinter specific imports
# get the tkinter detailed version
tclversion_detailed = tkinter.Tcl().eval('info patchlevel')
framework_version = tclversion_detailed
print(tclversion_detailed)
print(framework_version)
x=tkinter.Tcl().eval('info pr')
print(type(x))
print(x)