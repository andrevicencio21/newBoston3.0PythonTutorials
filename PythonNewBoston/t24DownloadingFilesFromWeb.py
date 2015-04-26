from urllib import request

# http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=3&e=25&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv
testUrl = r'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=3&e=25&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv'

def downloadStockData(csvUrl):
    response = request.urlopen(csvUrl)
    csv = response.read()
    csvStr = str(csv)
    lines = csvStr.split("\\n")
    destination = r'goog.csv'
    fw = open(destination, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()
    print("Write Complete, File CLosed")

downloadStockData(testUrl)
    
    

