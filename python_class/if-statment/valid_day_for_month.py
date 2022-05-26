
#given a month and a date, check if the date is valid.

months={
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

month=int(input("number of month? (eg. january=1, febuary=2, march=3...)"))
if month in months:
    date=int(input("date in the month?"))
    if date<=months[month] and date>0:
            print('valid date')
    else:
        print("invalid date")
else:
    print("invalid month")

#alternitive way
if month==1:
    if date<=31 and date>0:
        print('valid')
    else:
        print('invalid')

if month==2:
    if date<=29 and date>0:
        print('valid')
    else:
        print('invalid')
    