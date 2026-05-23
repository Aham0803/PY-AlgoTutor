import time

def start_counter(seconds,delay = 1):
    for i in range(1,seconds + 1):
        print("Counter is at:" , i)
        time.sleep(delay)
    print("counter finished!")

start_counter(5,delay = 1)