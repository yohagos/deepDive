# Classes and Objects

# Python is an object-oriented programming language. Everything in Python is an object,
# with its properties and methods. A number, string, list, dictionary, tuple, set etc.
# used in a program is an object of a corresponding built-in class. We create class to
# create an object. A class is like an object constructor, or a "blueprint" for creating
# objects. We instantiate a class to create an object. The class defines attributes and
# the behavior of the object, while the object, on the other hand, represents the class.
#
# We have been working with classes and objects right from the beginning of this challenge
# unknowingly. Every element in a Python program is an object of a class. Let us check if
# everything in python is a class:

# num = 10
# print(type(num))
#
# sg = 'string'
# print(type(sg))
#
# st = set()
# print(type(st))

#       <class 'int'>
#       <class 'str'>
#       <class 'set'>

# class Person:
#     pass
#
# print('Class : ',Person)
#
# p = Person()
# print('Instance : ', p)
#
#       Class :  <class '__main__.Person'>
#       Instance :  <__main__.Person object at 0x000001D9D7037CB0>

class Person:
    def __init__(self, name):
        self.name = name

p = Person('Yosef')
print(p)
print(p.name)

class PersonTwo:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def person_info(self):
        return f'My Name is {self.firstname} {self.lastname} and am {self.age} years old'

p2 = PersonTwo('Yosef', 'H', 35)
print(p2.firstname)
print(p2.person_info())

class PersonThree:
    def __init__(self, firstname='Yosef', lastname='H', age=35):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def person_info(self):
        return f'My Name is {self.firstname} {self.lastname} and am {self.age} years old'

# p3 = PersonThree()
# print(p3.firstname)
# print(p3.person_info())
#
# p4 = PersonThree('James', 'H', 123)
# print(p4.firstname)
# print(p4.person_info())


class PersonFour:
    def __init__(self, firstname='Yosef', lastname='H', age=35):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.skills = []

    def person_info(self):
        return f'My Name is {self.firstname} {self.lastname} and am {self.age} years old'

    def add_skill(self, skill):
        self.skills.append(skill)

p5 = PersonFour()
p5.add_skill('Python')
p5.add_skill('Java')
p5.add_skill('Go')
p5.add_skill('Angular')
print(p5.person_info())
print(p5.skills)

class Student(PersonFour):
    def __init__(self, firstname = 'St', lastname = 'U', age = 10, gender = 'M'):
        self.gender = gender
        super().__init__(firstname, lastname, age)
    def person_info(self):
        gender = 'He' if self.gender == 'M' else 'She'
        return f'{self.firstname}  -  {self.lastname}  -  {self.age}  -  {self.gender}'

s1 = Student()
s1.add_skill('Flutter')
s1.add_skill('JavaScript')
print(s1.person_info())
print(s1.skills)
