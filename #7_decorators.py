print("\n<Decorators>\n")


def function_1(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\tThis is the greet() function inside hello!'

    def welcome():
        return '\t\tThis is welcome() inside hello!'

    print('I am going to print a function!')

    if name == 'Jose':
        return greet()
    else:
        return welcome()


my_new_func = function_1('Camille')

print(my_new_func)


def hello():
    return 'Hi Jose!'


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello)

print("* We now are be able to create decorators: ", end="")


def new_decorator(original_function):
    def wrap_function():
        print('Some extra code before the original function!')
        original_function()
        print('Some extra code, after the original function!')

    return wrap_function


@new_decorator
def function_needs_decorator():
    print("I want to be decorated!")


decorator_function = new_decorator(function_needs_decorator)
decorator_function()
