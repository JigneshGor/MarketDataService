import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib

matplotlib.rcParams.update({'font.size': 9})

tickers = ['AAPL']

def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter

date_converter = bytedate2num("%Y%m%d")

def graphData(ticker):
    try:
        data_file = ticker + '_1y.txt'
        stock_date, close_price, high_price, low_price, open_price, volume = np.loadtxt(data_file, delimiter=',', unpack=True, converters={0: date_converter})

        fig = plt.figure()
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
        ax1.plot(stock_date, open_price)
        ax1.plot(stock_date, high_price)
        ax1.plot(stock_date, low_price)
        ax1.plot(stock_date, close_price)
        ax1.grid(True)

        plt.ylabel('Stock Price')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        ax2 = plt.subplot2grid((5,4), (4,0), sharex=ax1, rowspan=1, colspan=4)
        ax2.bar(stock_date, volume)
        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(True)
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(90)

        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.suptitle(ticker + ' Stock Price')
        plt.setp(ax1.get_xticklabels(), visible=False)

        plt.subplots_adjust(left=0.09,bottom=.16,right=.94,top=.94,wspace=.20,hspace=0)
        plt.show()

    except Exception as e:
        print("Exception:", e)

for ticker in tickers:
    graphData(ticker)
