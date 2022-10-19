#https://projecteuler.net/problem=16


power = 2
ans = 0
for i in range(999):
    power = power * 2
    #note: after finishing i found out you can just use pow(2, 1000) lol
for i in range(len(str(power))):
    ans += int(str(power)[i])

print(ans)
