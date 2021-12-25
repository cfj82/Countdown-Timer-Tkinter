from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.title('PythonGuides')
root.geometry('400x250+1000+300')

f1= Frame(root)
f1.pack()

def step():
    for i in range(100):
        pb1['value'] += 10
        root.update_idletasks()  ###### update for tkinter freeze
        time.sleep(1)


pb1 = Progressbar(f1, orient=HORIZONTAL, length=100, mode='determinate')
pb1.pack(expand=True)

Button(root, text='Start', command=step).pack()

root.mainloop()