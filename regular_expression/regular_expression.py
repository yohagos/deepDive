# Regular Expressions

# A regular expression or RegEx is a special text string that helps to find
# patterns in data. A RegEx can be used to check if some pattern exists in
# a different data type. To use RegEx in python first we should import the
# RegEx module which is called re.


# Methods in re Module
#
# To find a pattern we use different set of re character sets that allows to search for a match in a string.
#
#     re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
#     re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
#     re.findall: Returns a list containing all matches
#     re.split: Takes a string, splits it at the match points, returns a list
#     re.sub: Replaces one or many matches within a string

import re

# txt = 'I love to teach python and javaScript'
# # It returns an object with span, and match
# match = re.match('I love to teach', txt, re.I)
# print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (0, 15)
# # Let's find the start and stop position from the span
# start, end = span
# print(start, end)  # 0, 15
# substring = txt[start:end]
# print(substring)       # I love to teach
#
# match = re.match('I like to teach', txt, re.I)
# print(match) # None

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''
#
# # It returns an object with span and match
# match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (100, 105)
# # Let's find the start and stop position from the span
# start, end = span
# print(start, end)  # 100 105
# substring = txt[start:end]
# print(substring)       # first


#txt = '''Python is the most beautiful language that a human being has ever created.
#I recommend python for a first programming language'''

# # It returns a list
# matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']
#
# matches = re.findall('python', txt, re.I)
# print(matches)  # ['Python', 'python']
#
# matches = re.findall('Python|python', txt)
# print(matches)  # ['Python', 'python']
#
#
# matches = re.findall('[Pp]ython', txt)
# print(matches)  # ['Python', 'python']

# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# # OR
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
#
# matches = re.sub('%', '', txt)
# print(matches)

# txt = '''I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?'''
# print(re.split('\n', txt)) # splitting using \n - end of line symbol

# regex_pattern = r'apple'
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['apple']
#
# # To make case insensitive adding flag '
# matches = re.findall(regex_pattern, txt, re.I)
# print(matches)  # ['Apple', 'apple']
# # or we can use a set of characters method
# regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']

#
#     - '[]': A set of characters
#         [a-c] means, a or b or c
#         [a-z] means, any letter from a to z
#         [A-Z] means, any character from A to Z
#         [0-3] means, 0 or 1 or 2 or 3
#         [0-9] means any number from 0 to 9
#         [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
#
#     - '\' : uses to escape special characters
#         \d means: match where the string contains digits (numbers from 0-9)
#         \D means: match where the string does not contain digits
#     - '.' : any character except new line character(\n)
#     - '^': starts with
#         r'^substring' eg r'^love', a sentence that starts with a word love
#         r'[^abc] means not a, not b, not c.
#     - '$': ends with
#         r'substring$' eg r'love$', sentence that ends with a word love
#     - '*': zero or more times
#         r'[a]*' means a optional or it can occur many times.
#     - '+': one or more times
#         r'[a]+' means at least once (or more)
#     - '?': zero or one time
#         r'[a]?' means zero times or once
#     - '{3}': Exactly 3 characters
#     - '{3,}': At least 3 characters
#     - '{3,8}': 3 to 8 characters
#     - '|': Either or
#         r'apple|banana' means either apple or a banana
#     - '()': Capture and group

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']


regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']


regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
