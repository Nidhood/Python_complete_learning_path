print("\n<Basic if statements structure>\n")
string_1 = 'Apple'
print("* Basic if / elif / else statement structure example : ", end="")
if string_1 == 'Pineapple':
    print("¡I like pineapples!")
elif string_1 == 'Apple':
    print("¡I like apples!")
else:
    print("I don't like fruits.")
print("\n<Basic for loops statements structure>\n")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("* Basic for loops structure example #1 : ", end="")
for i in list_1:
    if i % 2 == 0:
        if i is len(list_1):
            print(i, " is a odd number!.")
        else:
            print(i, " is a odd number!, ", end="")
    else:
        print(i, " is not a odd number!, ", end="")
print("* Basic for loops structure example #2 : ", end="")
string_2 = 'Hello world!'
for letter in string_2:
    if letter is string_2[-1]:
        print("'", letter, "'.")
    else:
        print("'", letter, "',", end="")
print("* For loops can be used to unpack tuples like : ", end="")
tuple_1 = (1, 2, 3)
for item in tuple_1:
    if item is len(tuple_1):
        print(item, ".")
    else:
        print(item, ", ", end="")
print("* Another way to unpack tuples : ", end="")
tuple_2 = [(1, 2), (3, 4), (5, 6), (7, 8)]
for element in tuple_2:
    if element is tuple_2[-1]:
        print(element, ".", " and,  ", end="")
    else:
        print(element, ", ", end="")
for (a, b) in tuple_2:
    if a is tuple_2[-1][0] or b is tuple_2[-1][1]:
        print(a, "-", b, ".")
    else:
        print(a, "-", b, ", ", end="")
print("* For loops can be use also to unpack dictionaries elements like : ", end="")
dictionary_1 = {'k1': 1, 'k2': 2, 'k3': 3}
for item in dictionary_1.items():
    if item == list(dictionary_1.keys())[-1] or item == list(dictionary_1.values())[-1] or item == \
            list(dictionary_1.items())[-1]:
        print(item, ".")
    else:
        print(item, ", ", end="")
print("\n<Basic while statements structure>\n")
print("* Basic while structure example : ", end="")
x = 0
while x < 5:
    if x == 4:
        print(f'The current value of x is {x + 1}', ".")
    else:
        print(f'The current value of x is {x + 1}', ", ", end="")
    x += 1
# Important for loop flow control:
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the  closest enclosing loop.
# pass: Does nothing at all.
print("\n<Control flow in loops reserved words>\n")
print("* Next we use control flow in the loop : ", end="")
list_2 = [1, 2, 3]
for item in list_2:
    pass  # Here we use pass when actually we don't want to do anything into the loop.
string_3 = "¡Hey i'm% using python!"
for letter in string_3:
    if letter == '%':
        continue  # Here we use continue when we want to ignore some element but doesn't cut the flow loop.
    print(letter, end="")
print(", and ", end="")
for letter in string_3:
    if letter == '%':
        break  # Here we use break when we want stop right now the flow.
    print(letter, end="")
print("\n\n<Usefully operators in loops>\n")
print("* Range is a powerfully operator that allows to make loops and other things very easy, like : ", end="")
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in range(0, 10, 2):
    if num == 8:
        print(num, ".")
    else:
        print(num, ", ", end="")
print("* Easiest way to create numeric lists : ", end="")
print(list(range(0, 10, 2)))
print("* Counters are important to the programming logic : ", end="")
counter_1 = 0
for letter in 'abcde':
    if letter == 'e':
        print('At index {} the letter is {}.'.format(counter_1, letter))
    else:
        print('At index {} the letter is {}, '.format(counter_1, letter), end="")
    counter_1 += 1
print("* Another form to go through a loop is : ", end="")
string_4 = 'abcde'
for index, letter in enumerate(string_4):
    if index == 4:
        print(index, "-", letter, ".")
    else:
        print(index, "-", letter, ",", end="")
print("* Usefully method to combine two lists and make a tuple is : ", end="")
list_4 = [1, 2, 3, 4, 5]
list_5 = ['a', 'b', 'c', 'd', 'e']
list_6 = [100, 200, 300]
for item in zip(list_4, list_5):
    print(item, ", ", end="")
print("\n* Easiest form to create lists of mixed lists : ", list(zip(list_4, list_5, list_6)))  # Hint: like you can
# see here the element after the third element are ignored, that's because zip method only applies to equal number of
# items in each list that is mixed.
print("* First example of imports from a library : ", end="")
from random import shuffle, randint
list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(list_7)  # The function doesn't return anything!
print(list_7, ", and ", end="")
random_1 = randint(0, 100)
print(random_1)
print("\n<I/O flow>\n")
print("* Basic I/O examples, ", end="")
input_1 = input('Enter a number here: ')
print("Your answer is = ", input_1)
print("\n<Efficient way to create lists>\n")
print("* Example #1 : ", end="")
string_5 = '¡Hell yeah!'
list_8 = [letter for letter in string_5]
print(list_8)
print("* Example #2 : ", end="")
list_9 = [num for num in range(0, 10) if num % 2 == 0]
print(list_9)
print("* Example #3 : ", end="")
celcius = [0, 10, 20, 34.5]
fahernheit = [((9/5)*temp + 32) for temp in celcius]
print(fahernheit)
print("* Example #4 : ", end="")
list_10 = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(list_10)
print("* Example #5 : ", end="")
list_11 = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
print(list_11)
