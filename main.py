# The month_list dictionary for month conversion
month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}

# Names of Days in a Week
days_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# List of Days in a month for a leap and non-leap year Respectively
mon_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Class Date for storing date and printing
class Date:
    day = 0
    month = 0
    year = 0

    def __int__(self, day, month, year):  # initialising values
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):  # printing the string
        # print("\nDate is {} {} {}".format(self.day, month_list[self.month], self.year))
        # return "Input is \n\tDate :{}\n\tMonth :{}\n\tYear :{}".format(self.day, month_list[self.month], self.year)
        return "Date is {} {} {}".format(self.day, month_list[self.month], self.year)


def show(day, month, year):
    """Prints the calendar"""
    print("\nYear : {} \tMonth : {}".format(year, month_list[month]))
    for i in days_list:
        print(i, end=" ")
    for i in range(1, leap_check(year, month)+1):
        if i % 7 == 1:
            print("")
        if i == day:
            print('\u0332', end='{}*\t'.format(i))
        else:
            print(i, end='\t')
    return


def leap_check(x, y):
    """Checks if the year is leap or not for february month"""
    # m = 0
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                m = mon_leap[y-1]   # leap = 1  # Year is leap, follow mon_leap
            else:
                m = mon_days[y-1]  # leap = 0  # leap is false, follow mon_days
        else:
            m = mon_leap[y-1]   # leap = 1  # Year is leap, follow mon_leap
    else:
        m = mon_days[y-1]  # leap = 0  # leap is false, follow mon_days

    return m


def input_date():
    """Takes the input from user"""
    # print("\nInput for First date")
    flag, post = 0, 0
    d1, m1, y1 = 0, 0, 0
    d2, m2, y2 = 0, 0, 0

    while flag == 0:
        print("\nInput for First date")
        y1 = int(input("Enter the year :"))
        if y1 > 0:
            flag += 1

        m1 = int(input("Enter the month :"))
        if 0 < m1 < 13:
            flag += 1

        d1 = int(input("Enter the date :"))
        if 0 < d1 < leap_check(y1, m1)+1:
            flag += 1

        if flag != 3:
            print("Try Again")
            flag = 0
        else:
            break

    # check("first", d1, m1, y1)
    date1 = Date()
    date1.day = d1
    date1.month = m1
    date1.year = y1

    while post == 0:
        print("\nInput for Second date")
        y2 = int(input("Enter the year :"))
        if y2 > 0:
            post += 1

        m2 = int(input("Enter the month :"))
        if 0 < m2 < 13:
            post += 1

        d2 = int(input("Enter the date:"))
        if 0 < d2 < leap_check(y2, m2)+1:
            post += 1

        if post != 3:
            print("Try Again")
            post = 0
        else:
            break

    date2 = Date()
    date2.day = d2
    date2.month = m2
    date2.year = y2
    print("\n\nFirst", date1)
    show(d1, m1, y1)
    print("\nSecond", date2)
    show(d2, m2, y2)
    return


def diff():
    """shows the difference between 2 dates"""
    return


def welcome():
    """Welcome message for user"""
    # print("Enter your name")
    fn = input("Enter your name :")
    # print("\nWelcome {}".format(fn))
    return fn


def goodbye(par):
    """Shows Exit Message on Completion of Program"""
    return "\n\nThank you {}, for visiting :".format(par)


def main():
    print("Hello, to this program")
    named = welcome()
    print("\nWelcome {}".format(named))
    # show(31, 4, 2020)
    input_date()
    print(goodbye(named))


# to execute main function
if __name__ == '__main__':
    main()
