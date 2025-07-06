from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return "YouTube Downloader API is running!"

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        return jsonify({
            "title": yt.title,
            "video_url": stream.url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
