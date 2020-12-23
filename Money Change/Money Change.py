m = int(input())

denoms = [10,5,1]
currentMoney = m
numberOfCoins = 0

while currentMoney != 0:
    if currentMoney-denoms[0] >= 0:
        currentMoney-=denoms[0]
        numberOfCoins+=1
    elif currentMoney-denoms[1]>=0:
        currentMoney-=denoms[1]
        numberOfCoins+=1
    else:
        currentMoney-=denoms[2]
        numberOfCoins+=1

print(numberOfCoins)