from tkinter import *


root = Tk()

root.geometry('400x300+150+150')

def f_event(event,key):
	print(event,key)
	



e = Entry(root, justify=CENTER, font='Arial 15')
e.pack(fill=X, expand=1, padx=10, ipady=10)
e.bind('<Button-1>', lambda event ,key = 'left click':f_event(event,key))
e.bind('<Button-2>', lambda event ,key = 'right click':f_event(event,key))



root.mainloop()
