"""
modules
"""
import datetime #importing_date_and_time
x = datetime.datetime.now()
print(x)

"""
importing todays weekday
"""
x = datetime.datetime.now()
print("today's week day is ",x.strftime("%A")) #%A_is_used_to_print_the_full_name_of_week_day

"""
importing apr11 weekday
"""
x = datetime.datetime(2019, 4, 11)
print('week day 0n apr11 is ',x.strftime("%a")) #%a_is_used_to_print_weekday_in_short_form

"""
importing only date
"""
x=datetime.datetime.today()
print('todays_date_is',x.strftime("%d"))

"""
import only time
"""
print('present_time_is',x.strftime('%I:%M:%S'))

"""
string to datetime
"""
form datetime import datetime
t=datetime.strptime('apr 11 2019 10:30','%b %d %y %I:%M')
print(t.date())
