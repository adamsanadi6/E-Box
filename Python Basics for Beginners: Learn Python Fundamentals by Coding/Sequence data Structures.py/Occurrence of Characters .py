string = input()
frequence = dict()
for i in string:
    if i in frequence:
        frequence[i] += 1
    else:
        frequence[i] = 1

print("Dictionary of string: {",end="")
length = len(frequence)
keys = sorted(frequence.keys())
for key in keys:
    if length == 1:
        print("'%s': %d}"%(key, frequence[key]),end="")
        break
    print("'%s': %d, "%(key, frequence[key]),end="")
    length -= 1
for i in keys:
    print("%s-- %d"%(i, frequence[i]))