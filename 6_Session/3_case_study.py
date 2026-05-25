# we have a visitor list and subscriber list . now we have to find out the number of customer from subscriber list who has visited my shop

visitor_list = set(["gaurav" , "shyam" , "radha" , "kanha"])
subscriber_list = set(["krishna" , "shyam" , "radha" , "kanhaiya"])
print(visitor_list | subscriber_list)
print(visitor_list & subscriber_list)
print (visitor_list - subscriber_list)
print (visitor_list ^ subscriber_list)