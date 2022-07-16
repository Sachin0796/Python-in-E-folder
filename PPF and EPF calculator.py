invested_amount_per_year = 150000
ROI=7.1
years=30
total=0

for i in range(years):
    total=total+invested_amount_per_year
    total=total+((total*ROI)*.01)

print("Total invested:","{:,.2f}".format(invested_amount_per_year * years))
print("Total Return:","{:,.2f}".format(total))
print("Interest earned:","{:,.2f}".format(total-(invested_amount_per_year*years)))