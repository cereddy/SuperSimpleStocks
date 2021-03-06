# SuperSimpleStocks
An exercice for implementing a simplified stocks manager. Implementation is in Python 3.

# Description: 
- For a given stock: 
  - Given a market price as input, calculate the dividend yield,
  - Given a market price as input, calculate the P/E ratio,
  - Record a trade, with timestamp, quantity of shares, buy or sell indicator and trade price,
  - Calculate Volume Weighted Stock Price based on trades in past 15 minutes.\\
- Calculate the All-Share index using the geometric mean of prices for all stocks.


# Remarks:
- Sample Data for stocks is stored in the form of a dictionary.
- Records of the trades are stored in a list of dictionaries.
- When no trades have been recorded for a given stock in the last 15 minutes, an exception is raised.
When computing the all-share index, the prices is calculated using last 15 minutes trades. If user provides their
own prices (for even part of the stocks) they will be used in place.

- The code does not handle these issues :
  - Asynchronous behaviour (for multiple parallel accesses for instance..),
  - Persistence of data,
  - Multithreading for code performence.
