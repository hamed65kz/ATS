class BinanceUrlsClass:

    @staticmethod
    def getOrderBookUrl(symbol='BTCUSDT'):
        url = r''
        url_ordBooks = url + symbol
        return url_ordBooks

    @staticmethod
    def getTradesUrl(symbol='BTCUSDT',count=20):
        url = r'https://api.binance.com/api/v3/trades?symbol='
        url_trades = url + symbol+'&limit='+str(count)
        return url_trades

    @staticmethod
    def getOhlcUrl(symbol, aTimeResolution, aStartTimestamp, aEndTimestamp):
        url = r''
        txt = ""
        url_trades = url + txt
        return url_trades

    @staticmethod
    def getAddOrderUrl():
        url = r''
        return url

    @staticmethod
    def getProfileUrl():
        url= r''
        return url

    @staticmethod
    def getWallets():
        url = r''
        return url

    @staticmethod
    def getBalanceUrl():
        url = r''
        return url
    @staticmethod
    def getOrderStatusUrl():
        url = r''
        return url

    @staticmethod
    def getOrderUpdateUrl():
        url = r''
        return url

    @staticmethod
    def getOrderListUrl():
        url = r''
        return url
