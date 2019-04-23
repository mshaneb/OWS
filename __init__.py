# python 3
# this one initializes the gui and so forth


import os
import ohrf_report
from tkinter import *
from tkinter import Menu

def openreadme():
    os.startfile("readme.txt")

window = Tk()
window.title("OWS File Index Utility")
window.geometry("500x500")

menu = Menu(window)
window.config(menu = menu)
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "ReadMe", command = openreadme)
helpmenu.add_command(label = "Quit", command = window.quit)
##menu.add_command(label = "Custom Report")
##menu.add_command(label = "Existing Report")

#premade reports, all run OHRF currently
runohrflabel = Label(window, text = "Choose Report:") #add "or" to str later
runohrflabel.grid(row = 0, column = 1, padx = "60")
ohrfbtn = Button(window, text = "OHRF", command = ohrf_report.main)
ohrfbtn.grid(row = 1, column = 1, padx = "20", pady = "5")
### UNCOMMENT THIS BELOW WHEN THESE REPORTS ARE READY
##omabtn = Button(window, text = "OMA", command = oma_report.main) #this one's ready
##omabtn.grid(row = 2, column = 1, padx = "20", pady = "5")
##srambbtn = Button(window, text = "OWS All", command = sramb_report.main)
##srambbtn.grid(row = 4, column = 1, padx = "20", pady = "5")

#file type check button
#below here starts the test

##checkboxinfo = Label(window, text = "Check any combination of boxes to filter by extension:")
##checkboxinfo.grid(row = 0, sticky = W)
##var1 = IntVar()
##Checkbutton(window, text = "All", variable = var1).grid(row=1, column = 0, sticky = W)
##var2 = IntVar()
##Checkbutton(window, text = "PDF", variable = var2).grid(row=2, column = 0, sticky = W)
##var3 = IntVar()
##Checkbutton(window, text = "PowerPoint", variable = var3).grid(row=3, column = 0, sticky = W)
##var4 = IntVar()
##Checkbutton(window, text = "Word", variable = var4).grid(row=4, column = 0, sticky = W)
##var5 = IntVar()
##Checkbutton(window, text = "Excel", variable = var5).grid(row=5, column = 0, sticky = W)
##var6 = IntVar()
##Checkbutton(window, text = "Images", variable = var6).grid(row=6, column = 0, sticky = W)
##var7 = IntVar()
##Checkbutton(window, text = "Drawings (DWGs Only)", variable =7).grid(row=7, column = 0, sticky = W)
##filepathinfo = Label(window, text = "Enter up to 6 directories manually:")
##filepathinfo.grid(row = 8, column = 0, pady = (5, 0))
##p1 = Entry(window).grid(row = 9, column = 0)
##p2 = Entry(window).grid(row = 10, column = 0)
##p3 = Entry(window).grid(row = 11, column = 0)
##p4 = Entry(window).grid(row = 12, column = 0)
##p5 = Entry(window).grid(row = 13, column = 0)
##p6 = Entry(window).grid(row = 14, column = 0)
##
##keywordsinfo = Label(window, text = "Keywords:")
##keywordsinfo.grid(row = 15, column = 0, pady = (15, 0))
##keywords = Entry(window).grid(row = 16, column = 0)
##
##
##runbtn = Button(window, text = "Run Report", command = ohrf_report.main)
##runbtn.grid(row = 17, column = 0, pady = "5")

#test ends above here

mainloop()