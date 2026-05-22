#create a calculator to evaluate simple interest

def si(p , r, t):
    return (p*r*t)/100

p = int(input())
r = int(input())
t = int(input())

print(si(p,r,t))