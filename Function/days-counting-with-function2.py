def is_year_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    
    days_in_common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return days_in_common_year[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    day_num = 0
    for m in range(1, month):
        day_num += days_in_month(year, m)
    
    day_num += day
    return day_num

print(day_of_year(2000, 12, 31))  
