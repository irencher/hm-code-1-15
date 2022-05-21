#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

import random
n = random.randrange(1, 10)
user_num = input('Please type ur number: ')
if user_num.isnumeric():
    user_num = int(user_num)
    if user_num <= 0 or user_num > 10:
        print('sorry')
    elif n == user_num:
        print('cool')
    else:
        print('meh')
else:
    print(user_num + ' is not a number')



#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”
name = input('Whats ur name: ')
birthday = int(input('How old a u now:  '))
print('Hello ' + name + ', on your next birthday you’ll be ' + str(birthday + 1) + ' years')


#Words combination
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
#'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
#Tips: Use random module to get random char from string)
import random
word = input('Please say smthng..')
for x in range(5):
    print(''.join(random.sample(word, len(word))))


#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
import random
#SquidGame - ну тому, що багато чисел і тому, що стало цікаво чи окей для пайтону бачити корейські символи (SquidGame - корейский серіал, оригинальна назва 오징어게임)
def 오징어게임():
    num_1 = random.randint(1, 9999)
    num_2 = random.randint(1, 9999)
    result = True
    question = 'What is ' + str(num_1) + ' + ' + str(num_2) + '? Ur answer: '
    answer = int(input(question))
    if answer != num_1 + num_2:
        result = False
    question = 'What is ' + str(num_1) + ' - ' + str(num_2) + '? Ur answer: '
    answer = int(input(question))
    if answer != num_1 - num_2:
        result = False
    question = 'What is ' + str(num_1) + ' ** ' + str(num_2) + '? Ur answer: '
    answer = int(input(question))
    if answer != num_1 ** num_2:
        result = False
    question = 'What is ' + str(num_1) + ' // ' + str(num_2) + '? Ur answer: '
    answer = int(input(question))
    if answer != num_1 // num_2:
        result = False
    print(result)
오징어게임()