def is_leap(year):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0 and year % 400 != 0:
            is_leap = False
    return is_leap

print(is_leap(2001))