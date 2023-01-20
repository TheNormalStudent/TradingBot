from data.db_manager import DbManagerCl
import pandas
import ta 

class TaManager:
    def __init__(self):
        self.manager = DbManagerCl()
    
    def rsi_analyse(self,  ticker, tics, date):
        data = self.manager.get_by_date(ticker=ticker, tics=tics, date=date)
        # print(data)
        df = self.manager.to_pandas_dataframe(data)

        # rsi = ta.momentum.rsi()
        # df['RSI'] = ta.add_momentum_ta()

        print(df)

