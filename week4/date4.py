from datetime import datetime, timedelta
import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2025, 2, 13)
difference = date2 - date1

print("second difference: ", difference.total_seconds().strftime("%S"))