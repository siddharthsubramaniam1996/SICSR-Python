import tkinter as tk

def startgame():
    pass

mw = tk.Tk()              #Here I tried (1)
mw.title('The Sadist\'s game')

back = tk.Frame(master=mw, width=5000, height=5000, bg='#ffffff')
back.pack()

go = tk.Button(master=back, text='Start Game', bg='orange', fg='black',
                     command=lambda:startgame()).pack()
close = tk.Button(master=back, text='Quit', bg='white', fg='blue',
                     command=lambda:quit()).pack()
info = tk.Label(master=back, text='Made by Siddharth Subramaniam!', bg='green',
                         fg='black').pack()

mw.mainloop()
