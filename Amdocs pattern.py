number_of_rows=int(input("Enter the number of rows you want the pattern to print for:"))
space_before_stars=(number_of_rows-1)*2
numbers_of_stars=1
for i in range(number_of_rows):
    print(" "*space_before_stars,end="")
    print("*"*numbers_of_stars)
    space_before_stars-=2
    numbers_of_stars+=1
below_stars_number=number_of_rows-1
while(below_stars_number>0):
    print("*"*below_stars_number)
    below_stars_number-=1


