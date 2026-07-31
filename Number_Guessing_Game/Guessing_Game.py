import tkinter as tk
from tkinter import messagebox
import random


#______________________
#  Window
#______________________

window = tk.Tk()
window.title("🎯 Number Guessing Game 🎯 ")
window.geometry("500x450")
window.configure(background="#EAF6FF")
window.resizable(width=False, height=False)


#______________________
# Title
#______________________

title = tk.Label(window
                 , text="🎯 Number Guessing Game 🎯"
                 ,font=("Arial", 22,"bold"),
                 bg="#EAF6FF"
                 ,fg="#003366"
)

title.pack(pady=20)



#_________________
# Game Variable
#_________________
secret_number = random.randint(1,50)
attempts = 10


#_____________________
# Instructions
#_____________________

instruction_label = tk.Label(window
                             ,text = f"You have {attempts} attempts.\nGuess a number between 1 and 50 "
                             ,font = ("Arial", 13, "bold")
                             ,bg = "#EAF6FF"
                             ,fg="#003366"
)
instruction_label.pack(pady=20)


#______________________
# EntryBox
#______________________

guess_entry = tk.Entry(window
                       ,font = ("Arial", 16, "bold")
                       ,justify="center"
                       ,width= 10
)
guess_entry.pack(pady=10)

#____________________
# Guessing Button
#____________________

guess_button = tk.Button(window
                         ,text="Guess Number"
                         ,font = ("Arial", 12, "bold")
                         ,bg = "#EAF6FF"
                         ,fg="#003366"
                         ,width= 15
)

guess_button.pack(pady=10)


attempt_label = tk.Label(window
                         ,text = f"You have {attempts} attempts"
                         ,font = ("Arial", 12, "bold")
                         ,bg = "#EAF6FF"
                         ,fg="red"
)
attempt_label.pack()

#___________________
# Result Label
#____________________

result_label = tk.Label(window
                        ,text = ""
                        ,font = ("Arial", 13, "bold")
                        ,bg = "#EAF6FF"
)
result_label.pack(pady=10)


#________________________
# Check Guess Function
#_________________________

def check_guess():
    global secret_number
    global attempts

    guess = guess_entry.get()

    if not guess.isdigit():
        messagebox.showerror("Error","Please enter a valid number.")
        return
    guess = int(guess)

    if guess < 1 or guess > 50:
        messagebox.showerror(
            "Error",
            "Please enter a number between 1 and 50."
        )
        return

    attempts-=1

    attempt_label.config(text=f"You have {attempts} attempts")
    guess_entry.delete(0, tk.END)

    if guess == secret_number:
        result_label.config(text=f"🎉 Congratulations! You guessed the number {secret_number}!"
                            , fg = "green"
        )
        messagebox.showinfo("Congratulations","You guessed the number correctly!")
        guess_button.config(state="disabled")

    elif guess < secret_number:
        result_label.config(text="📉 Too Low!",
            fg="black"
        )

    else:
        result_label.config(text ="📈 Too High!",
            fg="orange"
        )

    if attempts ==0 and guess!=secret_number:
        messagebox.showerror("Game Over",f"The correct number was {secret_number}"
        )

        guess_button.config(state="disabled")

# ----------------------------
# Connect Button
# ----------------------------

guess_button.config(command=check_guess)

# ----------------------------
# Run Program
# ----------------------------

window.mainloop()

