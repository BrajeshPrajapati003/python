
t = int(input())

for i in range(t):
    num = int(input())
    shift = 10
    ans = []
    while num > 0:
        candidate = num % shift
        if candidate != 0:
            ans.append(candidate)
        num -= candidate
        shift *= 10

    print(len(ans))
    print(*ans)
