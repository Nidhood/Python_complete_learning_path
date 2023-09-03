print('\n<Programming Orientated to Objects>\n')
print('* Basic syntax of POO : ', end="")


class Name_of_class:
    def __int__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)


lista_1 = [1, 2, 3]
set_1 = set()


class Dog:
    #  Class object attribute.
    #  Same for any intense of a class.
    species = 'mammal'

    def __init__(self, breed, name,
                 spots):  # Init method, means a method that call the same name of the class constructor
        #  Attributes:
        #  Expects String:
        self.breed = breed
        #  Expects String:
        self.name = name
        #  Expects boolean True/False:
        self.spots = spots

    # Methods:
    def bark(self, age):
        print('¡WOFF! My name is {} and I have {} years old.'.format(self.name, age))


# Create an instance of 'Dog':
instance_1 = Dog('Lab', 'Rocky', True)
print(f"Dog breed is {instance_1.breed}, dog name is {instance_1.name}, spots of the dog is {instance_1.spots} "
      f"and the dog specie is {instance_1.species}. The bark of the dog is ", end="")
instance_1.bark(5)

print("* POO example : ", end="")


class Circle:
    # Class object attribute:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


# Create an instance of 'Circle':
instance_2 = Circle(30)
print(f"The circumference of the circle is {instance_2.get_circumference()} and his area is {instance_2.area}")
print('\n<Inheritance>\n')


class Animal:
    def __init__(self):
        print("¡Animal created!")

    def who_am_i(self):
        print("¡I am an animal!")

    def eat(self):
        print("¡I'm eating!")


instance_3 = Animal()


# Inheritance
class Dog_inherited(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("¡Dog created!")

    # Overwrite of methods
    def who_am_i(self):
        print("¡I am a dog!")

    # Overwrite of methods
    def eat(self):
        print("¡I'm eating!")

    def bark(self):
        print("¡WOOF!")


instance_4 = Dog_inherited()
instance_4.who_am_i()
instance_4.bark()
instance_4.eat()

print('\n<Polymorphism>\n')


#  Refers the way how classes can share the same method


class Dog_polymorphism_1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "¡" + self.name + " says woof!"


class Cat_polymorphism_1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "¡" + self.name + "says meow!"


instance_5 = Dog_polymorphism_1("Rocky")
instance_6 = Cat_polymorphism_1("Kira")

print(instance_5.speak())
print(instance_6.speak())
for pet_class in [instance_5, instance_6]:
    print(type(pet_class))
    print(type(pet_class.speak()))


def pet_speak(pet):
    print(pet.speak())


# Polymorphism:
pet_speak(instance_5)
pet_speak(instance_6)


class Animal_polymorphism:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("¡Subclass must implement this abstract method!")


class Dog_polymorphism_2(Animal_polymorphism):
    def speak(self):
        return "¡" + self.name + "says woof!"


class Cat_polymorphism_2(Animal_polymorphism):
    def speak(self):
        return "¡" + self.name + "says meow!"


instance_7 = Dog_polymorphism_2("Fido")
instance_8 = Cat_polymorphism_2("Isis")

print(instance_7.speak())
print(instance_8.speak())
print('\n<Magic/Dunder>\n')
# Are called Magic or Dunder methods because they use double underscore characters.
lista_2 = [1, 2, 3]


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # ToString method
    def __str__(self):
        return f"{self.title} by {self.author}."

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"¡A book object '{self.title}' has been deleted!")


instance_9 = Book('Machine learning', 'Anonymous', 200)
print(instance_9)
print(len(instance_9))
# Remove some instance from the memory of the computer:
# del instance_9
del instance_9
