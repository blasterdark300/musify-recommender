import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import re
import csv

# Load .env
load_dotenv()

# Ambil Client ID dan Secret dari environment
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

if not client_id or not client_secret:
    raise Exception("Client ID atau Client Secret tidak ditemukan. Cek file .env Anda.")

# Inisialisasi Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Path ke file yang berisi link Spotify
file_path = r"C:\Users\crism\Downloads\Musify\album0.txt"  

#r"C:\Users\crism\Downloads\Musify\album0.txt"  bisa diganti dengan file txt lainnya

# Baca file dan ambil album ID
album_ids = []
with open(file_path, 'r', encoding='utf-8-sig') as file:
    for line in file:
        line = line.strip()
        match = re.search(r"album/([a-zA-Z0-9]+)", line)
        if match:
            album_ids.append(match.group(1))

print(f"Total album IDs ditemukan: {len(album_ids)}")

# Ambil data lagu dari setiap album
track_data = []
for album_id in album_ids:
    try:
        album = sp.album(album_id)
        tracks = sp.album_tracks(album_id)
        for track in tracks['items']:
            track_info = sp.track(track['id'])
            track_data.append({
                'name': track_info['name'],
                'artist': ', '.join([artist['name'] for artist in track_info['artists']]),
                'album': album['name'],
                'popularity': track_info['popularity'],
                'explicit': track_info['explicit'],
                'release_date': album['release_date'],
                'duration_ms': track_info['duration_ms'],
                'preview_url': track_info['preview_url']
            })
    except Exception as e:
        print(f"Gagal mengambil data album {album_id}: {e}")

# Simpan ke CSV
output_csv = r"C:\Users\crism\Downloads\Musify\spotify_cris_music.csv"
with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'artist', 'album', 'popularity', 'explicit', 'release_date', 'duration_ms', 'preview_url'])
    writer.writeheader()
    writer.writerows(track_data)

print(f"Data lagu berhasil disimpan ke {output_csv}")
