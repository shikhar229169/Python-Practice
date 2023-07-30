a = "abbbbJHDHjjH"

uc = 0
lc = 0

for i in a:
    if (i.isupper()):
        uc += 1
    else:
        lc += 1

print (uc, lc)