# Short testing script for runePriceChecker.py

import json
import urllib

urlAirRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=a&page=1'
urlBodyRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=b&page=1'
urlEarthRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=e&page=1'
urlFireRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=f&page=1'
urlWaterRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=w&page=1'
urlChaosRune = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=32&alpha=c&page=1'


urlArray = [urlAirRune,urlBodyRune,urlChaosRune,urlEarthRune,urlFireRune,urlWaterRune]
apiIndex = [0,2,2,0,1,1]

for i in range(0,len(urlArray)):
    response = urllib.urlopen(urlArray[i])
    data = json.loads(response.read())
    itemName = data["items"][apiIndex[i]]["name"]
    itemPrice = data["items"][apiIndex[i]]["current"]["price"]
    print('%s current GE price is %s gp' % (itemName, itemPrice))
    # prices[i] = data["items"][apiIndex[i]]["current"]["price"]