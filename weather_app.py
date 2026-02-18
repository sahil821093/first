import requests
import datetime

def get_weather(city_name, lat, lon):
    print(f"\n🌍 Connecting to Weather Satellite for {city_name}...")
    
    # Ye ASLI API Link hai (Open-Meteo)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['current_weather']['temperature']
            wind = data['current_weather']['windspeed']
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            print("✅ Connection Successful!")
            print(f"--------------------------")
            print(f"📍 Location: {city_name}")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"💨 Wind Speed: {wind} km/h")
            print(f"🕒 Time: {time}")
            print(f"--------------------------")
        else:
            print("❌ Error: Satellite data nahi de raha.")
            
    except Exception as e:
        print(f"⚠️ Network Error: {e}")
        print("   (Check your internet connection)")

# Main Program
if __name__ == "__main__":
    print("--- 🌤️ Sahil's Real-Time Weather App ---")
    # Patna Location Coordinates
    get_weather("Patna, Bihar", 25.60, 85.10)
