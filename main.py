from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown(work_min_sec)
        title.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(long_break_sec)
        title.config(text="Break", fg=RED)
        checkmark["text"] = ""
    else:
        countdown(short_break_sec)
        title.config(text="Break", fg=PINK)
        checkmark["text"] += "✔"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minute = int(count / 60)
    second = count % 60
    if second == 0 or second < 10:
        second = "0" + str(second)

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_time()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
