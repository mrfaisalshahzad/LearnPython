#A built-in data type that stores a set of values
#it canstore elements of different types  (integer, float, string, etc)
#Lists are mutable (changeable)
#Strings are immutable (non changable)

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["faisal", 95.4, 17, "Riyadh"]
print(student)


#list slicing

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[:len(marks)])


#list methods

#list.append(4)  adds one element at the end
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
marks.append(25.6)
print(marks)

#list.sort()  sorts in ascending order
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks.sort())  #returns None because it making changes ot orignal string
marks.sort()
print(marks)

#list.sort(reverse = True)  sorts in decending order
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks.sort(reverse = True))  #returns None because it making changes ot orignal string
marks.sort(reverse = True)
print(marks)

#list.reverse()  reverses list
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
list = ["apple", "banana", "strawbery", "cherry"]
marks1.reverse()
marks2.reverse()
print(marks)
print(list)

#list.insert(idx, el)  insert element at a specific index
list = ["apple", "banana", "strawbery", "cherry"]
list.insert(2, "kiwi")
print(list)

#list.remove(1)  removes first occurence of element
list = ["apple", "banana", "strawbery", "appple", "cherry"]
list.remove("apple")
print(list)

#list.pop(idx)  removes element at idx
list = ["apple", "banana", "strawbery", "appple", "cherry", "apple"]
list.pop(4)
print(list)