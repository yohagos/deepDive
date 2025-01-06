from datetime import datetime, date, time, timedelta

now = datetime.now()
# print(now)                      # 2021-07-08 07:34:46.549883
# day = now.day                   # 8
# month = now.month               # 7
# year = now.year                 # 2021
# hour = now.hour                 # 7
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
#
#
# new_year = datetime(2025, 1, 1, 16, 17,55)
# print(new_year)
#
# print(f'New Year : {new_year.day}.{new_year.month}.{new_year.year}')
#
# t = now.strftime("%H:%M:%S")
# print('Time : ', t)
# time_one = now.strftime("%H:%M:%S, %d.%m.%Y")
# print("Time : ", time_one)

# date_string = "5 December, 2024"
# print("Date_String : ", date_string)
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("Date_String : ", date_object)

# d = date(2020,1,1)
# print(d)
# print('Current date : ', d.today())
#
#
# a = time()
# print("a =", a)
# # time(hour, minute and second)
# b = time(10, 30, 50)
# print("b =", b)
# # time(hour, minute and second)
# c = time(hour=10, minute=30, second=50)
# print("c =", c)
# # time(hour, minute, second, microsecond)
# d = time(10, 30, 50, 200555)
# print("d =", d)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
