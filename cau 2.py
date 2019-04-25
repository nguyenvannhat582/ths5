import datetime as dt
format='%Y-%m-%dT%H:%M:%S'
t1=dt.datetime.strptime('2018-10-12T14:45:52',format)
print('day' + str(t1.day))
print('minute' + str(t1.minute))
print('month' + str(t1.month))
print('second' + str(t1.second))

#define todays date and time
t2=dt.datetime.now()
diff=t2-t1
print('how many days difference?' + str(diff.days))
