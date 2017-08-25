from datetime import datetime as dt
from datetime import timedelta as tdelta

class SuperSimpleStocks:
    
    def __init__(self, sampleData={}, histTrade=[]):
        """
        :param sampleData: gathering the data for the Global Beverage Corporation Exchange (of type
        dict, with the following structure: {stockSymbol1:{'type':type1, 'lastDividend':..},stockSymbol2:{..},..}
        :param histTrade: A historic of the recorded trade (of type list, each element of the list is a dict
        in the form {'timestamp':.., 'stock':.., 'orderType':.., ..})
        :return:
        """
        self.sampleData = sampleData
        self.histTrade = histTrade


    def getDividendYield(self, stockSymbol, marketPrice):
        """
        Given a stock and a market price, returns the dividen yield.
        :param stockSymbol: from those available in sampleData
        :param marketPrice: has to be greater than zero
        :return: Dividen Yield, which is calculater by one of two formula,
        depending on the type of the stock (preferred or common)
        """
        if(marketPrice == 0):
            raise ValueError("Received zero for marketPrice value. Expecting stricly positive values.")
        if(marketPrice < 0):
            raise ValueError("Received negative value for marketPrice. Expecting stricly positive values.")

        stockData = self.sampleData.get(stockSymbol, None)
        if(stockData is None):
            raise ValueError("The stock {} was not found in the data".format(stockSymbol))
        type = stockData.get('type', None)
        if(type == "common"):
            lastDividend = stockData.get("lastDividend", None)
            if(lastDividend is not None):
                return lastDividend / marketPrice
            else:
                raise KeyError("LastDividend could not be found in the data "
                               "for the stock {}".format(stockSymbol))
        elif(type == "preferred"):
            fixedDividend = stockData.get("fixeDividend", None)
            parValue = stockData.get("parValue",None)
            if(fixedDividend is None):
                raise KeyError("Fixed Dividend could not be found in the data "
                               "for the stock {}".format(stockSymbol))
            if(parValue is None):
                raise KeyError("Par Value could not be found in the data for the "
                               "stock {}".format(stockSymbol))
            return fixedDividend * parValue / marketPrice

    def getPERatio(self, stockSymbol, marketPrice):
        """

        :param stockSymbol: from those available in sampleData
        :param marketPrice: has to be greater than zero
        :return: Price earnings Ratio, which is computed by formula: priceMarket/Dividend.
        Dividend is taken to be LastDividend
        """
        if(marketPrice == 0):
            raise ValueError("Received zero for marketPrice value. Expecting stricly positive values.")
        try:
            lastDividend = self.sampleData[stockSymbol]['lastDividend']
        except:
            raise KeyError("Could not find Last Dividend for the stock {}".format(stockSymbol))
        if(lastDividend == 0):
            print("Last dividend for stock {} is 0. So P/E Ratio is not computed")
        else:
            return marketPrice/lastDividend

    def recordTrade(self, stockSymbol, order, quantityShares, tradePrice):
        """
        Record a trade, with timestamp, quantity of shares, buy or sell indicator and trade price.
        A confirmation is made in a print form
        :param stockSymbol: has to be recognised in the data
        :param order: must either be "buy" or "sell"
        :param tradePrice: price, in pennies
        :return:
        """
        order = order.lower()# letters in lower case
        if(order != "buy" and order !="sell" ): # check if order is correct (either buy or sell)
            raise ValueError('Order type not recognized. "buy" and "sell '
                             'are handled. You entered {}" '.format(order))
        if(stockSymbol not in self.sampleData):
            raise ValueError('The stock you want to {} is not in the data.'.format(order))
        if(int(abs(quantityShares))!= quantityShares):
            raise ValueError('Expecting quantity of shares to be a positive integer. You entered '
                             '{}'.format(quantityShares))
        if(tradePrice <= 0):
            raise ValueError('Exepecting trade Price to be a stricly positive value')

        newTrade = {"stock":stockSymbol, "orderType":order,"quantityShares":quantityShares,
                               "tradePrice":tradePrice, "timestamp":dt.now()}
        try:
            self.histTrade.append(newTrade)
        except Exception as e:
            print("something went wrong with the trade.\n" \
            " ******** TRADE ORDER WAS NOT RECORDED ********.")
            raise
        # Print a confirmation:
        print("ORDER RECORDED: \n"
              "     TIMESTAMP   :  {}\n"
              "     STOCK TRADED:  {} \n"
              "     ORDER TYPE :   {}\n"
              "     TRADE PRICE :  {}"
              ".".format(newTrade["timestamp"].strftime("%A, %d. %B %Y %I:%M%p"), stockSymbol,order, tradePrice))

    def computeVWSP(self, stockSymbol):
        """
        Computes the Volume Weighted Stock Price based on trades in past 15 minutes
        :param stockSymbol: Must be recognised from the data in sampleData
        :return:
        """
        currentTime = dt.now()
        deltaTime = tdelta(minutes=15)
        gen = ((trade['tradePrice'], trade['quantityShares']) for
                trade in self.histTrade if (trade['stock'] == stockSymbol)
                                            & (currentTime-trade['timestamp']< deltaTime))
        res = 0.
        totalQuantity = 0.
        for price, quantity in gen:
            res += price * quantity
            totalQuantity += quantity
            # for higher precision, consider using numpy:
        # for price, quantity in gen:
        #   prices.append(price)
        #  quantities.append(quantity)
        #result = numpy.average(prices, 0, quantities) . Note that numpy specific types could also be used
        if totalQuantity== 0:
            raise ValueError("The stock {stock} has not been traded during the last 15 minutes.".format(stock=stockSymbol))
            #prossibly give other information, like the last trade price for that given stock if exists
        return res / totalQuantity

    def AllShareIndex(self,**kwargs):
        """
        Computes the Prices Weighted Index for the Global Beverage Corporation Exchange.
        The prices can be forwarded as input. If not forwarded, the prices are computed using
        the computeVWSP method. If partially forwarded (i.e. for part of the stocks), only the
        none forwared ones are computed
        :param kwargs: a dict of the form: {stock1: price, stock2:price, ..}
        :return:
        """

        result = 1.
        if(self.sampleData.keys() == {}):
            raise Exception('No stocks in the data.')
        for k in self.sampleData.keys():
            try:
                vwsp_k = kwargs.get(k,self.computeVWSP(k))
                result = result*vwsp_k
            except ValueError as e:
                raise ValueError("computeVWSP for stock {stock} could not be computed: no trades of {stock} in the last 15 minutes".format(stock=k))
        return (result)**(1./len(self.sampleData))
        # for higher precision, consider using scipy:
        # for k in self.sampleData.key():
        #    prices.append(self.computeVWSP(k))
        # result = scipy.stats.mstats.gmean(prices). Note that numpy types could also be used.














