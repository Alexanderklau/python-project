from tkinter import *

def resize(ev=NONE):
    label.config(font='Helevetica -%d bold' % scale.get())

top = Tk()
top.geometry('250x250')
label = Label(top,text='Hello World',font='Helvetica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',activebackground='red')
quit.pack()
mainloop()
