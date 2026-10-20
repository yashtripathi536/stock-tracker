# Stock Portfolio Tracker - CodeAlpha Task 2

# Hardcoded stock prices (per share)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

portfolio = {}      # stores stock name -> quantity
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you finish adding stocks.\n")

while True:
    stock = input("Enter stock name: ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available list.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Add to portfolio (if the stock is already added, increase the quantity)
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"Added {quantity} share(s) of {stock}.\n")

# Calculate and display results
print("\n===== Portfolio Summary =====")
lines = []
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    line = f"{stock}: {qty} x ${stock_prices[stock]} = ${value}"
    print(line)
    lines.append(line)

print("-----------------------------")
print(f"Total Investment: ${total_investment}")

# Optional: save to a file
if portfolio:
    save = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=======================\n")
            for line in lines:
                file.write(line + "\n")
            file.write(f"\nTotal Investment: ${total_investment}\n")
        print("Saved to portfolio.txt")
else:
    print("No stocks were added.")