"""
  * Author - Chandan kumar
   * Date - 9-NOV-2021
   * Time - 20:30
   * Title - To find the roots of the equation.
"""
class PowerOfTwo:
    def PowerCalculation(self):
        inputNumber = int(input("Enter Number to Calculate Table::"))
        try:
            if inputNumber>31:
                raise ValueError("********** Invalid Input *********")
            elif inputNumber<0:
                raise ValueError("********** Invalid Input *********")
            else:
                for i in range (1,inputNumber+1):
                    table=2*i
                    print("2^",i,":", table)
        except ValueError as e:
                print(e)
powerTwo=PowerOfTwo()
powerTwo.PowerCalculation()