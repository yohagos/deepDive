# File Handling

# So far we have seen different Python data types. We usually store our data in
# different file formats. In addition to handling files, we will also see different
# file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let
# us get familiar with handling files with common file format(.txt).
#
# File handling is an import part of programming which allows us to create, read,
# update and delete files. In Python to handle data we use open() built-in function.


# f = open('example.txt')
# print(f)

# Opening Files for Reading
# The default mode of open is reading, so we do not have to specify 'r' or 'rt'.
# I have created and saved a file named reading_file_example.txt in the files
# directory. Let us see how it is done:

## Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
#
#     "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
#     "a" - Append - Opens a file for appending, creates the file if it does not exist
#     "w" - Write - Opens a file for writing, creates the file if it does not exist
#     "x" - Create - Creates the specified file, returns an error if the file exists
#     "t" - Text - Default value. Text mode
#     "b" - Binary - Binary mode (e.g. images)

# As you can see in the example above, I printed the opened file and it gave some
# information about it. Opened file has different reading methods: read(), readline,
# readlines. An opened file has to be closed with close() method.
#
#     read(): read the whole text as string. If we want to limit the number
#     of characters we want to read, we can limit it by passing int value to the
#     read(number) method.

# f = open('example.txt')
# # txt = f.read()
# # print(type(txt))
# # print(txt)
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# After we open a file, we should close it. There is a high tendency of forgetting to
# close them. There is a new way of opening files using with - closes the files by
# itself. Let us rewrite the the previous example with the with method:

# with open('example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# with open('example.txt','a') as f:
#     f.write('This text has to be appended at the end')

# with open('writing_file_example.txt','w') as f:
#     f.write('This text will be written in a newly created file')

# import os
# os.remove('writing_file_example.txt')


# import os
# if os.path.exists('writing_file_example.txt'):
#     os.remove('writing_file_example.txt')
# else:
#     print('The file does not exist')

# import json
#
# # dictionary
# person= {
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }
# # JSON: A string form a dictionary
# person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
#
# # we use three quotes and make it multiple line to make it more readable
# person_json = '''{
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }'''
#
# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])
#
# person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
# print(type(person_json))
# print(person_json)
#
# with open('json_example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)


# import csv
#
# with open('csv_example.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#             line_count += 1
#     print(f'Number of lines:  {line_count}')


# import xlrd
#
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names())


import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


