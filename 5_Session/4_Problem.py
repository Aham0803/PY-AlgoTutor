# # to calculate number of uppercase and lowercase character.

# Line = " The quick Brown For jumps Over a Lazy Dog"

# n = len(Line)


# uppercase = 0
# lowercase = 0

# upperletter = ""
# lowerletter = ""
# for i in Line:
#     if i.isupper():
#         uppercase += 1
#         upperletter += i
#     elif i.islower():
#         lowercase += 1
#         lowerletter +=i

# print("number of uppercase is " ,uppercase)
# print("upperletters are : " ,upperletter)

# print("number of lowercase is " ,lowercase)
# print("lowerletters are : " ,lowerletter)


# another method using dictionary to solve this problemm
# method 2

sentence = " The quick Brown For jumps Over a Lazy Dog"
counts ={'upper' : 0 , 'lower' : 0}

for i in sentence:
    if i.isupper():
        counts['upper'] += 1
    elif i.islower():
        counts['lower'] += 1

print("number of uppercase is " ,counts['upper'])
print("number of uppercase is " ,counts['lower'])




