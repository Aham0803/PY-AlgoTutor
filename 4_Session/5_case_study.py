# i want to build a timer applications with a count down feature . WAP for it which gives value after every second
# execute a block of code which runs after every second

import time

def timer(seconds):
    for i in range(seconds , 0 , -1):
        print(i)
        time.sleep(1)
    print("happy new year")

timer(5)