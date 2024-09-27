import os
import time

x = 3+5j
y = 1-2j
z = x + y

print(z)

def loop_loco():
    for i in range(10):
        os.system('clear')
        for j in range(i):
            print(" " * j, end="")
            print("*" * (10 - j))
        print("")
        time.sleep(0.1)

loop_loco()