import datetime

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)

message = "GVR was born on {:%A, %B, %d, %Y}."
print(message.format(gvr))

now = datetime.datetime.now()

print(now)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)