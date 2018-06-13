#! Python 3

# Find the difference between the sum of the squares in a range and the square of the sum of the range

print("What range of numbers would you like to find the sum-square difference of?")
InputRange = input()
SumTotal = 0
SquareTotal = 0

for x in range(int(InputRange) + 1):
    SumTotal += x
    SquareTotal += x**2

SumSquare = SumTotal**2

Difference = SumSquare - SquareTotal
print("The difference is :" + str(Difference))
