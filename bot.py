from doctest import master
import ccxt
import config
import time_converter

exchange = ccxt.binance()

print(exchange)

markets = exchange.load_markets()

sym_arr = []

for i in markets:
    if i[-4:] == 'USDT':
        sym_arr.append(i)



master_arr = []

sorted_arr = []


for sym in sym_arr:
    try:
        response = exchange.fetch_ohlcv(sym, '12h', params={'price':'index'})
        arr = []
        x={}
        for i in range(len(response)):
            arr.append(response[i][2])

        x[sym] = response[arr.index(max(arr))][0]

        master_arr.append(x)

        y = str(time_converter.convert(response[arr.index(max(arr))][0])) +  '    ' + sym

        sorted_arr.append(y)
        print(x)
    except:
        pass

print('-*-*-*-------------*********---------------*-*-*-')
for elm in sorted(sorted_arr):
    print(elm)