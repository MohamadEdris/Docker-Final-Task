import requests

# Class to git BTC current Price
# Calculate the avg of bitcion price for the last ten minutes


# return average of bitcoin price for the last 10 minutes
def gitAvgBtCPrice():
    # save in the variable objects in json format
    sum=0
    BTCpriceMinute = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=9').json()['Data']['Data']
    for bt in BTCpriceMinute:
        sum+=bt['close']
    return (sum/10)

# return current bitcoin price function
def gitCurBTCPrice(): 
    # this request.get returns in json format a single object and the ['USD'] get the value(price) of the current bitcion price.
    CurrentBtc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']
    return CurrentBtc
