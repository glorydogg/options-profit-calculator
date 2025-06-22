class Options:
    def __init__(self, premium, strike_price, contract_size, option_type, market_price):
        self.premium = premium
        self.strike_price = strike_price
        self.contract_size = contract_size
        self.option_type = option_type
        self.market_price = market_price

    def calculate_profit(self, market_price):
        if self.option_type.lower() == 'long call':
            profit = (market_price - self.strike_price - self.premium) * self.contract_size
            return profit
        
        elif self.option_type.lower() == 'short call':
            if market_price > self.strike_price:
                profit = ((market_price - self.strike_price) * self.contract_size) - (self.premium * self.contract_size)
            else:
                profit = self.premium * self.contract_size

        elif self.option_type.lower() == 'long put':
            profit = (self.strike_price - market_price - self.premium) * self.contract_size
        
        elif self.option_type.lower() == 'short put':
            if market_price < self.strike_price:
                profit = (self.premium * self.contract_size) - ((self.strike_price - market_price) * self.contract_size)
            else:
                profit = self.premium * self.contract_size


        return profit


    def calculate_breakeven(self, market_price):
        if self.option_type.lower() == 'long call':
            breakeven =  self.strike_price + self.premium
        
        elif self.option_type.lower() == 'short call':
            breakeven = self.strike_price + self.premium
        
        elif self.option_type.lower() == 'long put':
            breakeven = self.strike_price - self.premium
        
        elif self.option_type.lower() == 'short put':
            breakeven = self.strike_price - self.premium

        return breakeven



        
option1 = Options(
    premium=3,
    strike_price=50,
    contract_size=100,
    option_type='long call',
    market_price=55
)

profit = option1.calculate_profit(option1.market_price)
print("Profit:", profit)

breakeven = option1.calculate_breakeven(option1.market_price)
print("Breakeven:", breakeven)
