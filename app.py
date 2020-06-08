import tkinter as tk
from tkinter import OptionMenu as OptionMenu
from tkinter import StringVar as StringVar

from process import *

def crunch():
    '''Executed when 'crunch!' button is clicked. Updates default output/instructions
    with the results of the age and claims input'''
    claims = claims_var.get()
    if claims == 0 or claims == 1:
        claims = int(claims)
    elif claims == "2-4":
        claims = 3
    elif claims == ">=5":
        claims = 6
    result = process(int(claims), int(age_entry.get()))
    result_text = "Premium increase: ${} Warning Ltr: {} is canceled: {}".format(result.premium_increase, result.warning_letter_enum, result.is_policy_canceled)
    print(result_text)
    output_var.set(result_text)

window = tk.Tk()

output_var = StringVar(window)
output_var.set("Click the \"Crunch\" button to calculate your auto insurance results")

claims_label = tk.Label(text="Previous claims:")
claims_label.pack()

claims_var = StringVar(window)
claims_var.set("0")
claims_entry = OptionMenu(window, claims_var, "0", "1", "2-4", ">=5")
claims_entry.pack()

age_label = tk.Label(text="Driver's age:")
age_label.pack()

age_entry = tk.Entry(fg="black", bg="white", width=40)
age_entry.pack()

button = tk.Button(
    text="Crunch",
    width=12,
    height=2,
    bg="blue",
    fg="yellow",
    command=crunch
)
button.pack()

output = tk.Label(window, textvariable=output_var)
output.pack()

window.mainloop()