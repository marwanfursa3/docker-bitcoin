
from flask import Flask
import requests
import time


start_time = time.time()
total = 0
counter = 0



def get_latest_bitcoin_price():
   
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(TICKER_API_URL)

    response_json = response.json() 

    return response_json["bpi"]["USD"]["rate"]


def calculateavg(bitcoin_history):
    summ=0
    for price in bitcoin_history:
        price= price.replace(',', '')
        #print(float(price))
        summ = summ+float(price)
        
    return summ/10

        
def get_avg():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        bitcoin_history.append(price)

       

        
        if len(bitcoin_history) == 10:
            avg = calculateavg(bitcoin_history)
            return avg

        # Sleep for 1 minutes 
        time.sleep(1 * 60)
    

latest_price = get_latest_bitcoin_price()

app = Flask(__name__)

@app.route("/") 
def main():
    global total, counter, latest_price
   
    if latest_price != get_latest_bitcoin_price():
        latest_price = get_latest_bitcoin_price()
    output = "The current Price of BitCoin is: " + latest_price + " USD "
    output += "BitCoin Average price for the last 10 minutes: " + get_avg()._str_() + " USD"
    return output


if __name__ == "__main__":
    # run app
    app.run(host="0.0.0.0")