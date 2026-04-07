'''
Jack loves Sundays because he gets to relax & enjoy his day.
You're given:
    n -> total no. of days in a month
    the starting day of the month (e.g. Sun, Mon,...)
Goal: How many Sundays occur within these n days
'''
def count_sundays(n, start_day):

    # map string -> number
    days = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2, 
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }

    start = days[start_day]

    # full weeks
    sundays = n // 7

    # remaining days
    rem = n % 7

    # check extra sunday in remaining days
    # for i in range(rem):
    #     if (start + i) % 7 == 0:
    #         sundays += 1
    # return sundays


    # check if Sunday falls in remaining window
    if (7 - start) <= rem and start != 0:
        sundays += 1
    elif start == 0 and rem > 0:
        sundays += 1

    return sundays

n = int(input())
start_day = input().strip()

print(count_sundays(n, start_day))
