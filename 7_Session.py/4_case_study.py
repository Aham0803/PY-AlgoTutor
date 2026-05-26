# merging two dictionaries

# d1 = {'a' : 1000 , 'b' : 2000}
# d2 = {'x' : 3000 , 'y' : 4000}

# d = d1.copy()
# d.update(d2)
# print(d)

# methood 2
def merge_dict(*dicts):
    result = dict()
    for d in dicts:
        result.update(d)
    return result

d1 = {'a' : 1000 , 'b' : 2000}
d2 = {'x' : 3000 , 'y' : 4000}

print(merge_dict(d1,d2))


