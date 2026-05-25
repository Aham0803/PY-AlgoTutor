#method 1
li = [1,2,3,4,5]
li.reverse()
print(li)

#method 2
a = [10,20,30,40,50]
rev = list(reversed(a))
print(rev)

# method 3
b = [10,20,30,40,50]
rever = b[::-1]
print(rever)

#method 4
c = [2,4,6,8]
i , j = 0 , len(c)-1
while i < j:
    c[i],c[j] = c[j] , c[i]
    i += 1
    j -= 1

print(c)