#The sum of the squares of the first ten natural numbers is 385

#The square of the sum of the first ten natural numbers is 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


squarestotal = 0
nums = 0
for i in range(100):
    squarestotal += (i + 1) * (i + 1)
    nums += i + 1
print(nums * nums - squarestotal)
