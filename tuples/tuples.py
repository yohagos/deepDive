# tuples are a collection of different data types, which is ordered and immutable

empty_tuple = ()
print(empty_tuple)

tpl = (5, 14, 2, 17, 32)
print(tpl)
first_item = tpl[0]
print(first_item)

middle_items = tpl[1:4]
print(middle_items)

lst = list(tpl)
print(lst)

print(14 in tpl)

tpl2 = (123, 432, 223, 987)
tpl_tpl2 = tpl + tpl2
print(tpl_tpl2)

# del tpl2 will delete the tuple
