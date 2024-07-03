import requests
import json
import datetime
import gzip
import os
import csv
import sys

def save_csv_gz(data, data_type):
    if not data:
        print("No data to save")
        return

    data_dir = "data"
    type_dir = os.path.join(data_dir, data_type)
    os.makedirs(type_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime('%Y%m%d')
    filename = f"{data_type}_{timestamp}.csv.gz"
    file_path = os.path.join(type_dir, filename)
    print(file_path)

    fieldnames = data[0].keys()
    print(",".join(fieldnames))
    print()
    with gzip.open(file_path, "wt", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {file_path}")
    return file_path


def fetch_data(api_url, data_type):
    params = {'type': data_type} if data_type else None
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        csvFile = save_csv_gz(data, data_type) if data_type else save_csv_gz(data, 'default')
        return csvFile
    else:
        print(f'Error: {response.status_code}')
        return None

def fetch_default(api_url):
    return fetch_data(api_url, None)

def fetch_music(api_url):
    return fetch_data(api_url, 'music')

def fetch_gaming(api_url):
    return fetch_data(api_url, 'gaming')

def fetch_movies(api_url):
    return fetch_data(api_url, 'movies')


def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <api_url>")
        return

    api_url = sys.argv[1]
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    default_file = fetch_default(api_url)
    if default_file:
        print(f'Default data saved to {default_file}')

    music_file = fetch_music(api_url)
    if music_file:
        print(f'Music data saved to {music_file}')

    gaming_file = fetch_gaming(api_url)
    if gaming_file:
        print(f'Gaming data saved to {gaming_file}')

    movies_file = fetch_movies(api_url)
    if movies_file:
        print(f'Movies data saved to {movies_file}')

if __name__ == "__main__":
    main()