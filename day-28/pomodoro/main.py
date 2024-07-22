from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# CHECK_MARK = "✔"
reps = 0
timer = None
cycle_counter = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    check_mark_label.config(text='')
    title_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text=f'00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text='Break', fg=RED)
    elif reps%2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text='Break', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count>0:
        timer = window.after(1000, countdown, count-1)
    else:
        if reps%2 != 0:
            cycle = reps//2+1
            if cycle % 4 == 0:
                cycle = 4
            else:
                cycle = cycle % 4
            check_mark_label.config(text=f'{cycle}')
        elif reps % 8 == 0:
            check_mark_label.config(text=f'0') 
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize()
window.title('Pomodoro App')
window.config(bg=YELLOW, padx=100, pady=100)

# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='day-28/pomodoro/tomato.png')
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50), pady=5)
title_label.grid(row=0, column=1)

button_start = Button(text='Start', width=5, font=(FONT_NAME, 12), command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text='Reset', width=5, font=(FONT_NAME, 12), command=reset_timer)
button_reset.grid(row=2, column=2)

check_mark_label = Label(text='0', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44, 'bold'))
check_mark_label.grid(row=3, column=1)

window.mainloop()