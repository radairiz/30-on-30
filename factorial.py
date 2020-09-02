# Day 1: I did factorial function which is an unary operator ! 
# It is used for determining the cumulative product of all integers before the argument number n
# The following piece of code is to do the factorial code by recursion
def factorial(n):
    # The argument n is any positive integer number
    if isinstance(n,int): #Integer check
        if n >= 0: #Zero or positive check
            r = 1 #Starting value of 1
            for i in range(n, 1, -1): #loop doing recursion from n until 1
                r = r * i #Cumulative product
            print(r) #Result
        else:
            print("Error: The given integer number is not 0 or positive")
    else:
        print("Error: The given expression is not an integer number")

factorial(2) #Results in 2
factorial(6) #Results in 720
factorial(10) #Results in 3,628,800
factorial(3.14) #Thinking about pi
factorial("NaN") #Obviously Not a Number
factorial(-1) #Spreading the negativity
