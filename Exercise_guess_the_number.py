n = 36
a=int(input("Enter your number:\n"))
left_guess=4
while(True):
    if(a<n and left_guess>0):
        print("Chances left : ", left_guess)
        a=int(input("Please enter bigger number.\n"))
        left_guess=left_guess-1
        continue
    elif(a>n and left_guess>0):
        print("Chances left : ", left_guess)
        a = int(input("Please enter smaller number.\n"))
        left_guess = left_guess - 1
        continue
    elif(a==n):
        if(left_guess<=1):
            print("You guessed the hidden number",n, "in",5-left_guess,"guesses with",left_guess,"chance left.!!!")
        elif(5-left_guess==1):
            print("You guessed the hidden number", n, "in",5-left_guess,"guess with", left_guess, "chances left.!!!")
        else:
            print("You guessed the hidden number", n, "in", 5 - left_guess, "guesses with", left_guess,
                  "chances left.!!!")
        break
    else:
        print("Game over !! Play Again.!!")
        break