#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


i = 2520
while True:
    for j in range(20):
        if i % (j + 1) != 0:
            break
    else:
        print(i)
        break
    i += 20
