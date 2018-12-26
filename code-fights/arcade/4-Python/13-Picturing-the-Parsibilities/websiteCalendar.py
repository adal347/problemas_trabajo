import calendar

def websiteCalendar(month, year):
    return calendar.HTMLCalendar().formatmonth(theyear = year, themonth = month,
            withyear = True).replace('\n', '')
