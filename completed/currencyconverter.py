import requests

def get_exchange_rate(base_currency, target_currency):
    """Fetch the exchange rate from an API."""
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    # When you use the /latest endpoint and provide a base currency, the API calculates the exchange rates 
    # for that currency against multiple other currencies
    
    try:
        response = requests.get(url)
        data = response.json()
        if target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            print("Invalid target currency!")
            return None
    except Exception as e:
        print("Error fetching exchange rates:", e)
        return None

def convert_currency(amount, base_currency, target_currency):
    """Convert currency based on exchange rate."""
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed!")

# Example Usage
base_currency = input("Enter base currency (e.g., USD): ").upper() #Base currency
target_currency = input("Enter target currency (e.g., INR): ").upper() #target currency
amount = float(input("Enter amount to convert: "))  #amount to convert

convert_currency(amount, base_currency, target_currency)
