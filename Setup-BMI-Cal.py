import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    global name_entry, height_entry, weight_entry, bmi_result_label

    name = name_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    bmi_amount = weight / ((height / 100) ** 2)

    bmi_result_label.config(text=f"{name}, your BMI amount is {bmi_amount:.2f}")

    if bmi_amount < 18.5:
        messagebox.showinfo("BMI Result", f"{name}, you are Underweight.")
    elif 24.9 >= bmi_amount >= 18.5:
        messagebox.showinfo("BMI Result", f"{name}, you are Normal weight.")
    elif 29.9 >= bmi_amount > 25:
        messagebox.showinfo("BMI Result", f"{name}, you are Overweight.")
    elif bmi_amount >= 30:
        messagebox.showinfo("BMI Result", f"{name}, you are Obesity.")

def main():
    global name_entry, height_entry, weight_entry, bmi_result_label

    window = tk.Tk()
    window.title("BMI Calculator")
    window.geometry("300x250")

    welcome_label = tk.Label(window, text="⌛--- BMI Calculator ---⌛", font=("Arial", 14, "bold"))
    welcome_label.pack(pady=10)

    name_label = tk.Label(window, text="Enter your name:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    height_label = tk.Label(window, text="Enter your height (in cm):")
    height_label.pack()
    height_entry = tk.Entry(window)
    height_entry.pack()

    weight_label = tk.Label(window, text="Enter your weight (in kg):")
    weight_label.pack()
    weight_entry = tk.Entry(window)
    weight_entry.pack()

    calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
    calculate_button.pack(pady=10)

    bmi_result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
    bmi_result_label.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
    
# © All Copyright Reserved By Savindu Deshan    
