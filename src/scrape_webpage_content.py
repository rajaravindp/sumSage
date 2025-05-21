import os
import json
import asyncio
from firecrawl import FirecrawlApp, ScrapeOptions

def get_webpage_content(url):
    """
    Fetches the content of a webpage given its URL.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The content of the webpage.
    """
    # Initialize the Firecrawl app with your API key
    FIRECRAWL_API_KEY = "fc-af020ac0f46c43c4adc71c39f094ad66"
    app = FirecrawlApp(api_key = FIRECRAWL_API_KEY)
    webpage_scrape_result = app.scrape_url(
        url,
        formats=['markdown'], 
        onlyMainContent=True
    )
    
    return webpage_scrape_result