import calendar
year = int(input('enter the year :'))

calendar.setfirstweekday(calendar.SUNDAY)

mycal = calendar.calendar(year)
print(mycal)