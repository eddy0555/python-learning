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

bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * (tip_percent / 100)
total = bill + tip

print("Tip:", tip)
print("Total:", total)