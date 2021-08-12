# The month_list dictionary for month conversion
month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}


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


def show():
    """Prints the calendar"""
    return


def input_date():
    """Takes the input from user"""
    # print("\nInput for First date")
    flag = 0
    post = 0
    d1 = 0
    d2 = 0
    m1 = 0
    m2 = 0
    y1 = 0
    y2 = 0
    while flag == 0:
        print("\nInput for First date")
        d1 = int(input("Enter the date :"))
        if 0 < d1 < 32:
            flag += 1

        m1 = int(input("Enter the month :"))
        if 0 < m1 < 13:
            flag += 1

        y1 = int(input("Enter the year :"))
        if y1 > 0:
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
        d2 = int(input("Enter the date:"))
        if 0 < d2 < 32:
            post += 1

        m2 = int(input("Enter the month :"))
        if 0 < m2 < 13:
            post += 1

        y2 = int(input("Enter the year :"))
        if y2 > 0:
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
    print("\nFirst", date1)
    print("\nSecond", date2)
    return


def diff():
    """shows the difference between 2 dates"""
    return


def modify():
    """marks an asterisk on important days"""
    return


def welcome():
    """Welcome message for user"""
    # print("Enter your name")
    fn = input("Enter your name :")
    print("\nWelcome {}".format(fn))


def main():
    print("Hello, to this program")
    welcome()
    input_date()


# to execute main function
if __name__ == '__main__':
    main()
