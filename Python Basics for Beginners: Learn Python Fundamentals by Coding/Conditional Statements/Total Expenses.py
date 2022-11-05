cost = int(input())
n = int(input())
prize = n * cost
if n >= 50 and n <= 100:
    prize = prize - ((prize/100) * 10)
elif n >= 101 and n <= 200:
    prize = prize - ((prize/100) * 20)
elif n >= 201 and n <= 400:
    prize = prize - ((prize/100) * 30)
elif n >= 401 and n <= 500:
    prize = prize - ((prize/100) * 40)
elif n > 500 :
    prize = prize - ((prize/100) * 50)
    
print("%.2f"%prize)