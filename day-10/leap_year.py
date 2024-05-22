def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

def days_in_month(year, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day == 2:
        if is_leap(year):
            # return month_days[day-1] + 1
            return 29
    return month_days[day-1]


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_month(year, month)
print(days)