from datetime import datetime, timedelta
import datetime

date1 = datetime.datetime.now()
previous_date = date1 + timedelta(days=-1)
next_date = date1 + timedelta(days=1)

print("today: ", date1.strftime("%x"))
print("yesturday: ", previous_date.strftime("%x"))
print("tomorrow: ", next_date.strftime("%x"))