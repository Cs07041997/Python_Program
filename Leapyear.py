"""
  * Author - Chandan kumar
   * Date - 9-NOV-2021
   * Time - 19:15
   * Title - To find the roots of the equation.
"""
def leapYear(year):
    if year < 1000:
        print("Please Enter 4 Digit Year")
        return

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("The given year is a Leap Year")
    else:
        print("The given year is not a Leap Year")


leapYear(int(input("Enter Year: ")))