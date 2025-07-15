import React, { useState } from 'react';
import axios from 'axios';
import ScraperForm from './components/ScraperForm';
import Results from './components/Results';
import Loader from './components/Loader';
import config from './config';
import './App.css';

function App() {
    const [scrapedData, setScrapedData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [sessionId, setSessionId] = useState(null);

    const handleScrape = async (url) => {
        setLoading(true);
        setError('');
        setScrapedData(null);

        try {
            const response = await axios.post(`${config.API_BASE_URL}/api/scrape`, { url });
            setScrapedData(response.data.data);
            setSessionId(response.data.sessionId);
        } catch (err) {
            console.error('Scraping error:', err);
            if (err.response) {
                setError(`Server error: ${err.response.status} - ${err.response.data?.error || 'Unknown error'}`);
            } else if (err.request) {
                setError('Network error: Unable to reach the server. Please check if the backend is running.');
            } else {
                setError('Failed to scrape the URL. Please check the URL and try again.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Web Scraper 🕸️</h1>
                <p>Enter a URL to scrape its content</p>
            </header>
            <main>
                <ScraperForm onScrape={handleScrape} />
                {loading && <Loader />}
                {error && <p className="error">{error}</p>}
                {scrapedData && <Results data={scrapedData} sessionId={sessionId} />}
            </main>
            <footer>
                <p>&copy; 2025 Web Scraper. All rights reserved.</p>
            </footer>
        </div>
    );
}

export default App;