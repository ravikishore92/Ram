from datetime import datetime, date, time
# Current date and time
now = datetime.now()
print(now)
# Specific date and time
dt = datetime(2023, 7, 18, 15, 30)
print(dt)
# Extracting date and time components
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
# Formatting datetime as string
formatted = dt.strftime('%Y-%m-%d %H:%M:%S')
print(formatted)
# Parsing string to datetime
parsed = datetime.strptime('2023-07-18 15:30:00', '%Y-%m-%d %H:%M:%S')

print(parsed)
import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)
specific_datetime = datetime.datetime(2023, 7, 18, 12, 30, 0)
print(specific_datetime)
date_string = "2023-07-18"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)
formatted_date = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
