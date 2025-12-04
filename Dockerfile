   FROM python:3.10-slim

   # Install ffmpeg, git and time synchronization tools
   RUN apt-get update && apt-get install -y ffmpeg git tzdata ntpdate

   # Copy requirements and install
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   # Copy app
   COPY . .

   # Set timezone and sync time
   ENV TZ=UTC
   RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

   # Run with time sync
   CMD ntpdate -u pool.ntp.org && python3 -m YukkiMusic
