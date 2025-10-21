import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
import requests
import json 

stock_symbol = input("Please enter a stock symbol (e.g., AAPL): ").upper()

api_key = "65BQCHHQEG6OLYHX"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"

response = requests.get(url)
response.raise_for_status()
data = response.json()

# Initialized outside the loop, as before.
price_history = [] 
date_history = []

# Check if the API returned an error message
if "Error Message" in data:
    print("Sorry, that stock symbol was not found.")
else:
    # 1. Access the daily time series data
    time_series = data.get("Time Series (Daily)", {})
    
    # --- IMPORTANT PART START HERE ---
    
    # Get the list of dates ONCE for efficiency and safety
    all_dates = list(time_series.keys()) 
    
    # We will only loop up to 30 days OR the number of days available
    num_days_to_display = min(30, len(all_dates)) 
    
    print("\n--- Latest Stock History ---")
    
    for i in range(num_days_to_display):
        # We use the pre-calculated list of dates and the index 'i'
        current_date = all_dates[i]
        
        # Access the data for the current date
        current_data = time_series[current_date]
        
        # Get the closing price
        closing_price = round(float(current_data["4. close"]), 2)
        
        # To add the price and the date to lists
        price_history.append(closing_price)
        date_history.append(current_date)
        
        # Print the result in a clean, user-friendly format
        print(f"[{i:02d}] {current_date}: ${closing_price}")
        

    # Reversing the list for plotting
    price_history.reverse()
    date_history.reverse()
    
    # --- START OF MATPLOTLIB SECTION (Safely inside the 'else' block) ---
    
    # I love these parameters
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.set_facecolor("#2C363F")
    ax.set_title(f"Price History for {stock_symbol} ({num_days_to_display} days)", color="white", fontsize=16) 
    ax.set_facecolor("#35393C")
    
    # Axis Labels for clarity
    ax.set_xlabel("Date", color="white", fontsize=12)
    ax.set_ylabel("Closing Price ($)", color="white", fontsize=12)
    
    # Set x and y values
    x = date_history
    y = price_history
    
    # Showtime
    ax.plot(x, y, color="#42858C", linewidth=2)
    
    # Final Touches
    ax.tick_params(axis='x', rotation=45, colors="white") # Added color for ticks
    ax.tick_params(axis='y', colors="white")
    
    plt.grid(True, alpha=0.2)
    plt.tight_layout() # Ensures labels don't get cut off
    plt.show()
    
# --- END OF MATPLOTLIB SECTION (Only runs if data is valid) ---




