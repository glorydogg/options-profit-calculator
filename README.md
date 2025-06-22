# 📈 Options Profit Calculator (CLI)

A command-line Python application that calculates **profit**, **breakeven**, **maximum profit**, and **maximum loss** for four types of options:

- Long Call
- Short Call
- Long Put
- Short Put

---

## Features

- Clean CLI interface
- Input validation (rejects bad or missing values)
- Support for custom contract sizes
- Automatic calculation of:
  - Profit/Loss
  - Breakeven Point
  - Max Profit
  - Max Loss
- Unit tested using Python’s `unittest` module

---

## Example Usage
Welcome to the Options Profit Calculator

Enter option type (long call, short call, long put, short put): long call
Enter strike price: 100
Enter premium: 5
Enter market price: 120
Enter contract size (press Enter to use 100):

--- Option Summary ---
Option Type: long call
Strike Price: 100.0
Premium: 5.0
Market Price: 120.0
Contract Size: 100
Profit: $1,500.00
Breakeven: $105.00
Max Profit: inf
Max Loss: $500.00

