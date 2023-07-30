# a = 1,2,3
# print(type(a))

# print((lambda x,y : y - 2*x) (1, 11))

# s = "PYTHON"

# k = 4

# myStr = ""

# for i in range(len(s)):
#     if (i == k):
#         continue
#     myStr += s[i]

# print(myStr)

def calcAvg(arr):
    avg: float
    try:
        sum = 0
        for i in arr:
            sum += i
        avg = sum / len(arr)
    except ZeroDivisionError: 
        avg = 0.0
    
    return avg

print(calcAvg([]))

# print(range(s, e))