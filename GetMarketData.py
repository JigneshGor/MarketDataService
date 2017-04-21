from urllib.request import urlopen
import time
import datetime
import threading, time

tickers = ['FB', 'GOOG', 'MSFT', 'AMZN', 'AAPL', 'VDE', 'JDST', 'JNUG', 'ERX', 'ERY', 'UCO', 'SCO', 'UGAZ', 'DGAZ']
ranges = ['1d'] #, '10d', '20d', '1y']

def get_ticker_data(ticker, range):
     try:
        print("Currently Pulling Stock:", ticker)
        print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

        data_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + ticker + '/chartdata;type=quote;range=' + range + '/csv'
        ticker_data_file = ticker + '_' + range + '.txt'

        try:
            current_records = open(ticker_data_file, 'r').read()
            split_current_records = current_records.split('\n')
            latest_record = split_current_records[-2] # Since last line (-1) is blank
            latest_record_datetime = latest_record.split(',')[0]
        except:
            latest_record_datetime = 0 # if file doesn't exists, last record time is 0

        data_file = open(ticker_data_file, 'a')
        data = urlopen(data_url).read()
        rows_data = data.decode('utf8').split('\n')

        for row in rows_data:
            row_data = row.split(',')
            if len(row_data) == 6:
                if 'values' not in row:
                    if int(row_data[0]) > int(latest_record_datetime):
                        data_file = open(ticker_data_file, 'a')
                        data = row + '\n'
                        data_file.write(data)

        data_file.close()

        print('Successfully pulled the data:', ticker)
        # print('sleeping...')
        print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        # time.sleep(1)

     except Exception as e:
        print('get_ticker_data:'), str(e)

for ticker in tickers:
    for range in ranges:
        threading.Thread(target=get_ticker_data, args=(ticker, range)).start()


