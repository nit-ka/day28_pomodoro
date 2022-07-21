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
timer = None
ticks = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global ticks
    ticks = ""
    label_ticks.config(text=ticks)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global ticks
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            ticks += "✔"
        label_ticks.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_image)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

label_work_sessions = Label(text="Completed work sessions:", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
label_work_sessions.config(pady=20)
label_work_sessions.grid(column=1, row=3)

label_ticks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_ticks.grid(column=1, row=4)

button_start = Button(text="Start", command=start_timer)
button_start.config(font=(FONT_NAME, 18, "bold"), fg="white", bg=GREEN)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.config(font=(FONT_NAME, 18, "bold"), fg="white", bg=PINK)
button_reset.grid(column=2, row=2)

window.mainloop()

