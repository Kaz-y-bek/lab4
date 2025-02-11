# #1
# import datetime
# x = datetime.datetime.now()
# print(int(x.day) - 5)

# #2
# import datetime
# x = datetime.datetime.today()
# yesterday = x - datetime.timedelta(days=1)
# today=datetime.datetime.today()
# tomorrow=x + datetime.timedelta(days=1)
# print(yesterday,today,tomorrow)

# #3
# import datetime
# x = datetime.datetime.now()
# print(x.replace(microsecond=0))

#4
import datetime
date1 = datetime.datetime(2024, 2, 12, 12, 30, 0) 
date2 = datetime.datetime(2024, 2, 13, 14, 45, 30) 
time = date2 - date1
seconds = time.total_seconds()
print(seconds)

