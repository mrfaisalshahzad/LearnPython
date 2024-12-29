list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter number :"))

for val in list:
    if(n == val):
        print("number found at idx", list.index(val))
        break
    else:
        print("finding...")