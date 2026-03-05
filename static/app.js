if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/sw.js').catch(function (err) {
        console.error('Service worker registration failed:', err);
    });
}
