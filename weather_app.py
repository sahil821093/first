import requests

def get_weather(city_name, lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['current_weather']['temperature']
            print(f"\n✅ Success! {city_name} ka temperature {temp}°C hai.")
        else:
            print("❌ Satellite se data nahi mil raha.")
    except:
        print("⚠️ Internet check karein!")

# 1. Shehron ki list (Coordinates)
cities = {
    "patna": (25.60, 85.10),
    "delhi": (28.61, 77.20),
    "mumbai": (19.07, 72.87),
    "bangalore": (12.97, 77.59)
}

print("--- 🌤️ Sahil's Interactive Weather App ---")
print("Sheher ke naam: Patna, Delhi, Mumbai, Bangalore")

# 2. User se input lena
user_choice = input("\nKis sheher ka mausam dekhna hai? ").lower()

# 3. Check karna ki sheher list mein hai ya nahi
if user_choice in cities:
    lat, lon = cities[user_choice]
    get_weather(user_choice.title(), lat, lon)
else:
    print(f"❌ Sorry! '{user_choice}' abhi hamari list mein nahi hai.")
    
