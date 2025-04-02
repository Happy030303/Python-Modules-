import requests


def wheather_api(api_key, city):
    url = "http://api.openweathermap.org/data/2.5/weather"

    param = {                      #the data that i want to retrieve from wheather api
                "q": city,         # Which city you want weather for
                "appid": api_key,  # Your unique API key (like a password)
                "units": "metric"  # Measurement system you prefer
            }
    
    try:
        response = requests.get(url, params = param)
        wheather_data = response.json() # converting json data got from wheather api into dictionary 
        print("status : ",response.status_code)
        print("url made : ", response.url)

        if wheather_data["cod"] == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {wheather_data['main']['temp']}°C")
            print(f"Feels like: {wheather_data['main']['feels_like']}°C")
            print(f"Humidity: {wheather_data['main']['humidity']}%")
            print(f"Weather conditions: {wheather_data['weather'][0]['description']}")
        else : 
            return
    except Exception as e:
        print(f"Exception is : {e}")


api_key = "fea2b4de20cec977175642536a59900d" # another api key : "0979bf5b63b322bec555887b18ada3c3"
city = input("enter city name : ")
wheather_api(api_key, city)
