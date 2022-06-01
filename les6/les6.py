# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
# import random
# i = 0
# num = []
# while i < 10:
#     num.append(random.randrange(1, 9))
#     i = i + 1
# print(num)
# print('The largest one: ', max(num))


# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random
a = []
b = []
c = []
i = 0
while i < 10:
    a.append(random.randint(1, 10))
    b.append(random.randint(1, 10))
    i = i + 1
i = 1
while i < 11:
    if i in a and i in b: 
        c.append(i)
    i = i + 1

c = list(set(c))
print(a)
print(b)
print(c)


# Make a list that contains all integers from 1 to 100, then find all integers from the list 
# that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
# list_1 = []
# i = 0
# while i < 100:
#     if i % 7 == 0 and i % 5 != 0:
#         list_1.append(i)
#     i = i + 1
# print(list_1)