def DAYS(days):
    year = days//365
    month = (days%365)//30
    day = (days%365)%30
    print(f"{year} years, {month} months, and {day} days")
DAYS(int(input()))