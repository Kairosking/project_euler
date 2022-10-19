fibonacci = [1, 2]
ans = 2
while fibonacci[-1] < 4000000:
    newvalue = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(newvalue)
    if newvalue % 2 == 0:
        ans += newvalue
print(ans)
