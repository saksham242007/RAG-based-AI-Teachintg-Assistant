import os
import subprocess
from pathlib import Path

VIDEOS_DIR = "videos"
AUDIOS_DIR = "audios"

os.makedirs(AUDIOS_DIR, exist_ok=True)

video_extensions = (".mp4", ".mov", ".avi", ".mkv", ".webm")

for filename in os.listdir(VIDEOS_DIR):
    if filename.lower().endswith(video_extensions):
        input_path = os.path.join(VIDEOS_DIR, filename)
        output_name = Path(filename).stem + ".mp3"
        output_path = os.path.join(AUDIOS_DIR, output_name)

        print(f"Converting: {filename} -> {output_name}")

        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vn",
            "-ar", "16000",
            "-ac", "1",
            "-b:a", "192k",
            "-y",
            output_path
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"  ❌ Failed: {result.stderr[-300:]}")
        else:
            print(f"  ✅ Saved to {output_path}")

print("Done!")