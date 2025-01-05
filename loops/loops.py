# while loops

# count = 0
# while count < 5 :
#     print(count)
#     count = count + 1
# else:
#     print(f'Count equals or is bigger than 5')


# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1
    # if count == 3:
    #     break

# for loop

# language = 'Python'
# for letter in language:
#     print(letter)
#
# for i in range(len(language)):
#     print(i)

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for key in person:
#     print(key)
#
# for key, value in person.items():
#     print(key, value) # this way we get both keys and values printed out

# numbers = (0,1,2,3,4,5,6)
# for num in numbers:
#     print(num)
#     if num == 3:
#         break
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')


# Range function

# lst = list(range(10))
# print(lst)
#
# st = set(range(1,11))
# print(st)
#
# lst = list(range(0,11,2))
# print(lst) # [0, 2, 4, 6, 8, 10]
# st = set(range(0,11,2))
# print(st) #  {0, 2, 4, 6, 8, 10}

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)
#
# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11
# else:
#     print('The loop stops at', number)

# hashtag = '#'
# steps = input('enter how many iteration you want : ')
# print('Steps you choose => ', steps)
# line = ''
# if steps.isnumeric():
#     number = int(steps)
#     for step in range(number):
#         line += hashtag
#         print(line)

# symbol = '# '
# for col in range(9):
#     line = ''
#     for row in range(9):
#         line += symbol
#     print(line)
