
import calendar
import datetime

today = datetime.date.today()
calendarMonth={}
for month_idx in range(1, 13):
    calendarMonth [calendar.month_name[month_idx].lower()]=month_idx
    calendarMonth [calendar.month_abbr[month_idx].lower()]=month_idx
#printNow(today.strftime("%d -%B %A"))
month = requestString("What month were you born? ")
if month.lower() in calendarMonth: 
  monthCalendar = calendar.month(today.year,calendarMonth[month])
  daysInMonth = calendar.monthrange(today.year,calendarMonth[month])
  printNow(monthCalendar)
  day = requestInteger("What day were you born? ")
  if day < daysInMonth[1] and day>0: 
    birthDay = datetime.date(today.year, calendarMonth[month], day)
    if birthDay<today: 
      birthDay = datetime.date(today.year+1, calendarMonth[month], day)
    dif = birthDay-today
    printNow("You have %d untill your birthday"%(dif.days))
  else:
    showError("Well, this sucks, I cannot find %d in %s"%(day,month))
else: 
  showError("Well, this sucks, I cannot find %s in our calendar"%(month))
  
doi = datetime.date(1776,6,4)
weekday = calendar.day_name[doi.weekday()]
month = calendar.month_name[doi.day]
year = doi.year
printNow(weekday)
printNow(month)
printNow(doi.day)
printNow(year)
printNow(" Did you know that Declaration of Independence was ratified by the Continental Congress "+ weekday+" "+month+" "+str(doi.day)+", "+str(year))
