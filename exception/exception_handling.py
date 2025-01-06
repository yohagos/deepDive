# Python uses try and except to handle errors gracefully.
# A graceful exit (or graceful handling) of errors is a simple
# programming idiom - a program detects a serious error condition
# and "exits gracefully", in a controlled manner as a result.
# Often the program prints a descriptive error message to a terminal
# or log as part of the graceful exit, this makes our application
# more robust. The cause of an exception is often external to the
# program itself. An example of exceptions could be an incorrect input,
# wrong file name, unable to find a file, a malfunctioning IO device.
# Graceful handling of errors prevents our applications from crashing.

# try:
#     print(10 + '5')
# except:
#     print('Something went wrong')
#
#
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2025 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except:
#     print('Something went wrong')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')
#
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


# def sum_of_five_nums(a,b,c,d,e):
#     return a + b + c +d + e
#
# lst = [1,4,3,6,8]
# print(sum_of_five_nums(*lst))
#
#
# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]
#
#
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
#
#
# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

#
# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7))
#
# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
#     # Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs
#
# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))
#
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


for index, item in enumerate([20, 30, 40]):
    print(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
