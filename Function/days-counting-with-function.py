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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
