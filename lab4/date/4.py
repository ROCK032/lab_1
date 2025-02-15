from datetime import datetime

date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

dt1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

difference = abs((dt2 - dt1).total_seconds())

print(f"Difference in seconds: {difference:.0f}")
