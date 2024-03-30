import requests
from datetime import datetime

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.stocks = {}

    def add_stock(self, symbol):
        if symbol not in self.stocks:
            self.stocks[symbol] = {'name': None, 'price': None}
            self.update_stock_price(symbol)
        else:
            print(f"{symbol} is already in your portfolio.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} removed from your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def update_stock_price(self, symbol):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}'

        try:
            response = requests.get(url)
            data = response.json()
            if 'Global Quote' in data:
                self.stocks[symbol]['price'] = float(data['Global Quote']['05. price'])
                self.stocks[symbol]['name'] = data['Global Quote']['01. symbol']
            else:
                print(f"Failed to retrieve data for {symbol}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def display_portfolio(self):
        print("Your Portfolio:")
        print("Symbol\t\tName\t\tPrice")
        total_value = 0
        for symbol, data in self.stocks.items():
            print(f"{symbol}\t\t{data['name']}\t\t{data['price']}")
            if data['price'] is not None:
                total_value += data['price']
        print("Total Portfolio Value:", round(total_value, 2))

    def get_portfolio_performance(self, start_date=None, end_date=None):
        if not all([start_date, end_date]):
            start_date = datetime.now().strftime('%Y-%m-%d')
            end_date = start_date
        else:
            try:
                datetime.strptime(start_date, '%Y-%m-%d')
                datetime.strptime(end_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

        total_investment = len(self.stocks) * 1000  # Assuming initial investment of $1000 per stock
        total_current_value = sum(data['price'] for data in self.stocks.values() if data['price'] is not None)

        print("Portfolio Performance Analysis:")
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Total Investment:", total_investment)
        print("Total Current Value:", round(total_current_value, 2))
        print("Total Gain/Loss:", round(total_current_value - total_investment, 2))

    def visualize_portfolio_performance(self):
        # Placeholder for visualization code
        print("Visualization of portfolio performance")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key
    portfolio = StockPortfolio(api_key)
    portfolio.add_stock('AAPL')
    portfolio.add_stock('MSFT')
    portfolio.add_stock('GOOGL')
    portfolio.display_portfolio()
    portfolio.remove_stock('GOOGL')
    portfolio.display_portfolio()
    portfolio.get_portfolio_performance()
