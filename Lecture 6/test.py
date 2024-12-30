#waf to check if a number is odd or even. (number is the parameter)

number = 22

def odd_even(n):
    if(n%2 == 0):
        print(n, "is even")
    else:
        print(n, "is odd")
    
odd_even(number)