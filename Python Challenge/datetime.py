

import datetime
import pytz 
import time


port = datetime.datetime.now(pytz.timezone('US/Pacific'))
op = port.replace(hour=9, minute=0, second=0)
cp = port.replace(hour=17, minute=0, second=0)

nyc = datetime.datetime.now(pytz.timezone('US/East-Indiana'))
on = nyc.replace(hour=9, minute=0, second=0)
cn = nyc.replace(hour=17, minute=0, second=0)


lon = datetime.datetime.now(pytz.timezone('Europe/London'))
ol = lon.replace(hour=9, minute=0, second=0)
cl = lon.replace(hour=17, minute=0, second=0)



def portOpen():
    
    if port >= op and port <= cp:
        return("The Portland branch is open")
    else:
        return("The Portland branch is closed")

    
def nycOpen():
    if nyc >= on and nyc <= cn:
        return("The New York City branch is open")
    else:
        return("The New York City branch is closed")

def lonOpen():
    if lon >= ol and lon <= cl:
        return("The London branch is open")
    else:
        return("The London branch is closed")
    

print(port.strftime("%c"))
print(nyc.strftime("%c"))
print(lon.strftime("%c"))
print(portOpen())
print(nycOpen())
print(lonOpen())
