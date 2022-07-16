import os
import time
import random
choice_list=["Snake","Water","Gun"]
while(True):
    choice=random.choice(choice_list)
    user_input=input("Enter your choice. Snake or Water or Gun:")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    if(user_input=="Snake" and choice=="Water"):
        print("You win.!!")
    elif(user_input=="Water" and choice=="Gun"):
        print("You win.!!")
    elif(user_input=="Gun" and choice=="Snake"):
        print("You win.!!")
    elif(user_input=="Snake" and choice=="Gun"):
        print("You loose.!!")
    elif(user_input=="Water" and choice=="Snake"):
        print("You loose.!!")
    elif(user_input=="Gun" and choice=="Water"):
        print("You loose.!!")
    elif(user_input=="Snake" and choice=="Snake"):
        print("Match draw.!!")
    elif(user_input=="Water" and choice=="Water"):
        print("Match draw.!!")
    elif(user_input=="Gun" and choice=="Gun"):
        print("Match draw.!!")
    else:
        print("Incorrect Input.!! Rules being broken..!! You are disqualified..")
    print("Computer selected:",choice)
    print("Do you want to play again?\n"
          "1. Yes\n"
          "2. No")
    wish_to_continue=int(input())
    if wish_to_continue==2:
        print("Thanks for playing. See you soon.!!")
        exit()