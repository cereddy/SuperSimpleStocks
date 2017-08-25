
# Sample Data written by hand.
# The Sample Data will be stored in the form of a dict. This emulates access to API (JSON) for instance.

listSymbols = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
listTypes = ['Common', 'Common', 'Common', 'Preferred', 'Common']
listLastDiv = [0., 0.08, 0.23, 0.08, 0.13]
listFixedDiv = [None, None, None, 0.02, None]
listParValues = [100, 100, 60, 100, 250]

sampleData = {}
for i,stockSymbol in enumerate(listSymbols):
    dictAux = {'type'          :listTypes[i],
               'lastDividend'  :listLastDiv[i],
               'fixedDividends':listFixedDiv[i],
               'parValue'      :listParValues[i]}
    sampleData[stockSymbol] = dictAux
