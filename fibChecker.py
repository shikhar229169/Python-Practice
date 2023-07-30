def fibChecker(N):
    a = 0
    b = 1
    if (N == a or N == b):
        return True
    while (True):
        curr = a + b
        if (N == curr):
            return True
        if (curr > N):
            break
        a = b
        b = curr
    return False

N = int(input("Enter number you want to check: "))
res = fibChecker(N)
if (res):
    print("Abe fibonacci he ye toh")
else:
    print("hahahha! fibonacci nhi he tu hhahahah")