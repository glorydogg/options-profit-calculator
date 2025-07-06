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
                profit = (self.premium * self.contract_size) - ((market_price - self.strike_price) * self.contract_size) 
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


    def calculate_breakeven(self):
        if self.option_type.lower() == 'long call':
            breakeven =  self.strike_price + self.premium
        
        elif self.option_type.lower() == 'short call':
            breakeven = self.strike_price + self.premium
        
        elif self.option_type.lower() == 'long put':
            breakeven = self.strike_price - self.premium
        
        elif self.option_type.lower() == 'short put':
            breakeven = self.strike_price - self.premium
        return breakeven
    
    def max_profit(self):
        if self.option_type.lower() == 'long call':
            return float('inf')
        elif self.option_type.lower() == ' short call':
            return self.premium * self.contract_size
        elif self.option_type.lower() == 'long put':
            return (self.strike_price - self.premium) * self.contract_size
        elif self.option_type.lower() == 'short put':
            return  self.premium * self.contract_size
        

    def max_loss(self):
        if self.option_type.lower() == 'long call':
            return self.premium * self.contract_size
        elif self.option_type.lower() == ' short call':
            return float('inf')
        elif self.option_type.lower() == 'long put':
            return self.premium * self.contract_size
        elif self.option_type.lower() == 'short put':
            return (self.strike_price - self.premium) * self.contract_size    
        
    def summary(self):
        return{
            "Option Type": self.option_type,
            "Strike Price": self.strike_price,
            "Premium": self.premium,
            "Contract Size": self.contract_size,
            "Market Price": self.market_price,
            "Profit": self.calculate_profit(self.market_price),
        }
       





        

