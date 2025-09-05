cash = float(input("Troca devida: "))

cash = round(cash * 100)

coins = 0

while cash > 0:
    match cash:
        case _ if cash >= 25:
            cash -= 25
            coins += 1
        case _ if cash >= 10:
            cash -= 10
            coins += 1
        case _ if cash >= 5:
            cash -= 5
            coins += 1
        case _ if cash >= 1:
            cash -= 1
            coins += 1

print(coins)