class NobitexUrlsClass:

    @staticmethod
    def getOrderBookUrl(symbol='USDTIRT'):
        url = r'https://api.nobitex.ir/v2/orderbook/'
        url_ordBooks = url + symbol
        return url_ordBooks

    @staticmethod
    def getTradesUrl(symbol='USDTIRT'):
        url = r'https://api.nobitex.ir/v2/trades/'
        url_trades = url + symbol
        return url_trades

    @staticmethod
    def getOhlcUrl(symbol, aTimeResolution, aStartTimestamp, aEndTimestamp):
        url = r'https://api.nobitex.ir/market/udf/history'
        txt = "?symbol={symbol}&resolution={res}&from={start}&to={end}".format(symbol = symbol, res = aTimeResolution , start = aStartTimestamp, end= aEndTimestamp)
        url_trades = url + txt
        return url_trades

    @staticmethod
    def getAddOrderUrl():
        url = r'https://api.nobitex.ir/market/orders/add'
        return url

    @staticmethod
    def getProfileUrl():
        url= r'https://api.nobitex.ir/users/profile'
        return url

    @staticmethod
    def getWallets():
        url = r'https://api.nobitex.ir/users/wallets/list'
        return url

    @staticmethod
    def getBalanceUrl():
        url = r'https://api.nobitex.ir/users/wallets/balance'
        return url
    @staticmethod
    def getOrderStatusUrl():
        url = r'https://api.nobitex.ir/market/orders/status'
        return url

    @staticmethod
    def getOrderUpdateUrl():
        url = r'https://api.nobitex.ir/market/orders/update-status'
        return url

    @staticmethod
    def getOrderListUrl():
        url = r'https://api.nobitex.ir/market/orders/list'
        return url
