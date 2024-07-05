income = float(input("Enter the income: "))
tax = 0.0

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0:
    tax = 0.0

tax = round(tax)
print(f"The tax is: {tax} thalers")
