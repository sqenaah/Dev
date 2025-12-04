# YukkiMusicBot Railway Deployment Guide

## Prerequisites
1. Railway account (https://railway.app)
2. Telegram API credentials
3. MongoDB database
4. GitHub repository connected

## Environment Variables Required

Set these environment variables in your Railway project:

### Bot Configuration
- `API_ID`: `27638882`
- `API_HASH`: `f745cdd5ddb46cf841d6990048f52935`
- `BOT_TOKEN`: `8471862186:AAEmBU46Ms8zk5p7RENe6pLEeNsrGC1Uisc`

### Database
- `MONGO_DB_URI`: `mongodb+srv://ergibot:alobloglodlo@cluster0.c4oc3s5.mongodb.net/aria_db?retryWrites=true&w=majority`

### Logging
- `LOG_GROUP_ID`: `-1003142281080`

### Bot Settings
- `MUSIC_BOT_NAME`: `ArmedMusicBot`

### Session
- `STRING_SESSION`: `AgGlvGIAfoRpPE35J988vdTdciWrh4IFBvI5usTAnGE82ukbJoVgqdOWBmNWTKW98__OL4LSBL_O0Cc87A3TKKGn7R1jvz3ywyFhV1KzWUaSHSQkYyWWrVHlzYPrva08gd-NrcmEaRagbJQuGPhjy6m4b6sinJz8xFmrjg807wgl6k3aa9vTIPJVt4O_LqB_D4gtIJBuKyz50qoHQUD48rJbGybpFTQ33LSV2RL5zle8V3bs_0myWIzGzIeJlN9N39WJSWCyJ6G4PIg8yQdHTngPChg5wfU4A_kE5pJzLODXUalo0qaexQh7QYEaHNfMQRX5EI4jRhJd9LG_QagwxYr4p98CVAAAAAHya_vDAA`

## Deployment Steps

1. Go to [Railway](https://railway.app) and create a new project
2. Connect your GitHub repository (https://github.com/sqenaah/Dev)
3. Railway will automatically detect the configuration and deploy
4. Set the environment variables in Railway dashboard (copy the values above)
5. Deploy the project

## Additional Notes

- The bot requires ffmpeg for audio/video processing
- MongoDB is required for data persistence
- All environment variables are already configured with your values
- Just copy and paste them into Railway dashboard
