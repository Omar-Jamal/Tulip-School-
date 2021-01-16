t = ("1.istanbul")
i = ("2.london")
j = ("3.tokyo")
u = ("4.newyork")
print("this program helps the user to know the times of these cities")
print(t, i, j, u)
print("please enter choice (1,2,3,4)")

que1 = input("where are you live ?")
if que1 == "1":
    print(" Now the time in Istanbul is ")
    from datetime import datetime
    import pytz
    IST = pytz.timezone('Europe/Istanbul')
    print(datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/London')
    print("in london ", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('US/Eastern')
    print("in newyork ", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Asia/Tokyo')
    print("in tokyo", datetime.now(IST).strftime('%H:%M:%S'))

elif que1 == "2":
    print("Now the time in London  is")
    from datetime import datetime
    import pytz

    IST = pytz.timezone('Europe/London')
    print(datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('US/Eastern')
    print("in newyork ", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Asia/Tokyo')
    print("in tokyo", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/Istanbul')
    print("in istanbul", datetime.now(IST).strftime('%H:%M:%S'))
elif que1 == "3":
    print("Now the time in Tokyo is")
    from datetime import datetime
    import pytz

    IST = pytz.timezone('Asia/Tokyo')
    print(datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('US/Eastern')
    print("in newyork ",datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/London')
    print("in london " , datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/Istanbul')
    print("in istanbul",datetime.now(IST).strftime('%H:%M:%S'))
elif que1 == "4":
    print("Now the time in Newyork is ")
    from datetime import datetime
    import pytz
    IST = pytz.timezone('US/Eastern')
    print(datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/London')
    print("in london ", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Europe/Istanbul')
    print("in istanbul", datetime.now(IST).strftime('%H:%M:%S'))
    IST = pytz.timezone('Asia/Tokyo')
    print("in tokyo",datetime.now(IST).strftime('%H:%M:%S'))


