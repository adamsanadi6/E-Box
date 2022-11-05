n = int(input("Enter the number of clients\n"))
clients = dict()
for i in range(1, n + 1):
    print("Enter the details of the client %d"%i)
    name = input()
    email = input()
    passportNumber = input()
    clients[passportNumber] = [name, email]

passportNumber = input("Enter the passport number of the client to be searched\n")
if passportNumber not in clients:
    print("Client not found")
else:
    print("Client Details")
    print("%s--%s--%s"%(clients[passportNumber][0], clients[passportNumber][1], passportNumber))