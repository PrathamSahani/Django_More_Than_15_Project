from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def get_currency(request):
    # Replace 'demo' with your Alpha Vantage API key
    api_key = 'TBZAVDWESU00D872'

    # Make a request to Alpha Vantage API to get currency data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            # Check if the "Time Series (5min)" key exists in the data
            if 'Time Series (5min)' in data:
                time_series = data['Time Series (5min)']
                # Find the most recent timestamp
                latest_timestamp = max(time_series.keys())
                latest_data = time_series[latest_timestamp]
                usd = latest_data.get('1. open')
                er = latest_data.get('2. high')
                inr = latest_data.get('3. low')
            else:
                usd = er = inr = 'N/A'
        except Exception as e:
            # Handle JSON parsing error
            print(f"JSON parsing error: {e}")
            usd = er = inr = 'N/A'
    else:
        # Handle API request error
        print(f"API request error: {response.status_code}")
        usd = er = inr = 'N/A'

    context = {'usd': usd, 'er': er, 'inr': inr}
    
    # Add this line to print the Alpha Vantage API response
    print(data)
    
    return render(request, 'partial/show.html', context)
