from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

todayDate = datetime(year,month,day)

nextWeekDate = todayDate + timedelta(days = 7)

print(f"Day: {nextWeekDate.day}  Month: {nextWeekDate.month}  Year: {nextWeekDate.year}")
