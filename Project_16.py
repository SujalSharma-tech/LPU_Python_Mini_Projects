date01, month01, year01 = input(
    "Enter date of birth in DD/MM/YY format: ").split('/')
date02, month02, year02 = input(
    "Enter current date in DD/MM/YY format: ").split('/')


year1 = int(year01)
year2 = int(year02)

totyr = year2 - year1

month1 = int(month01)
month2 = int(month02)

date1 = int(date01)
date2 = int(date02)

day = (date2-date1)


def leap(year1, year2):
    days = 0
    for year in range(year1, year2):
        if year % 4 == 0 or year % 100 == 0:
            if year % 400 == 0:
                days += 365
                continue
            days += 366
            continue
        days += 365
    return days


daysforyears = leap(year1, year2)
# print(int(daysforyears/365), "Years")


def months(month1, month2):
    totmonth = totyr*12
    if month01 != "01":
        totmonth -= month1-1

    if month02 != "01":
        totmonth += month2-1
    return totmonth

# print("Total: ", int(monthsforyears*30.439)+day-1, "Days")


monthsforyears = months(month1, month2)

if day < 0:

    monthsforyears -= 1
    day = 31+day

print(int(daysforyears/365), "Years ,",
      monthsforyears, "Months and", day, "Days")

print("Total: ", int(monthsforyears*30.437)+day, "Days")
