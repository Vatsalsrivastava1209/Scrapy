# Web Scraper Website

This is a full-stack web application that allows users to scrape text, images, and videos from a given URL.

## ✨ Features

- **Simple UI**: Enter a URL and click a button to start scraping.
- **Scrape Multiple Content Types**: Extracts text, images, and video URLs.
- **Organized Display**: Scraped content is displayed in separate, easy-to-read sections.
- **Downloadable Content**: Download scraped text as a `.txt` file and images as a `.zip` archive.
- **Responsive Design**: Works on both desktop and mobile devices.
- **Error Handling**: Provides feedback for invalid URLs or scraping failures.
- **Loading Indicator**: Shows a spinner while scraping is in progress.

## 🛠️ Tech Stack

### Backend

- **Python**: A versatile programming language.
- **Flask**: A lightweight web framework for Python.
- **BeautifulSoup**: A Python library for pulling data out of HTML and XML files.
- **Requests**: A simple, yet elegant, HTTP library for Python.
- **Flask-CORS**: A Flask extension for handling Cross-Origin Resource Sharing (CORS).

### Frontend

- **React**: A JavaScript library for building user interfaces.
- **Axios**: A promise-based HTTP client for the browser and Node.js.
- **HTML5 & CSS3**: For structuring and styling the application.

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/en/download/) (or [Yarn](https://yarnpkg.com/))

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/web-scraper.git](https://github.com/your-username/web-scraper.git)
    cd web-scraper
    ```

2.  **Setup the Backend:**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Setup the Frontend:**
    ```bash
    cd ../frontend
    npm install  # or `yarn install`
    ```

### Running the Application

1.  **Start the Backend Server:**
    -   Make sure you are in the `backend` directory and your virtual environment is activated.
    ```bash
    flask run --port=5001
    ```
    The backend will be running at `http://localhost:5001`.

2.  **Start the Frontend Development Server:**
    -   Open a new terminal, navigate to the `frontend` directory.
    ```bash
    npm start  # or `yarn start`
    ```
    The frontend will be running at `http://localhost:3000` and will open automatically in your browser.

## 🤖 API Endpoints

-   `POST /api/scrape`
    -   **Description**: Scrapes a website for content.
    -   **Request Body**: `{ "url": "https://example.com" }`
    -   **Response**:
        ```json
        {
          "sessionId": "some-unique-id",
          "data": {
            "text": "Scraped text content...",
            "images": ["url1.jpg", "url2.png"],
            "videos": ["url1.mp4"]
          }
        }
        ```

-   `GET /api/download/text/<session_id>`
    -   **Description**: Downloads the scraped text as a `.txt` file.

-   `GET /api/download/images/<session_id>`
    -   **Description**: Downloads all scraped images as a `.zip` file.

## 📜 Ethical Scraping

This tool is for educational purposes. Please be responsible and respect the terms of service of the websites you scrape. Avoid sending too many requests in a short period. This scraper includes a `User-Agent` header to identify its requests but does not handle `robots.txt` or advanced anti-scraping measures.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📄 License

This project is licensed under the MIT License.
