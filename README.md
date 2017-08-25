# SuperSimpleStocks
An exercice for implementing a simplified stocks manager.

# Features: 
For a given stock: 
  - Given a market price as input, calculate the dividend yield,
  - Given a market price as input, calculate the P/E ratio,
  - Record a trade, with timestamp, quantity of shares, buy or sell indicator and trade price,
  - Calculate Volume Weighted Stock Price based on trades in past 15 minutes.
 Calculate the All-Share index using the geometric mean of prices for all stocks.

# Some choices: 
When no trades have been recorded for a given stock in the last 15 minutes, an exception is raised.
When computing the all-share index, the prices a calculated using last 15 minutes trades. If user provides their
own prices (for even some of the stocks) they will be used in place.
# Not handled: 
- Asynchronous behaviour, for multiple parallel accesses for instance..
- Data access instead of sample data
