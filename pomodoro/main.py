from  tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_mark.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  #If it's the 1/3/5/7 rep
        count_down(long_break_sec) 
        timer_label.config(text='Long break', fg=RED)
    elif reps % 2 ==0:  #If it's the 2/4/6 rep
        count_down(short_break_sec)
        timer_label.config(text='Short break', fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✓'
        check_mark.config(text=mark)
        
# ---------------------------- User Interface SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW) #additional space on the window

canvas = Canvas(width=320 , height=345, bg=YELLOW, highlightthickness=0) # highlightthickness=0 get rid of white border of canvas

start = Button(text='Start', command=start_timer)
start.grid(row=2, column=0)

restart = Button(text='Restart', command=reset_timer)
restart.grid(row=2, column=2)

timer_label = Label(text= 'Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(row=0 ,column=1)

check_mark = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
check_mark.grid(column=1, row=3)

tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(160, 172, image=tomato_image)

timer_text = canvas.create_text(160, 195, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()