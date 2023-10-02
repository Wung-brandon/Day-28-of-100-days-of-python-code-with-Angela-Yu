from tkinter import *
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
#timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    timer_label.config(text="Timer")
    check_label.config(text="")
    window.after_cancel(timer)
    canva.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "*"
        check_label.config(text=marks)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.geometry("400x400")
window.config(pady=10,bg=YELLOW)


timer_label = Label(window, text="Timer",fg=GREEN,font=(FONT_NAME,40,'bold'),
                    bg=YELLOW)
timer_label.pack()


canva = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(100, 112, image=tomato_img)
timer_text = canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,'bold'))
canva.pack(pady=15)

start_btn = Button(window,text="Start",bd=4,cursor='hand2',command=start_timer)
start_btn.place(x=60,y=310)

check_label = Label(window, text="",fg=GREEN,font=(FONT_NAME,15,'bold'),
                    bg=YELLOW)
check_label.place(x=190,y=330)

reset_btn = Button(window,text="Reset",bd=4,cursor='hand2',command=reset_timer)
reset_btn.place(x=285,y=310)




window.mainloop()