# The maths package was imported in order to be able to compute the compound interest
import math 

# This is the first two lines the user will see 
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay monthly on a home loan")

# This code is inputted to allow the user to make their selection
# .lower() is used to mitigate any issues regarding capitalization of the choice the user makes
investment_bond = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")

# This code will activate when the user makes the choice 'investment'
# The while loop is used to hold the two if statements
while investment_bond.lower() == 'investment':

    # This code is used for users who choose the investment option
    deposit = float(input("Please enter the amount you will be depositing into your investment: "))
    interest_rate = float(input("Please enter your investment interest rate. NB: leave out the '%': "))
    investment_period = float(input("How many years do you plan on investing?: "))
    simple_compound = input("Will you be interested in simple or compound interest?: ")

    # Depending on the kind of investment the user wants to make, one of the two codes will run 
    if simple_compound.lower() == 'simple':
        print("The interest amount will amount to: R" + str(deposit * (interest_rate/100 * investment_period)) + " at the end of the period")
        break
    elif simple_compound.lower() == 'compound':
        print("The interest amount will amount to: " + str(deposit * math.pow((1 + interest_rate/100), investment_period)) + " at the end of the period")
        break 

# This code will run when the user chooses the 'bond' option
if investment_bond.lower() == 'bond':
    curr_house_value = float(input("Please enter the current value of the house you want to purchase: "))
    bond_interest = float(input("Please your interest rate. NB: leave out the '%': "))
    repayment_period = float(input("How many years will you be paying off the bond?: ")) # I convert the years to months by multiplying by 12 months in the formula below
    print("The total bond repayment will be: R" + str((bond_interest/100/12 * curr_house_value)/1 - (1 + bond_interest/100/12) ** 
    (-repayment_period * 12)) + " at the end of every month.")
    