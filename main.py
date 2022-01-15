import argparse
import backtrader
import pandas as pandas
from TestStrategy import TestStrategy
import json
import yfinance as yf
import datetime
from Conditioner import *

#dates
today = datetime.date.today()

start_delta = datetime.timedelta(days=20)

days20 = today - start_delta

print(today.strftime("%Y-%m-%d"))

print(days20)

mylist = []

mydict = {}

trendingup = []
trendingdown = []

with open('constituents_json.json') as json_file:
    mylist = json.load(json_file)

def runtrategy():

    for items in mylist:
        print("Calculating trend for ticker {0}".format(items["Symbol"]))
        try:
            hist = yf.Ticker("MMM").history(start='2021-01-06', end='2021-03-08', interval="1d")

            if hist is not None:
                print(hist)
                runcerebro(hist)

                if getvalue() == "yes":
                    trendingup.append(items["Symbol"])
                    print("Adding ticker to trending up")
                else:
                    trendingdown.append(items["Symbol"])
                    print("Adding ticker to trending down")

            clearvalue()
            clearlimit()
        except:
            print("something went wrong: Going next symbol")

def runcerebro(data):
    maincontrol = backtrader.Cerebro()

    data = backtrader.feeds.PandasData(dataname=data)

    mystrategy = TestStrategy

    maincontrol.addstrategy(mystrategy)

    maincontrol.adddata(data)

    maincontrol.run()
    maincontrol.plot()

def summerize():
    print("This is the trending up tickers: {0}".format(trendingup))

    print("This is the trending down tickers {0}".format(trendingdown))

runtrategy()

summerize()
