# creating a group with 5 friends for participating in smart india hackathon
#  cond 1 -> age > 18
#  cond 2 -> at least one female member
# WAP to address this scenario
#  friends = [ '', '', '']
#   Gender = ['','','']
# if condition is true then print(" you team is sucessfully") else print("not")


friends = ['aham', 'divyam' , 'madhav' , 'ritik']
gender = ["male" , "male" , "male" , "Female"]
age = [18 , 20 , 30 , 19]
if "Female" in gender and  any(a > 18 for a in age):
    print("your team can participate")
else:
    print("not participate")