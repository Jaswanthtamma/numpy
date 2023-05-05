import time
l=list(range(1000000))
for i in  range(1000000):
    l[i]*=l[i]
    print(i)

