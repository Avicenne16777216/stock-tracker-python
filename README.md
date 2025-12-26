📈 Real-Time Stock Market Tracker

A Python-based financial tool that interfaces with the Alpha Vantage API to retrieve, process, and visualize real-time equity data. This project focuses on asynchronous data fetching, JSON parsing, and dynamic plotting.

🚀 Features
- Real-time Data Retrieval: Fetches Intraday or Daily stock prices.
- Data Visualization: Generates time-series line charts using Matplotlib.
- Defensive Programming: Implements error handling for invalid ticker symbols or API limit reaches.
- Secure Configuration: Uses environment variables for API key management.

🏗️ System Workflow
The application follows a linear data pipeline:
1. User Input: Accepts a ticker symbol (e.g., TSLA, NVDA).
2. Request Layer: Constructs a REST API call with secure credentials.
3. Parsing Layer: Extracts time-series data from the nested JSON response.
4. Visualization: Maps timestamps to the X-axis and closing prices to the Y-axis.


⚙️ Setup
1. Install dependencies: `pip install requests matplotlib python-dotenv`
2. Add your API key to a `.env` file: `ALPHA_VANTAGE_KEY=your_key`
3. Run the script: `python stock_tracker.py`