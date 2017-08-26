
"""
This file generate a list of trades (tradeRecord) that occured during the last 20 minutes
Each trade is of dict type, in the form: {'timestamp':a_datetime,'stock':a_stock,
                                            'quantityShares':a_quantityShare, 'orderType':a_ordertype,
                                            'tradePrice':a_trade_price}
"""

from datetime import datetime as dt
from datetime import timedelta as deltat

def generateRecord():
    tradeRecord = []
    dateNow = dt.now()
    initPrice = [100., 105., 102., 95., 99.]
    variation = [1,2,3,-1,1,-2]
    for i in range(-20,0,):
        for ui, stock in enumerate(['TEA','POP', 'ALE', 'GIN', 'JOE']):
            if(i % 3 == 0):
                orderType = 'buy'
            else:
                orderType = 'sell'
            #newDate = dateNow + deltat(minutes=i)
            newMockTrade = {'timestamp':(dateNow-deltat(minutes=i)), 'stock':stock,
                            'orderType':orderType, 'tradePrice':110. - variation[ui]*i,
                            'quantityShares': i*60%23}
            tradeRecord.append(newMockTrade)
            newMockTrade = {}
    return tradeRecord
