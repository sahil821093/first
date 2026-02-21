import requests

def get_tech_news():
    print("--- 📰 Sahil's Tech News Aggregator ---")
    print("Fetching the latest Technology News from the server... Please wait.\n")
    
    # Using a free public API endpoint (No API key required)
    url = "https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json"
    
    try:
        # Requesting data from the API
        response = requests.get(url)
        data = response.json() # Parsing the JSON response
        
        # Slicing the list to extract only the top 5 news articles
        articles = data["articles"][:5]
        
        # Iterating through the articles and displaying them
        for i, article in enumerate(articles, 1):
            print(f"[{i}] {article['title']}")
            print(f"🔗 Read full story here: {article['url']}")
            print("-" * 60) # UI separator line
            
    except Exception as e:
        print("❌ Error: Unable to fetch data. Please check your internet connection or try again later.")

# Execute the main function
if __name__ == "__main__":
    get_tech_news()
  
