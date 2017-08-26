#!/usr/bin/env python3


import pandas as pd


class Candle():

    def Build(self, csvFile, tf):
        # csv format: 'EURUSD-2016-01.csv'
        # tf format: '15Min', '1H'
        data_frame = pd.read_csv(csvFile, names=['Symbol', 'Date_Time', 'Bid', 'Ask'], index_col=1, parse_dates=True)
        data_frame.head()
        data_ask = data_frame['Ask'].resample(tf).ohlc()
        data_bid = data_frame['Bid'].resample(tf).ohlc()
        data_ask.head()
        data_bid.head()
        data_ask_bid = pd.concat([data_ask, data_bid], axis=1, keys=['Ask', 'Bid'])
        return data_ask_bid
