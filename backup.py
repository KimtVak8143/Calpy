# Python code to print Calendar
# Without use of Calendar module

mm = int(input("Enter month:"))
yy = int(input("Enter year :"))

month_list = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}

days_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

mon_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# code below for calculation of odd days
day = (yy - 1) % 400
day = (day // 100) * 5 + ((day % 100) - (day % 100) // 4) + ((day % 100) // 4) * 2
day = day % 7

s = 0

if yy % 4 == 0:
    for i in range(mm - 1):
        s += mon_leap[i]
else:
    for i in range(mm - 1):
        s += mon_days[i]

day += s % 7
day = day % 7

# variable used for white space filling
# where date not present
space = ''
space = space.rjust(2, ' ')

# code below is to print the calendar
print(month_list[mm], yy)

x = " "
print(x.join(days_list))
# print('SUN', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')


for i in range(31 + day):

    if i <= day:
        print(space, end='  ')
    else:
        print("{:02d}".format(i - day), end='  ')
        if (i + 1) % 7 == 0:
            print()

