# Lambda function is a small anonymous function without a name.
# It can take any number of arguments, but can only have one expression.
# Lambda function is similar to anonymous functions in JavaScript.
# We need it when we want to write an anonymous function inside another
# function.

print((lambda a, b: a * b)(4,6))

square = lambda x : x ** 2
print(square(5))

multi_variable = lambda a, b, c : a ** 2 + b ** 2 + c ** 2
print(multi_variable(3, 4, 5))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)
