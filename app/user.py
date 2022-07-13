from data.config import API_KEY, API_SECRET
from exchange_managers.binance_manager import BinanceManager


class User:
    def __init__(self):
        self.__api_public = API_KEY
        self.__api_secret = API_SECRET
        self.binance_manager = BinanceManager(self.__api_public,
                                               self.__api_secret) # noqa
