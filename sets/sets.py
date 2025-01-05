# Set is a collection of unordered and un-indexed distinct elements

st = {'item1', 'item2', 'item3', 'item4'}
print(st)
st.add('item10')
print(st)
st.update(['item5','item6','item7'])
print(st)

st.remove('item6')
print(st)

remove_item = st.pop()
print(remove_item)

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)

# joining sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item10', 'item20', 'item30'}
st3 = st1.union(st2)
print(st3)

st1.update(st2)
print(st1)

set1 = {'item1', 'item2', 'item3', 'item4', 'item5'}
set2 = {'item1', 'item4'}
print('Intersection : ', set1.intersection(set2))
print('Is Sub Set : ', set2.issubset(set1))
print('Is Supper Set : ', set1.issuperset(set2))
print('Differences : ', set1.difference(set2))
print('Symmetric Differences : ', set1.symmetric_difference(set2))

# if two sets do not have a common (same) item, we call them disjoint sets. with isdisjoint we can check this
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


