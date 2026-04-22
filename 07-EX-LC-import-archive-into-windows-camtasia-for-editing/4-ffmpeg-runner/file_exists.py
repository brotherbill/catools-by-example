import os
# C:/dev/catools-by-example/07-EX-LC-import-archive-into-windows-camtasia-for-editing/4-ffmpeg-runner/file_exists.py

def main():
    if len(sys.argv) != 2:
        print("ERROR: expected exactly one argument (path to file)")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isfile(path):
        print(f"EXISTS: {path}")
        sys.exit(0)
    else:
        print(f"NOT_FOUND: {path}")
        sys.exit(2)

if __name__ == "__main__":
    main()
