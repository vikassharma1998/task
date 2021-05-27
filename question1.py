# Python program to find sum of elements in list
total = 0
 
# creating a list
list = [24, 6, 12, 18, 20]
 
# Iterate each element in list
# and add them in variale total
for ele in range(0, len(list)):
    total = total + list[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)