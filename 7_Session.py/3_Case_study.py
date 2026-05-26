# write a program to sort (ascending or decending) a dictionary by value 
def sort_dict(d , reverse = False):
    return dict(sorted(d.items() , key = lambda x : x[1] , reverse = reverse))

d = {"red": 1 , "Green" : 5 , "Blue" : 2 , "Black" : 3 , "white" : 4}

sorted_color = sort_dict(d)
print (sorted_color)
