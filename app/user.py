from distutils.command import config


from data.config import API_KEY, API_SECRET
from exchange_managers.binance_manager import Binance_manager
class User:
    def __init__(self):
        self.__api_secret = API_KEY
        self.__api_public = API_SECRET
        self.trading_list = 0
        self.binance_manager = Binance_manager(self.__api_public, self.__api_secret)