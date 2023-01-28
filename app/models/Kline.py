

class Kline:
    def __init__(self, open_price_var, high_price_var, low_price_var, close_price_var)->None:
        self.open_price = open_price_var
        self.high_price = high_price_var
        self.low_price = low_price_var
        self.close_price = close_price_var
    
kline = Kline(1, 2, 3, 4)
print(kline.close_price)