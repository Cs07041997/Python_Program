"""
  * Author - Chandan kumar
   * Date - 7-NOV-2021
   * Time - 16:40
   * Title - To find the distance.
"""
import math
x1=float(input('Enter the x1 co-ordinate'))
y1=float(input('Enter the y1 co-ordinate'))
x2 = float(input('Enter the x2 co-ordinate of the second point:'))
y2 = float(input('Enter the y2 co-ordinate of the second point:'))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print("distance is ",distance)