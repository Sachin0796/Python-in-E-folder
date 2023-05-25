amount=int(input("Enter amount:\n"))
ROI=float(input("Enter ROI:\n"))
years=int(input("Enter years:\n"))
basic=amount

for i in range(0,years):
    if i==0:
        amount = amount  + (basic * ROI / 100)
        # print("First year:",amount)
    else:
        amount = amount + basic +  ((basic + amount) * ROI / 100)
        # print(amount)

print(amount)