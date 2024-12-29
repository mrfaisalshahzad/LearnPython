#Accessing parts of string is called slicing

#str [starting_idx : ending_idx]  ending idx is not included

#+ve indexing

str = "Faisal Shahzad"

print(str[1:4])
print(str[1:7])


#-ve indexing

print(str[-4:-1])
print(str[-7:-1])
print(str[-len(str):-1])
print(str[:-1])