
#for i in range(1,8):
 #  print(7*i,end=" ")


# Python program to find the largest
# number among the three numbers


def maximum(a, b, c):
    if (a > b) and (a > c):
        largest = a
    elif (b > a) and (b > c):
        largest = b
    else:
        largest = c
    return largest

a = 1009
b = 9
c = 123
print(maximum(a, b, c))


git config --global user.name 'Irina Cherkaska'
git config --global user.email amadare55555@gmail.com

