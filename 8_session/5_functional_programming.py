# ## pure functions defination

# def pure_func(list):
#     New_list = []
#     for i in list:
#         New_list.append(i*2)
#     return New_list

# my_list = [1,2,3,4]
# modified_list = pure_func(my_list)
# print(modified_list)

# # recursion in functional programming
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

# # functions are first class citizens in python
# def shout(text):
#     return text.upper() + "!!!"
# def whisper(text):
#     return text.lower() +"..."
# def greet(func): # func value is used as a parameter to pass the function as an argument
#     greeting = func("Hello , World")
#     print(greeting)

# greet(shout)
# greet(whisper)

# #imp prop ->
# # a function is an instance of object type
# # you can store the function in a variable
# # you can pass the function as an argument to another function
# # you can return a fuunction from another function
# # you can store functions in data strcutures such as lists , disctionaries etc

# ## built in higher order functions in python

# # map function

# def addition(n):
#     return n+n

# numbers = [1,2,3,4,5]
# result = map(addition, numbers)

# print(result)

# for x in result:
#     print(x)



# filter function
## the filter function is used to filter the elements of a sequence bsed on given condistion. it takes two arguments : a function that defines the condition and an itreable (like a list) to be filtered .
# the function should return true for elements that should be included in the result and false for thouse that should be excluded

def fun(n):
    letters = ['a','e','i','o','u']
    if n in letters:
        return True
    else:
        return False
    
sequence = ['a','b','c','d','e','f']
filtered_sequence = filter(fun,sequence)
print(type(filtered_sequence))
for x in filtered_sequence:
    print(x)


## lambbda function

lambda_func = lambda x:x*2 ## lambda arguments:expression
print(lambda_func(5))