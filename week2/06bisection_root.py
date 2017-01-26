x = 8
epsilon = 0.01
high = x
low = 0
ans = (high + low) / 2.0

while abs(ans**3 - x) >= epsilon:
    print(low, high)
    if ans**3 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2.0

print(ans)
