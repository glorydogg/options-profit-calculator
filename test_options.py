import unittest
from options_calc_main import Options

class TestOptions(unittest.TestCase):
    def test_long_call_profit(self):
        option = Options(
            premium=2,
            strike_price=50,
            contract_size=100,
            option_type='long call',
            market_price=60
        )
        expected_profit = (60 - 50 - 2) * 100  # = 800
        self.assertEqual(option.calculate_profit(60), expected_profit)

    def test_short_call_profit(self):
        option2 = Options(
            premium=5,
            strike_price=100,
            contract_size=100,
            option_type='short call',
            market_price=120
        )
        expected_profit = (5 * 100) - ((120 - 100) * 100)
        self.assertEqual(option2.calculate_profit(120), expected_profit)

    def test_breakeven(self):
        option3 = Options(
            premium=10,
            strike_price=100,
            contract_size=100,
            option_type='long call',
            market_price=10
        )
        expected_breakeven = 100 + 10
        self.assertEqual(option3.calculate_breakeven(), expected_breakeven)
    
    def test_long_put_profit(self):
        option4 = Options(
            premium=5,
            strike_price=100,
            contract_size=100,
            option_type='long put',
            market_price=80
        )
        expected_profit = (100 - 80 - 5) * 100
        self.assertEqual(option4.calculate_profit(80),expected_profit)

    def test_short_put_profit(self):
        option5 = Options(
            premium=5,
            strike_price=80,
            contract_size=100,
            option_type='long call',
            market_price=100
        )



