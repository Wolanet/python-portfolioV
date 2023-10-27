import calendar
from datetime import datetime

#getting current year and month
now = datetime.now()
currentyear = now.year
currentmonth = now.month

#print the current month calendar
print (calendar.month(currentyear, currentmonth))