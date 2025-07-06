from flask import Flask, request, jsonify
import pytube
import os

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        return jsonify({
            "title": yt.title,
            "video_url": stream.url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
