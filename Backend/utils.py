import os
import zipfile
import requests

def download_images_as_zip(image_urls, output_path):
    """
    Downloads images from a list of URLs and saves them to a zip file.

    Args:
        image_urls (list): A list of image URLs.
        output_path (str): The path to save the zip file.
    """
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for i, url in enumerate(image_urls):
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                filename = f"image_{i+1}.{url.split('.')[-1]}"
                zipf.writestr(filename, response.content)
            except requests.exceptions.RequestException as e:
                print(f"Could not download {url}: {e}")