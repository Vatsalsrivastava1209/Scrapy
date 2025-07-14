import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    """
    Scrapes a website for text, images, and videos.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing the scraped text, image URLs, and video URLs.
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape text
    texts = [p.get_text() for p in soup.find_all('p')]
    headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    scraped_text = "\n".join(headings + texts)

    # Scrape images
    image_urls = [urljoin(url, img['src']) for img in soup.find_all('img') if img.get('src')]

    # Scrape videos
    video_urls = []
    for video in soup.find_all('video'):
        if video.get('src'):
            video_urls.append(urljoin(url, video.get('src')))
        else:
            for source in video.find_all('source'):
                if source.get('src'):
                    video_urls.append(urljoin(url, source.get('src')))

    # Look for YouTube and Vimeo embeds
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src')
        if src:
            if 'youtube.com/embed' in src:
                video_urls.append(src)
            elif 'player.vimeo.com/video' in src:
                video_urls.append(src)


    return {
        'text': scraped_text,
        'images': list(set(image_urls)),
        'videos': list(set(video_urls))
    }