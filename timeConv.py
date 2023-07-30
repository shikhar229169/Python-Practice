
'''@param currTime It is in format HH:MM AM/PM
'''
def timeConv(currTime):
    # I don't like magic numbers
    OFFSET = 12
    MAX_HOURS = 24

    hr = int(currTime[0:2])
    min = int(currTime[3:5])

    if "PM" in currTime:
        hr = (hr + OFFSET) % MAX_HOURS
    
    return str(hr) + ':' + str(min)


myTime = "11:53 PM"
_24_FORMAT = timeConv(myTime)    
print(_24_FORMAT)