'''
There are n days, Every 7th day is Sunday -> Jack doesn't get that day
Some additional days (given in array) are also holidays -> Jack doesn't get those days
Find how many days Jack actually gets.
'''

# idea: total Sundays = n // 7
# Working Days = n - Sundays - extra holidays

def count_working_days(n, holidays):

    sundays = n // 7
    # set = uniqueness + safety + performance
    holiday_set = set(holidays)

    extra_holidays = 0

    for h in holiday_set:
        if h <= n and h % 7 != 0: # not sunday
            extra_holidays += 1
    
    return n - sundays - extra_holidays
