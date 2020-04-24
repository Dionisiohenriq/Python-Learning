import datetime

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)  # 'timedelta' uses an integer value or a datetime value to subtract or add to another date
print(mill + dt)

message = "GVR was born on {:%A, %B, %d, %Y}."
print(message.format(gvr))

now = datetime.datetime.now() # same as datetime.today()

print(now)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 1, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

print(launch_date.month)
print(launch_datetime.day)

now_2 = datetime.datetime.today()
print(now_2)

help(datetime)