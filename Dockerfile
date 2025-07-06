FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    pip install flask yt-dlp

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
