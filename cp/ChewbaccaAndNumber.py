
num = input()

if num == '9':
    print(num)
else:
    ans = ''
    for i in range(len(num)):
        a = int(num[i])
        b = 9-a
        if b == 0 and i == 0:
            ans = ans + str(a)
        else:
            ans = ans + str(min(a,b))
    print(ans)
