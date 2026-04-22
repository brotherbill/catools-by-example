#!/usr/bin/env python3
# C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/ffmpeg_runner.py

import json
import subprocess
import sys
import os
from datetime import datetime

def run_subprocess(cmd):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return {"success": True, "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        return {"success": False, "stdout": e.stdout, "stderr": e.stderr}

def probe_video(input_path):
    cmd = [
        os.path.join("bin", "ffprobe.exe"),
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        "-show_programs",
        "-show_stream_groups",
        input_path
    ]
    result = run_subprocess(cmd)
    if not result["success"]:
        return {"error": "ffprobe failed", "details": result}
    try:
        return json.loads(result["stdout"])
    except json.JSONDecodeError:
        return {"error": "Invalid JSON from ffprobe", "raw_output": result["stdout"]}

def run_ffmpeg_test_patterns(output_dir):
    ffmpeg = os.path.join("bin", "ffmpeg.exe")

    outputs = {
        "ffmpeg_test_black.mp4": "color=black",
        "ffmpeg_test_white.mp4": "color=white"
    }

    results = {}

    for filename, color in outputs.items():
        out_path = os.path.join(output_dir, filename)

        cmd = [
            ffmpeg,
            "-y",
            "-f", "lavfi",
            "-i", f"{color}:s=1920x1080:d=1:r=30",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            out_path
        ]

        result = run_subprocess(cmd)
        results[filename] = "success" if result["success"] else "failure"

    return results

def write_metadata(output_dir, metadata):
    metadata_path = os.path.join(output_dir, "metadata.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

def main():
    if len(sys.argv) < 2:
        print("Usage: python ffmpeg_runner.py <input_video>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = f"{base_name}_out"
    os.makedirs(output_dir, exist_ok=True)

    probe_data = probe_video(input_file)

    ffmpeg_results = run_ffmpeg_test_patterns(output_dir)

    metadata = {
        "input_file": input_file,
        "output_directory": output_dir,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "probe": probe_data,
        "ffmpeg_test_black": ffmpeg_results.get("ffmpeg_test_black.mp4"),
        "ffmpeg_test_white": ffmpeg_results.get("ffmpeg_test_white.mp4")
    }

    write_metadata(output_dir, metadata)

    print(f"Runner completed. Output directory: {output_dir}")

if __name__ == "__main__":
    main()
