"""
  * Author - Chandan kumar
   * Date - 8-NOV-2021
   * Time - 18:00
   * Title - To print  Nth Harmonic.
"""
def harmonic(num):
    i = 1
    sum = 0

    while i <= num:
        sum += 1 / i
        i += 1
        print(sum)


num = int(input("Enter Number: "))
if num <= 0:
    print("Please enter the no greater than zero.")
else:
    harmonic(num)