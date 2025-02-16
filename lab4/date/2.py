import datetime
def yesterday(today):
    return today - datetime.timedelta(days=1)

def tomorrow(today):
    return today + datetime.timedelta(days=1)

def today():
    return datetime.datetime.today()

current_date = today()

print("Yesterday: ", yesterday(current_date))
print("Today: ", current_date)
print("Tomorrow: ", tomorrow(current_date))
