import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
# Import the backtrader platform
from Conditioner import *
import backtrader as bt

# Create a Stratey
class TestStrategy(bt.Strategy):

    counterdown = 0

# The moving averages
    params = ({
        'fast': 10,  # period for the fast moving average
                       })

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.fast_moving_average = bt.indicators.EMA(period=self.params.fast, plotname="20 EMA")



    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])
        # previous close less than the previous close

        if self.dataclose[0] > self.fast_moving_average[0] and getlimit() != 1:
            self.counterdown = 0
            setvalue()
        elif self.fast_moving_average[0] > self.dataclose[0] and self.counterdown != 3:
            self.counterdown += 1
        elif self.counterdown == 3:
            setlimit()
            clearvalue()




