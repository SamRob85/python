import math
from datetime import datetime
date=input("What date do you want to find the distance from")
d = datetime.now()
d1 = datetime.strptime(date, '%d/%m/%Y')
x=(d-d1).days
pi=math.pi
earthtosun=149597870700
diameter=earthtosun*2
circumference=pi*diameter
degree=circumference/360
totalangle=360
daysinyear=365.256
angleday=totalangle/daysinyear
totalangle=x*angleday
totaldistance=totalangle*degree
print(str(totaldistance)+"m or "+str((totaldistance/1000))+"km")




