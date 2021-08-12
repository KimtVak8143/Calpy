class Date:
    day = 0
    month = 0
    year = 0
    #month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
     #             9: "September", 10: "October", 11: "November", 12: "December"}

    def __int__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "Input is \n\tDate :{}\n\tMonth :{}\n\tYear :{}".format(self.day, self.month, self.year)


# month_list = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
  #             9: "September", 10: "October", 11: "November", 12: "December"}


def check():
    """Performs a check on input data"""
    return


# self.day = input("Enter the date :")
# self.month = input("Enter the month :")
# self.year = input("Enter the year :")
def show():
    """Prints the calendar"""
    return


def input_date():
    """Takes the input from user"""
    print("Input for First date :\n")
    d1 = int(input("Enter the date :"))
    m1 = input("Enter the month :")
    y1 = int(input("Enter the year :"))
    date1 = Date()
    date1.day = d1
    date1.month = m1
    date1.year = y1
    print("Input for second date :\n")
    d2 = int(input("Enter the date :"))
    m2 = input("Enter the month :")
    y2 = int(input("Enter the year :"))
    date2 = Date()
    date2.day = d2
    date2.month = m2
    date2.year = y2
    print("First", date1)
    print("Second", date2)
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
    print("Welcome {}".format(fn))


def main():
    print("Hello, to this program")
    welcome()
    input_date()


# to execute main function
if __name__ == '__main__':
    main()
