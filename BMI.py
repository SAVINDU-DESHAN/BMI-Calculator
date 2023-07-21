#import

import os
import time

# Welcome massage

print("\n")
print("\t ////////////////////////////////////////////////////////// \t")
print("\n")
print("\t\t\t ⌛--- BMI Calculator ---⌛ \t\t")
print("\n")
print("\t ////////////////////////////////////////////////////////// \t")
print("\n")

# Variables

print("****************************************")
name = input("⁂ Enter your name \t: ")
print("****************************************")
print("\n")
height = int(input(f"⁕ {name} enter your height \t: "))
weight = int(input(f"⁕ {name} enter your weight \t: "))
prosses = "Your data is processing......."

# Prosses

print("\n")

def loading_animation(duration):
    massage = "Your data is processing......."
    for _ in range(duration):
        print(massage, end='\r')
        time.sleep(1)


if __name__ == "__main__":
    loading_animation(10)
    
print("\n")
bmi_amount = weight/height*2

# Output

print(f"| {name} your BMI amount is {bmi_amount} |")
print("\n")
print("-----------------------------------")
print("BMI Categories: \n⁕Underweight = <18.5 \n⁕Normal weight = 18.5–24.9 \n⁕Overweight = 25–29.9 \n⁕Obesity = BMI of 30 or greater")
print("-----------------------------------")
print("\n")

if bmi_amount<18.5:
    print(f"{name} you are Underweight.")
elif 24.9>bmi_amount>18.5:
    print(f"{name} you are Normal weight.")
elif 29.9>bmi_amount>25:
    print(f"{name} you are Overweight. ")
elif bmi_amount>30:
    print(f"{name} you are Obesity.")
    
# End

print("\n")
print("\t ////////////////////////////////////////////////////////// \t")
print("\n")
print(f"\t\t\t ☘--- {name} Good Bye ---☘ \t\t")
print("\n \t\t\t\t\t ~Program By Savindu Deshan")
print("\t ////////////////////////////////////////////////////////// \t")
print("\n")




# © All Copyright Reserved By Savindu Deshan
