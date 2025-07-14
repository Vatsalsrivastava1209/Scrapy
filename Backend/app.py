from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import uuid

from scraper import scrape_website
from utils import download_images_as_zip

app = Flask(__name__)
CORS(app)

# In-memory storage for scraped data
scraped_data_storage = {}

@app.route('/api/scrape', methods=['POST'])
def scrape():
    """
    API endpoint to scrape a website.
    Accepts a JSON payload with a 'url' key.
    """
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        data = scrape_website(url)
        if data is None:
            return jsonify({'error': 'Failed to scrape the website.'}), 500

        session_id = str(uuid.uuid4())
        scraped_data_storage[session_id] = data

        return jsonify({'sessionId': session_id, 'data': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/text/<session_id>', methods=['GET'])
def download_text(session_id):
    """
    API endpoint to download scraped text as a .txt file.
    """
    data = scraped_data_storage.get(session_id)
    if not data:
        return jsonify({'error': 'Session not found'}), 404

    temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, f"{session_id}.txt")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data['text'])

    return send_file(file_path, as_attachment=True, download_name='scraped_text.txt')

@app.route('/api/download/images/<session_id>', methods=['GET'])
def download_images(session_id):
    """
    API endpoint to download scraped images as a .zip file.
    """
    data = scraped_data_storage.get(session_id)
    if not data:
        return jsonify({'error': 'Session not found'}), 404

    temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    zip_path = os.path.join(temp_dir, f"{session_id}_images.zip")

    download_images_as_zip(data['images'], zip_path)

    return send_file(zip_path, as_attachment=True, download_name='scraped_images.zip')

if __name__ == '__main__':
    app.run(debug=True, port=5001)