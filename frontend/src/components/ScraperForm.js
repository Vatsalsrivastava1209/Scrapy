import React, { useState } from 'react';

const ScraperForm = ({ onScrape }) => {
    const [url, setUrl] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (url) {
            onScrape(url);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="scraper-form">
            <input
                type="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://example.com"
                required
            />
            <button type="submit">Scrape</button>
        </form>
    );
};

export default ScraperForm;
