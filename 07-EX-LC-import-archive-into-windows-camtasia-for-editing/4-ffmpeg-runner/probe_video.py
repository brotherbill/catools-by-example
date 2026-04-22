#!/usr/bin/env python3

import json
import subprocess
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("ERROR: expected exactly one argument (path to video file)")
        sys.exit(1)

    video_path = sys.argv[1]

    # Resolve ffprobe relative to this script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ffprobe_path = os.path.join(script_dir, "bin", "ffprobe.exe")

    cmd = [
        ffprobe_path,
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,duration,codec_name",
        "-of", "json",
        video_path
    ]

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"ERROR: ffprobe failed: {e.stderr.strip()}")
        sys.exit(1)
    except FileNotFoundError:
        print("ERROR: ffprobe executable not found (expected in PATH or ./bin)")
        sys.exit(1)

    try:
        metadata = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("ERROR: failed to parse ffprobe output as JSON")
        sys.exit(1)

    print(json.dumps(metadata, indent=4))

if __name__ == "__main__":
    main()
