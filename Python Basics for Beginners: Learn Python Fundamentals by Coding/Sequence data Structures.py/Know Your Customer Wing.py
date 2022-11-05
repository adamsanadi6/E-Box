key = ["Door-no: ", "Street: ", "Area: ", "City: ", "State: ", "Zipcode: ", "Country: "]
val = list(input().split(","))
address = dict(zip(key, val))
for key, val in address.items():
    print("%s%s"%(key, val))