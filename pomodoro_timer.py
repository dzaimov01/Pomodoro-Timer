import os
import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

t_now = dt.datetime.now()
t_pom = 25 * 60
t_delta = dt.timedelta(0, t_pom)
t_fut = t_now + t_delta
delta_sec = 5 * 60
t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)

root = tkinter.Tk()
root.withdraw()

messagebox.showinfo("Pomodoro Started!", "\nIt is now " + t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")

total_pomodoros = 0
total_breaks = 0

while True:
    if  t_now < t_fut:
        print('Pomodoro!')
    elif t_fut <= t_now <= t_fin:
        print('In break!')
        if total_breaks == 0:
            print('If break')
            for i in range(5):
                winsound.Beep((i+100), 700)
            print('Break time!')
            total_breaks += 1
    else:
        print('Finished!')
        total_breaks = 0
        for i in range(10):
            winsound.Beep((i*100), 500)

        urs_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another pomodoro?")
        total_pomodoros += 1
        if urs_ans:
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)
            continue
        elif not urs_ans:
            messagebox.showinfo("Pomodoro Finished!", "\nYou completed " + total_pomodoros + "pomodoros today!")
            break
    print('Sleeping')
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")
