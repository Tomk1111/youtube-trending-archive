# YouTube Trending Archive

A Python script to fetch and archive trending videos from private YouTube trending API.

## Video Object Properties

The script retrieves the following properties for each trending video:

- `title`: The title of the video.
- `description`: The video's description.
- `publishedDate`: The date and time when the video was published (in a machine-readable format).
- `publishedText`: The date and time when the video was published (in a human-readable format).
- `videoId`: The unique identifier for the video.
- `videoUrl`: The URL of the video.
- `channelName`: The name of the channel that published the video.
- `channelId`: The unique identifier for the channel.
- `channelUrl`: The URL of the channel.
- `thumbnails`: URLs for the video's thumbnail images in different resolutions.
- `views`: The number of views the video has received.
- `viewsText`: The number of views in a human-readable format (e.g., "1.2M views").
- `duration`: The duration of the video (in a machine-readable format).
- `durationText`: The duration of the video in a human-readable format (e.g., "3:24").
- `verified`: A boolean indicating whether the channel is verified or not.
- `creatorOnRise`: A boolean indicating whether the channel is marked as a "Creator on the Rise" by YouTube.
- `isShort`: A boolean indicating whether the video is a YouTube Shorts video or not.

# Data Collection

The script collects trending video data from various categories on YouTube:

- **Default**: The main YouTube trending page, featuring videos across all categories.
- **Music**: The trending page specifically for music videos and music-related content.
- **Gaming**: The trending page for gaming videos, live streams, and gaming-related content.
- **Movies**: The trending page for movie trailers, clips, and other movie-related videos.

## Data Storage

The collected data is saved in compressed CSV (Comma-Separated Values) files, with one file per category. The file naming convention follows the format: **category**_**timestamp**.csv.gz


Where:

- `category` is the name of the category (e.g., `default`, `music`, `gaming`, `movies`).
- `timestamp` is the current date and time in the format `YYYYMMDD` (e.g., `20230501` for May 1, 2023).

All data files are stored in the `data` directory within the project.

## Automation

To ensure regular data collection, the script is scheduled to run automatically using GitHub Actions. It is executed daily at 20:00 UTC (8:00 PM UTC), fetching the latest trending videos from each category and writing the data to the corresponding CSV file.

## Kaggle Upload

GitHub Actions has been setup to automatically upload latest YouTube trending data to a kaggle dataset. This is executed daily at 20:00 UTC (8:00 PM UTC). https://www.kaggle.com/datasets/pyuser11/youtube-trending-videos-updated-daily

