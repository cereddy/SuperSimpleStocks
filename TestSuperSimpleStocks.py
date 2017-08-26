import unittest
from generateMockTradeRecord import generateRecord
from generateSampleData import sampleData
from SuperSimpleStocks import SuperSimpleStocks
from datetime import datetime as dt

class TestSuperSimpleStocks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._ssStocks = SuperSimpleStocks(sampleData, generateRecord())

    def test_getDividendYield(self):
        stockSymbol = 'TEA'
        marketPrice = 102.5
        result = TestSuperSimpleStocks._ssStocks.getDividendYield(stockSymbol, marketPrice)
        self.assertEqual(result, 0.0)

        stockSymbol = 'POP'
        marketPrice = 100
        result = TestSuperSimpleStocks._ssStocks.getDividendYield(stockSymbol,marketPrice)
        self.assertEqual(result, 0.0008)

        stockSymbol = 'ALE'
        marketPrice = 40
        result = TestSuperSimpleStocks._ssStocks.getDividendYield(stockSymbol,marketPrice)
        self.assertEqual(result, 0.00575)

        stockSymbol = 'GIN'
        marketPrice = 100
        result = TestSuperSimpleStocks._ssStocks.getDividendYield(stockSymbol,marketPrice)
        self.assertEqual(result, 0.02)

        stockSymbol = 'JOE'
        marketPrice = 130
        result = TestSuperSimpleStocks._ssStocks.getDividendYield(stockSymbol,marketPrice)
        self.assertEqual(result, 0.001)

    def test_getPERatio(self):
        stockSymbol = 'TEA'
        marketPrice = 120
        result = TestSuperSimpleStocks._ssStocks.getPERatio(stockSymbol,marketPrice)
        self.assertIsNone(result)

        stockSymbol = 'POP'
        marketPrice = 120
        result = TestSuperSimpleStocks._ssStocks.getPERatio(stockSymbol,marketPrice)
        self.assertEqual(result, 1500)

        stockSymbol = 'ALE'
        marketPrice = 138
        result = TestSuperSimpleStocks._ssStocks.getPERatio(stockSymbol,marketPrice)
        self.assertEqual(result, 600)

        stockSymbol = 'GIN'
        marketPrice = 103
        result = TestSuperSimpleStocks._ssStocks.getPERatio(stockSymbol,marketPrice)
        self.assertEqual(result, 1287.5)

        stockSymbol = 'JOE'
        marketPrice = 39
        result = TestSuperSimpleStocks._ssStocks.getPERatio(stockSymbol,marketPrice)
        self.assertEqual(result, 300)

    def Test_recordTrade(self):

        stockSymbol = 'TEA'
        order = 'buy'
        quantityShares = 34
        tradePrice = 120.3
        date_1 = dt.now()
        result = TestSuperSimpleStocks._ssStocks.recordTrade(stockSymbol, order, quantityShares, tradePrice)
        self.assertEqual(result['order'], order)
        self.assertEqual(result['stock'], stockSymbol)
        self.assertEqual(result['quantityShares'], quantityShares)
        self.assertEqual(result['tradePrice'], tradePrice)
        self.assertGreater(result['timestamp'], date_1)
        self.assertGreater(dt.now(), result['timestamp'])

    def Test_computeVWSP(self):
        stockSymbol = 'TEA'
        result = TestSuperSimpleStocks._ssStocks.computeVWSP(stockSymbol)
        self.assertEqual(result, 120)

        stockSymbol = 'POP'
        result = TestSuperSimpleStocks._ssStocks.computeVWSP(stockSymbol)
        self.assertEqual(result, 120)

    def Test_AllShareIndex(self):
        result = TestSuperSimpleStocks._ssStocks.AllShareIndex()
        self.assertEqual(result, 121.26747529884128)
if '__name__' == '__main__':
    unittest.main()

