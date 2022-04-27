"""
Example usage of the Free News API Python SDK.
"""

import datetime
from freenewsapi import NewsAPI, NewsAPIError

def main():
    # Replace with your actual API key
    api_key = "your-api-key"
    
    # Initialize the SDK
    api = NewsAPI(api_key)
    
    # Example 1: Simple search
    try:
        print("EXAMPLE 1: Simple search for 'bitcoin'")
        results = api.search(q="bitcoin", max=3)
        print(f"Found {results['totalArticles']} articles")
        
        # Display articles
        for article in results["articles"]:
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}")
            print("---")
        print()
    except NewsAPIError as e:
        print(f"Error: {e}")
     

if __name__ == "__main__":
    main()