import datetime
date = datetime.date(2025,9,7)
today = datetime.date.today()
time = datetime.time(13,17,16)
time_now = datetime.datetime.now()
#time_now  = time_now.strftime("%m-%d-%y %H:%M:%S")
print("...",time_now,"...")
target_time = datetime.datetime(2021,12,31,11,59,59,999999)
print(target_time)
if target_time < time_now:
    print("target date has passed...")
else:
    print("target date has not passed...")
