import React from 'react';
import config from '../config';

const Results = ({ data, sessionId }) => {
    const handleDownload = (type) => {
        window.open(`${config.API_BASE_URL}/api/download/${type}/${sessionId}`);
    };

    return (
        <div className="results">
            {data.text && (
                <section>
                    <h2>
                        Scraped Text
                        <button onClick={() => handleDownload('text')} className="download-btn">
                            Download .txt
                        </button>
                    </h2>
                    <pre>{data.text}</pre>
                </section>
            )}

            {data.images && data.images.length > 0 && (
                <section>
                    <h2>
                        Scraped Images
                        <button onClick={() => handleDownload('images')} className="download-btn">
                            Download .zip
                        </button>
                    </h2>
                    <div className="image-gallery">
                        {data.images.map((src, index) => (
                            <img key={index} src={src} alt={`Scraped content ${index + 1}`} />
                        ))}
                    </div>
                </section>
            )}

            {data.videos && data.videos.length > 0 && (
                <section>
                    <h2>Scraped Videos</h2>
                    <div className="video-gallery">
                        {data.videos.map((src, index) => {
                            if (src.includes('youtube.com/embed') || src.includes('player.vimeo.com/video')) {
                                return (
                                    <iframe
                                        key={index}
                                        src={src}
                                        title={`Scraped video ${index + 1}`}
                                        frameBorder="0"
                                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                        allowFullScreen
                                    ></iframe>
                                );
                            }
                            return (
                                <video key={index} controls>
                                    <source src={src} type="video/mp4" />
                                    Your browser does not support the video tag.
                                </video>
                            );
                        })}
                    </div>
                </section>
            )}
        </div>
    );
};

export default Results;
