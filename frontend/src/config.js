// API Configuration
const config = {
  // Use environment variable if available, otherwise default to production
  API_BASE_URL: process.env.REACT_APP_API_BASE_URL || 'https://scrapy-e4my.onrender.com',
  
  // For local development, you can set REACT_APP_API_BASE_URL=http://localhost:5001
  // in your .env file
};

export default config;
