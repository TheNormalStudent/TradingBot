from data.config import API_KEY, API_SECRET, TRADING_LIST
from exchange_managers.binance_manager import Binance_manager


class User:
    def __init__(self):
        self.__api_public = API_KEY
        self.__api_secret = API_SECRET
        self.trading_list = TRADING_LIST
        self.binance_manager = Binance_manager(self.__api_public,
                                               self.__api_secret, self.trading_list) # noqa
