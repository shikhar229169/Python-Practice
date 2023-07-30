
'''@param currTime It is in format HH:MM AM/PM
'''
def timeConv(currTime):
    # I don't like magic numbers
    OFFSET = 12

    hr = int(currTime[0:2])
    min = int(currTime[3:5])

    if "PM" in currTime and hr != 12:
        hr = (hr + OFFSET)
    elif "AM" in currTime and hr == 12:
        hr = 0
    
    convTime = ""

    convTime += (str(hr // 10))
    convTime += (str(hr % 10))
    convTime += (":")
    convTime += (str(min // 10))
    convTime += (str(min % 10))

    return convTime


myTime = "01:53 PM"
_24_FORMAT = timeConv(myTime)    
print(_24_FORMAT)