"""
  * Author - Chandan kumar
   * Date - 7-NOV-2021
   * Time - 16:40
   * Title - To find 2D array.
"""
Rows = int(input("Enter the number of rows:"))
Col = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries in row wise:")

for i in range(Rows):
    array = []
    for j in range(Col):
        array.append(int(input()))  # ---->ADDING INPUT IN ARRAY
    matrix.append(array)
print("The 2D array is given below:")
for i in range(Rows):
    for j in range(Col):
        print(matrix[i][j], end=" ")
    print()
