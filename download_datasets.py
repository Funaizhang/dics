import os
import argparse
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_files(files, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for key in files.keys():
        gdd.download_file_from_google_drive(file_id=files[key], dest_path=os.path.join(directory, key), unzip=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-output', help='output folder path')
    args = parser.parse_args()

    files = {
        'celebrA.zip': '0B7EVK8r0v71pZjFTYXZWM3FlRnM',
        'one-piece-faces-128.zip': '1NI4GSmKMo0LQB2hNwxkDumo1W58TIUsj',
    }
    download_files(files, args.output)
