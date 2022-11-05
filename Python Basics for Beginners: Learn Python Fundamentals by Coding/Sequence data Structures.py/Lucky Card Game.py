def findPoint(card, num):
    result = 0
    if card == 'R' or card == 'Q':
        result = 10 * num
    elif card == 'P':
        result = 7 * num
    else:
        result = 5 * num
    return result

arun = arya = 0
n = int(input("Enter number of time player can flip the card\n"))
for i in range(n):
    card = input("Arun flip the card\n")
    num = int(input())
    arun += findPoint(card, num)
    card = input("Arya flip the card\n")
    num = int(input())
    arya += findPoint(card, num)

print("Total scores  %d %d"%(arun, arya))
if arun > arya:
    print("Arun won the game")
elif arun < arya:
    print("Arya won the game")
else:
    print("Game tied")