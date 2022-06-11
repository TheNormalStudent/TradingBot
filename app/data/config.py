from environs import Env

env = Env()
env.read_env()

API_KEY = env.str('API_KEY')     # api key to login to binance
API_SECRET = env.str('API_SECRET')   # api SECRET to login to binance
TRADING_LIST = env.list('TRADING_LIST')
