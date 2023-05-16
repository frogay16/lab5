import datetime

def magicdate(date):
    try:
        a = datetime.datetime.strptime(date, "%d.%m.%Y")
        day = a.day
        month = a.month
        year = a.year % 100
        if day * month == year:
            return True
        else:
            return False
    except ValueError:
        return False

date = input()
print(magicdate(date))