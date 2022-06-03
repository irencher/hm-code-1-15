# Write a Python program to detect the number of local variables declared in a function.

def count_local_variables():
    a = 1
    b = "2"
    c = 3
    print(len(dir()))


count_local_variables()


# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def multiply_by(x: int):
    def fun(y: int):
        return x * y

    return fun


fun_by_2 = multiply_by(2)
num = input("Please enter one num: ")
print("Your number multiplyed by 2: ", fun_by_2(int(num)))
