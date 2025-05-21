import logging
from src.tts import tts
from src.get_content import Firecrawler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("webpage2audio.log"),
        logging.StreamHandler()
    ]
)

def main():
    url_input = input("Enter the URL of the webpage you want to scrape: ")
    crawler = Firecrawler()
    webpage_content = crawler.scrape_webpage_content(url_input)
    if webpage_content:
        logging.info(f"Success: Webpage content fetched successfully ::: {webpage_content}")
    else:
        logging.error("Error: Failed to fetch webpage content.")
        return
    audio_output = tts(webpage_content)
    if audio_output:
        logging.info("Success: Audio generated successfully.")
        with open("output.mp3", "wb") as file:
            file.write(audio_output.read())
            audio_output.close()
    else:
        logging.error("Error: Failed to generate audio.")

if __name__ == "__main__":
    main()
