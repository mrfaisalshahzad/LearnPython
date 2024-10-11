"""
Here we are repeating coding lines

tom_exp_list = [2100, 3400, 2400]
joe_exp_list = [1200, 2300, 5000]

total = 0
for item in tom_exp_list:
    total = total + item
print("Tom's total expense is ", total)

total = 0
for item in joe_exp_list:
    total = total + item
print("Joe's total expense is ", total)
"""

"""
Defining function

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp_list = [2100, 3400, 2400]
joe_exp_list = [1200, 2300, 5000]

tom_total = calculate_total(tom_exp_list)
joe_total = calculate_total(joe_exp_list)

print("Tom's total expense is ", tom_total)
print("Joe's total expense is ", joe_total)
"""

"""
Positional Arguments
Local vs Global Variables

def sum(a, b):
    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n = sum(10, 5)
print("Total outside function: ", n)
"""


"""
Named Arguments

def sum(a, b):
    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n = sum(b=5, a=6)
print("Total outside function: ", n)
"""


# Default Arguments (should be defined in function argument like b=0)

def sum(a, b=0):

    """
    This function takes two arguments which are integer and returns sum of them as an output.
    """
    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n1 = sum(10)
n2 = sum(10,5)
print("Total outside function: ", n1)
print("Total outside function: ", n2)
