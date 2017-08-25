
from generateMockTradeRecord import tradeRecord
from generateSampleData import sampleData
from SuperSimpleStocks import SuperSimpleStocks
import time
ssStocks = SuperSimpleStocks(sampleData,tradeRecord)

print("Recording a trade:\n")
result = ssStocks.recordTrade('TEA','buy',43,110)
print('\n \n ')


results = ssStocks.getDividendYield('POP', 101.4)
print("Result from ssStocks.getDividendYield('POP', 101.4):\n{}".format(results))
print('\n \n')


results = ssStocks.getPERatio('GIN', 120.9)
print("Result from ssStocks.getPERation('GIN', 120.9:\n{}".format(results))
print('\n \n')


result = ssStocks.AllShareIndex()
print("result from ssStocks.AllShareIndex(): \n{}".format(result))

