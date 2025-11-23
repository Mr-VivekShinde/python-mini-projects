import time
print("set your own countdown timer")
set_time=int(input("Enter time in seconds :"))
for i in range(set_time,0,-1):
    hour=int(i/3600)
    min=int(i/60) % 60
    sec=int(i%60)
    
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("TIMES'S UP!")