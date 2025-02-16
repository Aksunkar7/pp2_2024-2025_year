import datetime
def difference(date1, date2):
    difference = abs((date1-date2).total_seconds())
    return difference
    
date1 = datetime.datetime(2025, 2, 16, 12, 0, 0)  # Example: 16th Feb 2025, 12:00:00
date2 = datetime.datetime(2025, 2, 14, 9, 30, 0)  # Example: 14th Feb 2025, 09:30:00

print(f"difference in seconds: {difference(date1, date2)}")
    
