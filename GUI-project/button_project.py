import tkinter

top = tkinter.Tk()
quit = tkinter.Button(top,text='Command me!!',command=top.quit())
quit.pack()
tkinter.mainloop()
