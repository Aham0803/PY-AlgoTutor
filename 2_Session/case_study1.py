# A person requires at least 80% of marks to be qualified for test for pyscial assessment
# conditon -> if he is a sportsperson then the qualification marks are 75%
# declare a global variable which stores the marks
# WAF to check whether a person is from sports quaota or not
# if sports === true :
#      print("new quaifying marks are 75")
# else:
#      print("qualifying marks are 80")

marks = 80
def calculate_quota(total_marks):
    global sports
    sports = True
    if sports == True:
        return "sports quota is applicable . And your new qualifying marks are 75"
    else :
        return "sports quota is not applicable."

# calculate_quota(marks)
print(f'your total marks are {marks} , your status is {calculate_quota(marks)} and your sports quota status is {sports}')