# a = [0,1,2,3,4,5]
# for n in a:
#     print(n)

# set = set(a) # here we can convert list to a set
# print(type(a))

# b = set("Gaurav") # converting string to set
# print(b)

# another way to iterate  in set is enumerate()
# enumerate() -> a built in tool used over an iterable (like a list , tuple or string) while keeping track of both the index and the value of each item

# num_set = {1,2,3,4}
# for value , char in enumerate(num_set):
#     print(char , end = " ")

# a  = set()
# a.add("Gaurav") ## add -> adds element to set
# print(a)

# a.update(["shyam" , "Radha" , "aham"]) ## adding multiple item to set
# print(a)

# b = set([0,1,2,3,4])
# print(b)
# b.pop() # Removing random element from set
# print(b)
# b.remove(2) # removing specific element from set
# print(b)
# b.discard(3) # removing specific element but if elements not present than it will not raise error
# print(b)

# remove every element in the set
# a = set([1,2,3,4,5])
# a.clear()
# print(a)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2) #union of set1 and set 2
print( set1 & set2) # Intersection of set1 and set2
print(set1 - set2) # Diffrence of set1 and set 2

# for symmetric elements a-(a&b) + b-(a&b)
# symmetric elements are those which are not common in a and b . it is represented by ^ 