
#My API Key

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

API_KEY = "VMJ3EI4FQQYU6323"
listOfTickers = ["ASX:CBA"]    # , "ASX:CBA", "ASX:MP1"

# Chose your output format, or default to JSON (python dict)
ts = TimeSeries(API_KEY, output_format='pandas')
ti = TechIndicators(API_KEY)

# Get the data, returns a tuple
# data is a pandas dataframe, meta_data is a dict
for ticker in listOfTickers:

    aapl_data, aapl_meta_data = ts.get_daily(symbol=ticker, outputsize='full')
    # aapl_sma is a dict, aapl_meta_sma also a dict
    aapl_ema, aapl_meta_sma = ti.get_ema(symbol=ticker)
    # generate output file based on current ticker name. Removes "ASX:"
    outfilename = "D:/00git/alphaAdvantageStocks/TestDeleteOutput" + ticker.replace('ASX:', '') + ".pkl"
    print(outfilename)
    with open(outfilename, 'w') as outfile:
        aapl_data.to_pickle(outfilename)



print(aapl_data, type(aapl_data))

# # Visualization
# figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
# aapl_data['4. close'].plot()
# plt.tight_layout()
# plt.grid()
# plt.show()




# #URL to access our info
# #stock symbols(Required)
# #datatype(Optional) can be JSON(Default) or CSV
# #outputsize can be compact(limits to 100 data points) or full
# #interval(Required)  can be 1, 5, 15, 30, 60 minutes
# URL = "https://www.alphavantage.co/query?"
# INTRA_DAY_URL = "function=TIME_SERIES_INTRADAY"
# DAILY_URL = "function=TIME_SERIES_DAILY"
# SYMBOLS = ["AAPL"]
# SIZE = "compact"
# INTERVAL = "5min"
#
# #Constants used to extract data
# OPEN = "1. open"
# HIGH = "2. high"
# LOW = "3. low"
# CLOSE = "4. close"
# VOL = "5. volume"
#
#
# #function for making request to Alpha Advantage. Symbol is expected to be stock Ticker symbol
# def makeIntraDayRequest(self, symbol = None):
# 	req = URL + INTRA_DAY_URL + '&symbol=' + s + '&interval=' + INTERVAL + '&outputsize=' + SIZE + '&apikey=' + API_KEY
# 	data = requests.get(req)
# 	data = data.json()
# 	return data
#
# #function for making request to Alpha Advantage. Symbol is expected to be stock Ticker symbol
# def makeDailyRequest(self, symbol = None):
# 	req = URL + DAILY_URL + '&symbol=' + s + '&outputsize=' + SIZE + '&apikey=' + API_KEY
# 	print("Making request to: " + req)
# 	data = requests.get(req)
# 	data = data.json()
# 	return data
#
# #Function used to save to a file. Symbol: stock ticker symbol. Data: information to save
# def saveFile(symbol, data):
# 	filename = s + ".json"
# 	with open(filename, 'w') as outfile:
# 		json.dump(data, outfile, indent=4)
#
# #Function that does things
# def processData(s, data):
# 	#Selects the data
# 	entries = data["Time Series (Daily)"]
#
# 	opening = {}
# 	highs = {}
# 	lows = {}
# 	closing = {}
# 	volume = {}
# 	#Each entry has a time stamp for a key and a dict of values
# 	for date, entry in entries.items():
# 		opening[date] = entry["1. open"]
# 		highs[date] = entry["2. high"]
# 		lows[date] = entry["3. low"]
# 		closing[date] = entry["4. close"]
# 		volume[date] = entry["5. volume"]
#
# 	#use our function to format data into a trace object used for plotly
# 	ohlcData = makeOhlcTrace(
# 		s,
# 		[*entries],
# 		[*opening.values()],
# 		[*highs.values()],
# 		[*lows.values()],
# 		[*closing.values()]
# 	)
# 	return ohlcData
#
# #Converts dict with (Key, value) pairs into trace object with x=key, y=value
# #Used for plotly line charts
# def makeLineTrace(dict, label, type):
# 	trace = go.Scatter(
# 		x = [*dict],
# 		y = [*dict.values()],
# 		name = label,
# 		mode = type
# 	)
#
# 	return trace
#
# #Converts 5 lists into trace object
# #Used for plotly stock charts
# def makeOhlcTrace(label,dates, opens, highs, lows, closes):
# 	trace = go.Ohlc(
# 		name=label,
# 		x=dates,
# 		open=opens,
# 		high=highs,
# 		low=lows,
# 		close=closes
# 	)
#
# 	return trace
#
#
# traces = []
# for s in SYMBOLS:
# 	data = makeDailyRequest(s)
# 	saveFile(s, data)
# 	traces.append(processData(s, data))
#
# py.iplot(traces, filename='stock_data')




