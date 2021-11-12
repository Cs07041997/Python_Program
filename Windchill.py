"""
   * Author - Chandan kumar
   * Date - 9-nov-2021
   * Time - 21:00
   * Title - WindChill
"""
import math

while True:
    try:
        t = int(input("Enter Temperature t:"))
        v = int(input("Enter Wind Speed v:"))
        break
    except ValueError:
        print("Check the input")


if t <= 50 and 3 <= v <= 120:
    w = 35.74 + 0.625 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print(w)
else:
    print("Enter Correct Values.")