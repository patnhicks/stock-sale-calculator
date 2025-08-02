# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 10:06:09 2025

@author: patnh
"""

"""
Assignment 1
7/8/2025
Patrick N. Hicks, R11661632
"""
import sys

# Declare constants
NUM_SHARES = 200
PURCHASE_PRICE = 30
CAP_GAINS_RATE = 0.15


# Collect information about first stock sale
print("\n * First Stock Sale * \n")
while True:
    shares_sold_1 = int(input(f'You have {NUM_SHARES} shares. How many would you like to sell?: '))
    if shares_sold_1 > NUM_SHARES:
        print(f"Error: You don't own enough shares to sell {shares_sold_1}.")
    else:
        break
    
sales_price_1 = float(input('Enter sales price per share: '))

# Declare variables
remaining_shares_1 = NUM_SHARES - shares_sold_1

#Collect information about second stock sale
print("\n * Second Stock Sale * \n")
while True:
    shares_sold_2 = int(input(f'You have {remaining_shares_1} shares left. How many would you like to sell?: '))
    if shares_sold_2 > remaining_shares_1:
        print(f"Error: You don't own enough shares to sell {shares_sold_2}.")
    else: 
        break
    
sales_price_2 = float(input('Enter sales price per share: '))

# Declare variable from combined sales; cost basis and capital gains
total_spent = NUM_SHARES * PURCHASE_PRICE
cost_basis_1 = (shares_sold_1 * PURCHASE_PRICE) 
cost_basis_2 = (shares_sold_2 * PURCHASE_PRICE) 
cost_basis = cost_basis_1 + cost_basis_2
total_shares_sold = shares_sold_1 + shares_sold_2
amount_received = (shares_sold_1 * sales_price_1) + (shares_sold_2 * sales_price_2)
capital_gains = amount_received - cost_basis
capital_gains_tax = max(capital_gains, 0) * CAP_GAINS_RATE
profit = capital_gains - capital_gains_tax

print(f"\nTotal Spent on Initial Stock Purchase: ${total_spent:.2f}")
print(f"Total Received from Sales: ${amount_received:.2f}")
print(f"Capital Gains Tax: ${capital_gains_tax:.2f}")
print(f"Net Profit or Loss: ${profit:.2f}")