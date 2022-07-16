i=0
while(i<100):
    i = i + 1
    if i<5:
        continue
    if i==45:
        break
    print(i,end=" ")
# ask for input untill input is greater than 100

a=int(input("\nEnter ur number:"))
while(a<=100):
    a = int(input("Try again\n"))
    continue
if(a>100):
    print("Congrats.!! You have entered a number greater than 100")
