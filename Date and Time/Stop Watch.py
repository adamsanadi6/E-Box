sh, sm, ss =map(int, input("Start time \n").split(":")) 
eh, em, es =map(int, input("End time \n").split(":"))


s = es - ss
m = (em - sm) * 60
h = (eh - sh) * 60 * 60
total = h + m + s
print("Time in milliseconds is %d"%(total * 1000))