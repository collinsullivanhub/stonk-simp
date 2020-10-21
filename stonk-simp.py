import yfinance as yf
import xlsxwriter
import time
import os
import sys
import json


class Stonky:
    """
    A representation of a stock and associated data
    Attributes:
        ticker(string)
    """
    def __init__(self, ticker):
        self.ticker = ticker


    def pull_stock_dividends(self):
        print("Stock historical dividends: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.dividends)


    def pull_stock_info(self):
        stonk = yf.Ticker(self.ticker)
        print("Stonk Information: {}".format(stonk.info['longName']))
        print(stonk.info['longBusinessSummary'] + "\n\n")
        print("Sector: " + stonk.info['sector'])
        print("Previous Close: " + str(stonk.info['previousClose']))
        print("Two-Hundred Day Average: " + str(stonk.info['twoHundredDayAverage']))
        print("Annual Dividend: " + str(stonk.info['trailingAnnualDividendRate']))
        print("Average 10-day Volume: " + str(stonk.info['averageVolume10days']))
        print("P/E Ratio: " + str(stonk.info['trailingPE']))
        print("Market Cap: " + str(stonk.info['marketCap']))

        print("Dividend Rate:")
        print(calculate_rate(stonk.info['trailingAnnualDividendRate'], stonk.info['previousClose']))
        dividend_rate = calculate_rate(stonk.info['trailingAnnualDividendRate'], stonk.info['previousClose'])
        print("\n\n")
        print("Calculating...")
        if stonk.info['trailingPE'] < 30 and dividend_rate > 2:
            print("This stonk is a STRONG BUY according to the stonk-simp score bot!")
        elif stonk.info['trailingPE'] < 30 and dividend_rate < 2:
            print("This stonk is a BUY according to the stonk-simp score bot!")
        elif stonk.info['trailingPE'] < 50 and dividend_rate < 2:
            print("This stonk has a low PE ratio but a low dividend... NEUTRAL rating!")
        else:
            print("This stonk is not considered a buy, further research may be required!")
            


    def pull_stock_financials(self):
        print("Stock Fincials: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.financials)


    def pull_stock_major_holders(self):
        print("Major holders: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.major_holders)


    def pull_stock_balance_sheet(self):
        print("Balance Sheet: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.balance_sheet)


    def pull_stock_cashflow(self):
        print("Cashflow: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.cashflow)


    def pull_stock_earnings(self):
        print("Earnings: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.earnings)


    def pull_analysis(self):
        print("Recommendations: ")
        stonk = yf.Ticker(self.ticker)
        print(stonk.recommendations)


    @classmethod
    def get_user_input(self):
        while 1:
            try:
                ticker = input('Enter ticker: ')
                return self(ticker)
            except:
                print('Invalid input!')
                continue


def calculate_rate(dividend, price):
    return dividend / price * 100
    

if __name__ == '__main__':
    print('''
   _   _   _   _   _     _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ 
 ( S | t | o | n | k ) ( S | i | m | p | s )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ 
                REEEEEEEEEEE
               Collin Sullivan
                    2020
    ''')

    ticker_one = Stonky.get_user_input()
    workbook = xlsxwriter.Workbook('stonky_{}_analysis.xlsx'.format(ticker_one))
    worksheet = workbook.add_worksheet()
    global row
    global col
    row = 0
    col = 0

    data_input = input('''Select an option:
    1. Show me the simp-data
    2. Give me a simp-score
    ''')
    if data_input == "1":
        ticker_one.pull_stock_dividends()
        ticker_one.pull_stock_major_holders()
        ticker_one.pull_analysis()
        ticker_one.pull_stock_info()


    
