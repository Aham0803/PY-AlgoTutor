# convert keys to uppercase

dict = {'a' : 1 , 'b':2}

dict1 ={k.upper(): v for k, v in dict.items()}
print(dict1)