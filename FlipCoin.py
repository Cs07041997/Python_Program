"""
  * Author - Chandan kumar
   * Date - 9-NOV-2021
   * Time - 18:40
   * Title - To find Flip coin percentage.
"""
import random
def flipCoin():
    number = int(input("Enter the first number"))
    
    if number<=0:
        print("please enter the positive number")
    head=0
    tail=0
    for i in range(number):
        toss = random.randint(0, 1) # we can also use randrange
        print("Random number between 0 and 1 is "  (toss))
        if toss<=0.5:
            print("Tails")
            tail += 1
            tailPercent = (tail / number) * 100
            print(tailPercent)
        else:
            print("Heads")
            head += 1
            headPercent = (head / number) * 100
            print(headPercent)                     
    flipCoin()
 


