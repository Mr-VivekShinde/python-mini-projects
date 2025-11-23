import time
set_time=int(input("Enter time in seconds :"))
for i in range(set_time,0,-1):
    print(i)
    time.sleep(1)
print("TIMES'S UP!")