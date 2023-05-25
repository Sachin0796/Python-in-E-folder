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
print("Total deposited:", basic  * years)
print("Total Return:", amount)
print("Interest gained:", amount - (basic * years))
print("Interest gained per year:", (amount - (basic * years))/years)
print("Interest gained per month:", ((amount - (basic * years))/12)/years)

################# 15 Years Returns ####################

# Enter amount:
# 150000
# Enter ROI:
# 7.1
# Enter years:
# 15
# Total deposited: 2250000
# Total Return: 4068209.220287906
# Interest gained: 1818209.220287906
# Interest gained per year: 121213.94801919373
# Interest gained per month: 10101.162334932811

# Enter amount:
# 100000
# Enter ROI:
# 7.1
# Enter years:
# 15
# Total deposited: 1500000
# Total Return: 2712139.480191937
# Interest gained: 1212139.4801919372
# Interest gained per year: 80809.29867946247
# Interest gained per month: 6734.10822328854

# Enter amount:
# 125000 
# Enter ROI:
# 7.1
# Enter years:
# 15
# Total deposited: 1875000
# Total Return: 3390174.350239922
# Interest gained: 1515174.3502399218
# Interest gained per year: 101011.62334932812
# Interest gained per month: 8417.635279110676

# Enter amount:
# 75000
# Enter ROI:
# 7.1
# Enter years:
# 15
# Total deposited: 1125000
# Total Return: 2034104.610143953
# Interest gained: 909104.610143953
# Interest gained per year: 60606.97400959687
# Interest gained per month: 5050.5811674664055

################# 30 Years Returns ####################

# Enter amount:
# 150000
# Enter ROI:
# 7.1
# Enter years:
# 30
# Total deposited: 4500000
# Total Return: 15450910.594092919
# Interest gained: 10950910.594092919
# Interest gained per year: 365030.3531364306
# Interest gained per month: 30419.196094702555

# Enter amount:
# 100000
# Enter ROI:
# 7.1
# Enter years:
# 30
# Total deposited: 3000000
# Total Return: 10300607.06272861
# Interest gained: 7300607.06272861
# Interest gained per year: 243353.56875762032
# Interest gained per month: 20279.464063135027

# Enter amount:
# 125000
# Enter ROI:
# 7.1
# Enter years:
# 30
# Total deposited: 3750000
# Total Return: 12875758.828410765
# Interest gained: 9125758.828410765
# Interest gained per year: 304191.9609470255
# Interest gained per month: 25349.330078918792

# Enter amount:
# 75000
# Enter ROI:
# 7.1
# Enter years:
# 30
# Total deposited: 2250000
# Total Return: 7725455.297046459
# Interest gained: 5475455.297046459
# Interest gained per year: 182515.1765682153
# Interest gained per month: 15209.598047351277


