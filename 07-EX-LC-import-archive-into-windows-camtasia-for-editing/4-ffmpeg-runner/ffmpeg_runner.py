#!/usr/bin/env python3
# C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/ffmpeg_runner.py
import sys
import os
import json
import subprocess
from datetime import datetime

def file_exists(path):
    return os.path.isfile(path)

def run_probe(input_file):
    """Call probe_video.py and return parsed JSON."""
    try:
        result = subprocess.run(
            [sys.executable, "probe_video.py", input_file],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        return json.loads(result.stdout)
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) != 2:
        print("Usage: ffmpeg_runner.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # 1. Check file existence
    if not file_exists(os.path.join("validation_source", input_file)):
        print(f"ERROR: File not found: {input_file}")
        sys.exit(1)

    # 2. Prepare output directory
    base = os.path.splitext(input_file)[0]
    out_dir = f"{base}_out"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 3. Run probe
    probe_data = run_probe(os.path.join("validation_source", input_file))

    # 4. Write metadata file
    metadata = {
        "input_file": input_file,
        "output_directory": out_dir,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "probe": probe_data
    }

    metadata_path = os.path.join(out_dir, "metadata.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Runner completed. Output directory: {out_dir}")
    sys.exit(0)

if __name__ == "__main__":
    main()
