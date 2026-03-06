"""
Exercise: Number Guessing Game

Description:
A simple program that calculates the tip and total bill amount. 

Concepts practiced:
- user input
- variables
- arithmetic
- formatted output
"""

#ask user for the bill amount
bill = float(input("Enter bill amount: "))
#ask user for the tip percentage
tip_percent = float(input("Enter tip percentage: "))

#calculate tip and total amount with tip
tip = bill * (tip_percent / 100)
total = bill + tip

#print tip and total
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")