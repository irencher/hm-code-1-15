from datetime import datetime


def task1():
    name = 'Ira'
    day = datetime.now().date()

    print('Hello {name}. Today is {day}'.format(name=name, day=day))
    print(f'Hello {name}. Today is {day}')
    print('Hello %s. Today is %s' % (name, day))


def task1_v1():
    name = 'Ira'
    day = 'today'
    print('Hello,', name)
    print(day, 'a good one day')

def task2_v1():
    first_name = 'Ira'
    last_name = 'Cher'
    name = first_name + " " + last_name
    print('Hello', name + '. Meow-Meow, you?')

def calculate(a=55, b=5):
    print(f'variables: a={a}, b={b}')
    print('addition:', a + b)
    print('subtraction:', a - b)
    print('Division:', a / b)
    print('Multiplication:', a * b)
    print('Exponent (Power):', a ** b)
    print('Modulus:', a % b)
    print('Floor division:', a // b)



def get_two_numbers():
    a = input('Type a first number: ')
    b = input('Type a second number: ')
    return int(a), int(b)


numbers = get_two_numbers()
calculate(*numbers)
