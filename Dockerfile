   FROM python:3.10-slim

   # Install ffmpeg
   RUN apt-get update && apt-get install -y ffmpeg

   # Copy requirements and install
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   # Copy app
   COPY . .

   # Run
   CMD ["python3", "main.py"]
