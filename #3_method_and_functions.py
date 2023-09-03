print('\n<Python Documentation>\n')
list_1 = [1, 2, 3, 4]
print('*Example to know documentation of a function is: ', help(list_1.pop))
print('*It can be read in the next link: https://docs.python.org/')
print('\n<Functions>\n')
print('* Basic function structure is : ', end="")


def name_of_function(name):
    """
    Docstring explains function
    """
    return "Hello " + name


print(name_of_function('Ivan'))
print('* Example of function #1: ', end="")


def tell_age(age='None'):
    print(f'Your age is {age}.')


tell_age(19)

print('* Example of example #2 is: ', end="")


def even_check(num):
    return num % 2 == 0


print(even_check(8))
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = []

print('* Example of example #3 : ', end="")


def check_even_list(num_list):
    for check_number in num_list:
        if check_number % 2 == 0:
            list_3.append(check_number)
    return list_3


print(check_even_list(list_2))

print('\n<Unpacking tuples with functions>\n')
print("* Example can be = ", end="")
work_hours = [('Juan', 20), ('Laura', 40), ('Carla', 10)]


def employee_check(work_hours_tuple):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours_tuple:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    # Return
    return employee_of_month, current_max


person = employee_check(work_hours)
person_name, person_work_hours = employee_check(work_hours)

print(
    f'The employee of the month is {person_name}, and he/she worked along {person_work_hours} hours, the tuple form is : ',
    person)
print('\n<Interactions between functions>\n')
print('* Here we can see the interaction between functions : ', end="")
list_4 = [1, 2, 3, 4, 5]
from random import shuffle


def shuffle_list(list_to_shuffle):
    shuffle(list_to_shuffle)
    return list_to_shuffle


list_5 = shuffle_list(list_4)
print(list_5)
print('* A simple game with functions interactions: ', end="")


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number (between 0, 1, or 2): ")  # Input always return a string.
    return int(guess)


def check_guess(list_to_check, guess):
    if list_to_check[guess] == 'O':
        print('¡Correct answer!')
    else:
        print('¡Wrong answer! ', end="")
        print(list_to_check)


#  Initial list
list_6 = [' ', 'O', ' ']
#  Shuffle list
list_7 = shuffle_list(list_6)
# User guess
index_1 = player_guess()
# Check guess
check_guess(list_7, index_1)
print('\n<*args and **kwargs>\n')
print('* (*args) This is to use unlimited amount of parameters : ', end="")


def function_1(*args):
    return sum(args) * 0.05


print(function_1(1, 2, 3, 4, 5, 6))
print('* (**kwargs) difference between (*args) is that returns a dictionary, like : ', end="")


def function_2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here. :C')


function_2(fruit='Apple', veggie='lettuce')
print('* Also it can mix the two types of args format, like : ', end="")


def function_3(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


function_3(10, 20, 30, fruit='peach', food='eggs', animal='dog')
print('\n<Lambda expressions Map and Filter>\n')
print('* First we check the map function : ', end="")


# Is important that the function arg into the map function is without the '()'
# Map function means that the function will be applied to all elements in a list.


def square(num):
    return num ** 2


list_8 = [1, 2, 3, 4, 5]
list_9 = list(map(square, list_8))
print(list_9)
print('* Map function #2 : ', end="")
list_10 = ['Carlos', 'Valentina', 'Camila']


def splicer(string_1):
    if len(string_1) % 2 == 0:
        return 'EVEN'
    else:
        return string_1[0]


list_11 = list(map(splicer, list_10))
print(list_11)
print('* Now we check the filter function : ', end="")


# Returns iterator when the function passed is true or not


def check_even(num):
    return num % 2 == 0


list_12 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(check_even, list_12)))
print('* We checked lambda function : ', end="")


# We use lambda when the function is used only one time, also called like no-function form.


def square(num):
    return num ** 2


print(list(map(lambda num: num ** 2, list_12)))
print('\n<Nested Statements and scope>\n')
print('We need to have present the L - E - G - B rule.')
# (1) L: local -> variable assigned into a function that not is global in the same function.
# (2) Enclosing -> Function inside another function variables.
# (3) G: Global -> Names assigned in top-level of the file.
# (4) Built-in -> Python preassigned words.

print('* Example of level jerarqui of : ')
name = 'THIS IS A GLOBAL STRING'  # -> ¡ this is a global variable !

def greet():
    name = 'Sammy' #  -> ¡ this is an enclosing variable !

    def hello():
        #  -> ¡ this is a local variable !
        print('Hello ' + name)
    hello()


print('* Global reserved word search along all the program to find a word that have assigment the same word, like : ', end="")
x = 50


def function_4():
    global x
    print(f'is {x}')
    # ¡LOCAL REASSIGNMENT ON GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL TO X TO {x}')
    return x


x = function_4()
print(x)
