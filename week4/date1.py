from datetime import datetime, timedelta
import datetime

first_day = datetime.datetime.now()

for i in range(5):
    day = first_day + timedelta(days=1)
    print(day.strftime("%x"))
    first_day = day
