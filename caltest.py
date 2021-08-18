import calendar


def print_cal(y):
    print(calendar.calendar(y))


year = int(input("Enter year :"))
print_cal(year)
