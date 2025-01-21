# 준현이는 전량 매수한다.
# 성민이는 33 매매법을 사용한다.

cash = int(input())
stock_price = list(map(int, input().split()))

def junhyun(cash, stock_price):
    stock = 0
    for price in stock_price:
        stock += cash // price
        cash %= price
    return cash + stock * stock_price[-1]

def sungmin(cash, stock_price):
    stock = 0
    count = 0
    for i in range(1, len(stock_price)):
        if stock_price[i] > stock_price[i-1]:
            if count >= 0:
                count += 1
            else:
                count = 1
            if count == 3:
                cash += stock * stock_price[i]
                stock = 0
        elif stock_price[i] < stock_price[i-1]:
            if count <= 0:
                count -= 1
            else:
                count = -1
            if count == -3:
                stock += cash // stock_price[i]
                cash %= stock_price[i]
    return cash + stock * stock_price[-1]

junhyun = junhyun(cash, stock_price)
sungmin = sungmin(cash, stock_price)
if junhyun > sungmin:
    print('BNP')
elif junhyun < sungmin:
    print('TIMING')
else:
    print('SAMESAME')
