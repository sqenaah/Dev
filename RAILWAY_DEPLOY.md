# YukkiMusicBot Railway Deployment Guide

## Prerequisites
1. Railway account (https://railway.app)
2. Telegram API credentials
3. MongoDB database
4. GitHub repository connected

## Environment Variables Required

Set these environment variables in your Railway project:

### Bot Configuration
- `API_ID`: Your Telegram API ID (get from https://my.telegram.org)
- `API_HASH`: Your Telegram API Hash (get from https://my.telegram.org)
- `BOT_TOKEN`: Your bot token (get from @BotFather)

### Database
- `MONGO_DB_URI`: Your MongoDB connection string (get from MongoDB Atlas or similar)

### Logging
- `LOG_GROUP_ID`: Your log group chat ID (create a private group and add your bot)

### Bot Settings
- `MUSIC_BOT_NAME`: Name for your music bot (default: YukkiMusicBot)

### Session
- `STRING_SESSION`: Pyrogram string session (get from @yukkistringbot)

## Deployment Steps

1. Go to [Railway](https://railway.app) and create a new project
2. Connect your GitHub repository (https://github.com/sqenaah/Dev)
3. Railway will automatically detect the configuration and deploy
4. Set the environment variables in Railway dashboard
5. Deploy the project

## Additional Notes

- The bot requires ffmpeg for audio/video processing
- MongoDB is required for data persistence
- Make sure all environment variables are set correctly before deployment
