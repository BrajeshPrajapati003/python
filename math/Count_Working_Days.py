'''
There are n days, Every 7th day is Sunday -> Jack doesn't get that day
Some additional days (given in array) are also holidays -> Jack doesn't get those days
Find how many days Jack actually gets.
'''

# idea: total days - Sundays - other holidays (excluding Sundays)
# if a holiday falls on Sunday -> don't count twice

def countWorkingDays(n, holidays):

    # mark holidays for quick lookup
    holiday_set = set(holidays)
    working_days = 0

    for day in range(1, n+1):

        # check Sunday
        if day % 7 == 0:
            continue

        # check holiday
        if day in holiday_set:
            continue

        working_days += 1
    
    return working_days

n = int(input()) # 14
holidays = list(map(int, input().split())) # 2 5 7
print(countWorkingDays(n, holidays)) # 10 (1,3,4,6,8,9,10,11,12,13)
