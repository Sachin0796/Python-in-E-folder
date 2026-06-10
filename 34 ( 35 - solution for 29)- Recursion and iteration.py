#iterative - we use the iterations to solve the problem. E.G. for loop
#Recursive - calling the function within itself with a break ocndition to yield the output

def fact_iterative(number1):
    fact=1
    for i in range(number1):
        fact=fact*(i+1)
    return fact
print("Factorial using iterative :",fact_iterative(5))

def fact_recursive(number2):
    if number2==1:
        return 1
    else:
        return number2*fact_recursive(number2-1)
print("Factorial using recursive :",fact_recursive(5))

print("************ Function to find nth number in fibonacci series***********")


def nth_fibonaccci_number(nth_number):
    prev_number = 0
    current_number = 1
    next_number = 0
    if nth_number==1:
        return prev_number
    elif nth_number==2:
        return current_number
    else:
        for i in range(nth_number-2):
            next_number=prev_number+current_number
            prev_number=current_number
            current_number=next_number
        return next_number

print("Input is 8 and number in series is",nth_fibonaccci_number(8))
#copied from codewithharry
def nth_fibonaccci_number_recursive(nth_number):
    if nth_number == 1:
        return 0
    elif nth_number == 2:
        return 1
    else:
        return nth_fibonaccci_number_recursive(nth_number-1)+nth_fibonaccci_number_recursive(nth_number-2)

print("Input is 8 and number in series is",nth_fibonaccci_number_recursive(8))