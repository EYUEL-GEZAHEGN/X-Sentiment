import yfinance as yf
import pandas as pd

# List of stock tickers and their corresponding names
stocks = {
    'BSX': 'Boston Scientific Corp',
    'CI': 'The Cigna Group',
    'TMO': 'Thermo Fisher Scientific Inc',
    'UNH': 'UnitedHealth Group Inc',
    'VRTX': 'Vertex Pharmaceuticals Inc'
}

# Define the start and end dates
start_date = '2025-03-14'
end_date = '2025-03-21'

# Download historical data for the specified tickers and date range
data = yf.download(list(stocks.keys()), start=start_date, end=end_date)['Close']

# Calculate the percentage return for each stock
returns = data.pct_change().iloc[-1] * 100

# Prepare the data for export
export_data = pd.DataFrame({
    'Ticker': list(stocks.keys()),
    'Name': list(stocks.values()),
    'Daily Closing Price 2025-03-14': data.iloc[0].values,
    'Daily Closing Price 2025-03-21': data.iloc[-1].values,
    'Return (%)': returns.values
})

# Export the data to an Excel file
export_data.to_excel('stock_data.xlsx', index=False)
