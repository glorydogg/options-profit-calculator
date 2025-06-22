from options_calc_main import Options

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to the Options Profit Calculator\n")
    valid_types = ['long call', 'short call', 'long put', 'short put']
    while True:
        option_type = input("Enter option type (long call, short call, long put, short put): ").lower().strip()
        if option_type in valid_types:
            break
        else:
            print("Invalid option type please try")

    
    strike_price = get_positive_float("Enter strike price: ")
    premium = get_positive_float("Enter premium: ")
    market_price = get_positive_float("Enter market price: ")

    contract_size_input = input("Enter contract size (press Enter to use 100): ").strip()
    contract_size = int(contract_size_input) if contract_size_input else 100
    option = Options(premium, strike_price, contract_size, option_type, market_price)
    print("\n--- Option Summary ---")
    print(f"Option Type: {option.option_type}")
    print(f"Strike Price: {option.strike_price}")
    print(f"Premium: {option.premium}")
    print(f"Market Price: {option.market_price}")
    print(f"Contract Size: {option.contract_size}")
    print(f"Profit: ${option.calculate_profit(market_price):.2f}")
    print(f"Breakeven: ${option.calculate_breakeven(market_price):.2f}")
    print(f"Max Profit: {option.max_profit()}")
    print(f"Max Loss: {option.max_loss()}")
    
    
    
if __name__ == "__main__":
    main()




