from pprint import pprint

# fruits = ['banana', 'orange', 'mango', 'lemon']
# pprint(fruits)

# random_list = [10, 42.34, "Hello", {"test", "yosef"}]
# pprint(random_list)
# pprint(random_list[-1])

# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana', 'orange', 'mango', 'lemon']
# banana, orange, mango, lemon, *rest = fruits
# pprint(f"Banana = {banana}, Orange = {orange}, Mango = {mango}, Lemon = {lemon}")
# pprint(f"Rest (length: {len(rest)} = {rest}")
#
# half_fruits = fruits[::2]
# pprint(half_fruits)

# fruits = ['banana', 'orange']
# banana_in_fruits = 'banana' in fruits
# print(f'Banana in Fruits : {banana_in_fruits}')
# apple_in_fruits = 'apple' in fruits
# print(f'Apple in Fruits : {apple_in_fruits}')

# fruits = ['banana', 'orange', 'mango']
# print(fruits)
# fruits.append('apple')
# print(fruits)
# fruits.append('tomato')
# print(fruits)
#
# fruits.remove('tomato')
# print(fruits)
# fruits.pop(2)
# print(fruits)

# del fruits[2] # removes index 2
# del fruits # removes the whole list, therefore 'fruits' cannot be used anymore

cars = ['Audi', 'Benz', 'BMW', 'Opel']
bikes = ['Harley', 'Yamaha', 'Toyota']
# cars_copy = cars.copy()
# cars_copy.clear()
# print(cars)
# print(cars_copy)

cars_plus_bikes = cars + bikes
print(cars_plus_bikes)
bikes.extend(cars)
print(bikes)

# sort will sort the original list into alphabetical order
# bikes.sort()
# print(bikes)
# bikes.sort(reverse=True)
# print(bikes)

# sorted() or sorted(list, reserve=True) will sort the returned value, but does not manipulate the original list

language = 'Python'
lst = [i for i in language]
print(lst)

squares = [i * i for i in range(11)]
print(squares)

even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)
