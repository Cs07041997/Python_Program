"""
  * Author - Chandan kumar
   * Date - 7-NOV-2021
   * Time - 16:00
   * Title - To find the roots of the equation.
"""

import math
# take user inputs
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))

# calculate value of Function
val = b ** 2 - 4 * a * c
root = math.sqrt(abs(val))

# Check for roots and print according to their nature
if val > 0:
    print("Two Real Roots")
    try:
        print((-b + root) / (2 * a))
        print((-b - root) / (2 * a))
    except Exception:
        print("can not divide by zero")
elif val == 0:
    print("One Real Root")
    try:
        print(-b / (2 * a))
    except Exception:
        print("cant divide by zero")
else:
    print("No Real Root")
    print(- b / (2 * a), " + i", root)
    print(- b / (2 * a), " - i", root)