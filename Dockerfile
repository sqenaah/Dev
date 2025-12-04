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
echo "Attempting time synchronization..."\n\
# Try multiple time sync methods\n\
(ntpsec-ntpdate -u pool.ntp.org 2>/dev/null || date -s "$(curl -s --max-time 10 http://worldtimeapi.org/api/timezone/Etc/UTC.txt | grep "datetime:" | cut -d" " -f2)" 2>/dev/null || true)\n\
echo "Time sync completed (or skipped)"\n\
echo "Starting Python application..."\n\
exec python3 -m YukkiMusic' > /start.sh && chmod +x /start.sh

   # Run startup script
   CMD ["/start.sh"]
