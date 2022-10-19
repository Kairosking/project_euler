squarestotal = 0
nums = 0
for i in range(100):
    squarestotal += (i + 1) * (i + 1)
    nums += i + 1
print(nums * nums - squarestotal)
