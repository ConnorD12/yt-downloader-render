from flask import Flask, request, jsonify
import subprocess
import json
import os

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    try:
        # Use yt-dlp to fetch video info in JSON
        result = subprocess.run(
            ["yt-dlp", "-j", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            return jsonify({"error": result.stderr.strip()}), 500

        video_info = json.loads(result.stdout)
        return jsonify({
            "title": video_info.get("title"),
            "video_url": video_info.get("url"),
            "duration": video_info.get("duration"),
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
