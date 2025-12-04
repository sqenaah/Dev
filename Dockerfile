   FROM python:3.10-slim

   # Install ffmpeg, git and time synchronization tools
   RUN apt-get update && apt-get install -y ffmpeg git tzdata ntpsec-ntpdate

   # Copy requirements and install
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   # Copy app
   COPY . .

   # Set timezone and sync time
   ENV TZ=UTC
   RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

   # Create startup script
   RUN echo '#!/bin/bash\n\
echo "Starting YukkiMusicBot..."\n\
echo "Setting environment variables..."\n\
export PYROGRAM_SKIP_TIME_CHECK=1\n\
export PYROGRAM_NO_TIME_SYNC=1\n\
echo "Environment variables set"\n\
echo "Starting Python application..."\n\
exec python3 -m YukkiMusic' > /start.sh && chmod +x /start.sh

   # Run startup script
   CMD ["/start.sh"]
