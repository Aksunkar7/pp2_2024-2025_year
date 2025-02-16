import datetime

def subtract_days(today, delta):  
    return today - delta

n = int(input("Time delta: "))  # Қанша күн азайтатынымыз
current_date = datetime.datetime.today()
time_delta = datetime.timedelta(days=n)

print("New Date:", subtract_days(current_date, time_delta))
