import os
import json
import asyncio
from firecrawl import FirecrawlApp, ScrapeOptions

class Firecrawler:
    """A class to handle webpage content scraping and crawling using Firecrawl."""
    
    def __init__(self, api_key=os.getenv("FIRECRAWL_API_KEY")):
        """
        Initialize the WebpageScraper with Firecrawl API key.

        Args:
            api_key (str): Firecrawl API key.
        """
        self.api_key = api_key or "fc-af020ac0f46c43c4adc71c39f094ad66"
        self.app = FirecrawlApp(api_key=self.api_key)

    def scrape_webpage_content(self, url):
        """
        Fetches the content of a webpage given its URL.

        Args:
            url (str): The URL of the webpage to fetch.

        Returns:
            str: The content of the webpage.
        """
        webpage_scrape_result = self.app.scrape_url(
            url,
            formats=['markdown'],
            onlyMainContent=True
        )
        
        return webpage_scrape_result

    def crawl_website(self, url):
        """
        Crawls a website and fetches content from multiple pages.

        Args:
            url (str): The URL of the website to crawl.
            max_pages (int): Maximum number of pages to crawl.

        Returns:
            list: List of scraped content from the crawled pages.
        """
        scrape_options = ScrapeOptions(
            onlyMainContent=True,
            formats=['markdown'],
            waitFor=3, 
            blockAds=True, 
            removeBase64Images=True, 
                                                limit=100, 
                                    ignoreQueryParameters=False,
                                    allowBackwardLinks=True,
                                    allowExternalLinks=False, 
                                    maxDepth=3,
                                    maxDiscoveryDepth=2,
                                    ignoreSitemap=False,
        )
        
        crawl_result = self.app.crawl_url(
                                    url,
                                    scrape_options=scrape_options)
                                
        return crawl_result