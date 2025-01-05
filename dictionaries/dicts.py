# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

person = {
    'first_name':'Test',
    'last_name':'Test',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print('Person : ', person)
# print('Person length : ',len(person))
#
# print('Persons Age : ', person['age'])
# print('Persons Skills : ', person['skills'])
# print('Persons Skills (get) : ', person.get('skills'))
# print('Persons first Skill : ', person['skills'][0])

person['job_title'] = 'Freelancer'
person['skills'].append('Java')
print(person)

print('skills in person : ', 'skills' in person )
print('skillz in person : ', 'skillz' in person )

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('dct : ', dct)
dct.pop('key1') # removes key1 item
print('dct : ', dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
print('dct : ', dct)
del dct['key2'] # removes key2 item
print('dct : ', dct)

print('dct to list : ', dct.items())
# dct.keys() => list of all keys
# dct.values() => list of all values

# Removing Key and Value Pairs from a Dictionary

    #pop(key): removes the item with the specified key name:
    #popitem(): removes the last item
    #del: removes an item with specified key name

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
#     }
# person.pop('first_name')        # Removes the firstname item
# person.popitem()                # Removes the address item
# del person['is_married']        # Removes the is_married item
