units=int(input("Please enter the number of units you consumed:"))

if(units < 50):
    amount = units * 3.60
    tax = 25

# now checking for units less than 100
elif(units <= 100):
    amount = 140 + ((units - 50) * 4.00)
    tax = 35

# now checking for units less or equal to 200
elif(units <= 200):
    amount = 130 + 123.40 + ((units - 100) * 5.40)
    tax = 45

else:
    amount = 130 + 123.40 + 540 + ((units - 200)* 8.35)
    tax= 78

total = amount + tax
print("\Electricity Bill = %.2f" %total)