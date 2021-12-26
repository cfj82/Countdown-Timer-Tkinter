
import tkinter as tk
from tkinter import ttk
import time
import threading

# create GUI
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("340x330")

total_time = int(0)

hour = int(0)
minute = int(0)
second = int(0)

def add_hr():
    global total_time, hour, minute, second
    total_time = total_time + 3600
    update_time()


def add_min():
    global total_time, hour, minute, second
    total_time = total_time + 60
    update_time()


def add_sec():
    global total_time, hour, minute, second
    total_time = total_time + 1
    update_time()


def update_time():
    global total_time, hour, minute, second
    hour = total_time/3600
    minute = total_time/60
    second = total_time/1
    hr_live.set("{0:.4f}".format(hour))
    m_live.set("{0:.2f}".format(minute))
    s_live.set("{0:.0f}".format(second))


def start_count():
    global total_time, hour, minute, second
    t = threading.Thread(target=progress_bar, args=(all_prog,))
    t.start()
    all_prog.start(1)
    root.update()
    while total_time > 0:
        hour = total_time / 3600
        minute = total_time / 60
        second = total_time / 1
        hr_live.set("{0:.4f}".format(hour))
        m_live.set("{0:.2f}".format(minute))
        s_live.set("{0:.0f}".format(second))

        root.update()
        total_time = total_time - 1
        time.sleep(1)

    if total_time == 0:
        hr_live.set("- -")
        m_live.set("- -")
        s_live.set("- -")


def progress_bar(args):
    global total_time, hour, minute, second
    for i in range(total_time):
        all_prog['value'] += 2
        root.update_idletasks()   # update for tkinter freeze
        time.sleep(1)
        percent_lbl.config(text="Current Progress: "+str(all_prog['value'])+"%")


def reset():
    global total_time, hour, minute, second
    total_time = 0
    hour = 0
    minute = 0
    second = 0
    hr_live.set("{0:.4f}".format(hour))
    m_live.set("{0:.2f}".format(minute))
    s_live.set("{0:.0f}".format(second))

# frames
f0 = tk.Frame(root, bg="#32174d")
f0.pack(fill="both", expand=True)
f1 = tk.Frame(root, bg="#32174d")
f1.pack(fill="both", expand=True)

# labels
hr_live=tk.StringVar()
hr_live_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                    bg="#32174d", fg="gray", textvariable=hr_live)
hr_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                    bg="#32174d", fg="gray", text="Hours")

m_live=tk.StringVar()
min_live_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                       bg="#32174d", fg="gray", textvariable=m_live)
min_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                    bg="#32174d", fg="gray", text="Minutes")

s_live=tk.StringVar()
sec_live_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                       bg="#32174d", fg="gray", textvariable=s_live)
sec_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='center',
                    bg="#32174d", fg="gray", text="Seconds")

t_live=tk.StringVar()
t_live.set("Countdown Clock")
total_lbl = tk.Label(f0, font=("Helvetica", 18), relief="flat", border=7, justify='right',
                    bg="#32174d", fg="gray", textvariable=t_live)

percent_lbl = tk.Label(f0, font=("Helvetica", 15), relief="flat", border=7, justify='right',
                    bg="#32174d", fg="gray",text="Current Progress: 0%" )

hr_live_lbl.grid(row=0, column=0)
hr_lbl.grid(row=1, column=0, padx=5, )
min_live_lbl.grid(row=0, column=1)
min_lbl.grid(row=1, column=1, padx=5, )
sec_live_lbl.grid(row=0, column=2)
sec_lbl.grid(row=1, column=2, padx=5, )
percent_lbl.grid(row=3, column=0, columnspan=3, padx=5, pady=1)
total_lbl.grid(row=5, column=0, columnspan=3, pady=10, padx=5, sticky='nsew')


# progress bars
# indeterminate means bar shows an indicator that bounces back and forth. used for not knowing measure time
# progress bar styles
prog_s = ttk.Style()  # must tell tkinter to change the default style
prog_s.theme_use('clam')
prog_s.configure("def.Vertical.TProgressbar", foreground='yellow', background='black',)  # create custom vertical progress bar

all_prog = ttk.Progressbar(f0, orient='horizontal', mode='determinate', length=300)

all_prog.grid(row=2, column=0, columnspan=3, padx=10, pady=8)


# buttons
hr_btn = tk.Button(f0, font=("Helvetica", 13), anchor="center", activebackground="#7B68EE", border=5,
                 bg="#A569BD", relief=tk.GROOVE, text="Add Hour", command=add_hr)
min_btn = tk.Button(f0, font=("Helvetica", 13), anchor="center", activebackground="#7B68EE", border=5,
                 bg="#A569BD", relief=tk.GROOVE, text="Add Min", command=add_min)
sec_btn = tk.Button(f0, font=("Helvetica", 13), anchor="center", activebackground="#7B68EE", border=5,
                 bg="#A569BD", relief=tk.GROOVE, text="Add Sec", command=add_sec)
start_btn = tk.Button(f0, font=("Helvetica", 13), anchor="center", activebackground="#7B68EE", border=5,
                 bg="#A569BD", relief=tk.GROOVE, text="Start", command=start_count)
# start_btn = tk.Button(f0, font=("Helvetica", 12), anchor="center", activebackground="#7B68EE", border=5,
#                  bg="#A569BD", relief=tk.GROOVE, text="Start", command=lambda: threading.Thread(start_count()).start() )

hr_btn.grid(row=4, column=0, padx=10, pady=8)
min_btn.grid(row=4, column=1, padx=10, pady=8)
sec_btn.grid(row=4, column=2, padx=10, pady=8)
start_btn.grid(row=6, column=1)



# create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# create menu drop down
option_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=option_menu)

option_menu.add_command(label='Reset Time', command=reset)
option_menu.add_separator()  # adds line to separate
option_menu.add_command(label='Quit', command=root.quit)

root.mainloop()
