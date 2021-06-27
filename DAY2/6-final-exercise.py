"""
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
"""

print("Welcome to Tip Calculator")
total_bill = float(input("Enter the value of total bill? "))
persons = int(input("Enter no. of persons: "))
tip = int(input("How much do you would you like to tip 12%, 15%, 18%, 20%?"))

total_bill_tip = total_bill + ((total_bill * tip) / 100)

print(total_bill_tip)
spilt_value  = round(total_bill_tip / 5, 2)


print(f"Each person should split the value of ${spilt_value} of the total value.")
