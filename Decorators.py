def desiging_function(func1):
    def func2():
        print("Exectution starts..")
        func1()
        print("Execution ends..")
    return func2

@desiging_function                       # Way 1
def func1():
    print("Function called")

# func1=desiging_function(func1)        # Way 2
func1()