"""
   * Author - chandan kumar
   * Date - 10-Nov-2021
   * Time - 4:14 PM
   * Title - Sum of three Integer adds to ZERO
"""

def find_triples(arr, n):
    found = True
    count = 0
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    found = True
                    count = count + 1
    print("The number of triples is: ", count)

    # If no triplet with 0 sum found in array
    if not found:
        print(" not exist ")

while True:
    try:
        array = []
        length = int(input("Enter length of array: "))
        for i in range(length):
            temp = int(input("Enter numbers: "))
            array.append(temp)
        find_triples(array, length)
        break
    except ValueError:
        print("Check the input")