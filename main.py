from yahoo_fin import stock_info as si

# Start the loop
while True:
    # Get the ticker
    ticker = input("Which stock (ticker symbol) do you want?\n").upper()
    # Check if input is "done" to exit the loop
    if ticker == "done":
        break
    else:
        # Get the stock price from Yahoo
        price = round(si.get_live_price(ticker), 3)
        print(f'The stock price for {ticker} is {price}')
