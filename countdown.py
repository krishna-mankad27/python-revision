import time as T
t = int(input("enter time in seconds : "))
while t >= 0:
    s = int(t%60)
    m = int((t/60))%60
    h = int((t/3600))%24
    d = int(t/86400)
    print(f"{d:02}:{h:02}:{m:02}:{s:02}")
    T.sleep(1)
    t -= 1