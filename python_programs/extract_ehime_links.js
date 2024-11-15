// Assuming VIDEO_CONFIG is available in the global scope
if (typeof VIDEO_CONFIG !== 'undefined' && VIDEO_CONFIG.streams) {
    VIDEO_CONFIG.streams.forEach((stream, index) => {
        console.log(`play_url for format_id ${stream.format_id}: ${stream.play_url}`);
        // Open each play_url in a new tab (optional)
        // window.open(stream.play_url, '_blank');
    });
} else {
    console.log('VIDEO_CONFIG is not defined or streams are not available.');
}

