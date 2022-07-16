from flask import Flask
import BTC
# import requests
import redis

app = Flask(__name__)
btcData = redis.Redis(host='redis', port=6379)


@app.route("/")

def home():
    # True loop used for getting the price in less than minute
    while True:

        price = float("{:.2f}".format(BTC.gitCurBTCPrice()))
        avgPrice = float("{:.2f}".format(BTC.gitAvgBtCPrice()))

        # save it in btcData redis file
        btcData.set('CurrPrice', price)
        btcData.set('AvgPrice', avgPrice)

        #refresh to update the content in page without clicking refresh each time
        return """
        <meta http-equiv="refresh" content="1" /><h2>Docker Final Task, Current BTC Price</h2><br> <h3>Current BitCoin Price is: {}$</h3><br> <h3>Average BitCoin Price Last 10 Minutes: {}$ </h3><br> """.format(price,avgPrice)