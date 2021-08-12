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
        return "\nDate is {} {} {}".format(self.day, month_list[self.month], self.year)


def check():
    """Performs a check on input data"""
    return


def show():
    """Prints the calendar"""
    return


def input_date():
    """Takes the input from user"""
    print("\nInput for First date")
    d1 = int(input("Enter the date :"))
    m1 = int(input("Enter the month :"))
    y1 = int(input("Enter the year :"))
    date1 = Date()
    date1.day = d1
    date1.month = m1
    date1.year = y1
    print("\nInput for second date")
    d2 = int(input("Enter the date :"))
    m2 = int(input("Enter the month :"))
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
    print("\nWelcome {}".format(fn))


def main():
    print("Hello, to this program")
    welcome()
    input_date()


# to execute main function
if __name__ == '__main__':
    main()
