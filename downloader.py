import os
import subprocess
from yt_dlp import YoutubeDL
from colorama import Fore, Style, init

# Inisialisasi colorama (untuk Windows & Linux)
init(autoreset=True)

# Membuat direktori konfigurasi yt-dlp jika belum ada
config_directory = os.path.expanduser("~/.config/yt-dlp")
os.makedirs(config_directory, exist_ok=True)

# Folder untuk menyimpan file
output_directory = "/storage/emulated/0/downloads"
os.makedirs(output_directory, exist_ok=True)  # Membuat folder jika belum ada

# Daftar situs populer
popular_sites = {
    "1": "YouTube",
    "2": "TikTok",
    "3": "Twitter",
    "4": "Dailymotion",
    "5": "Instagram",
    "6": "Facebook",
    "7": "Twitch",
    "8": "Lainnya"
}

# Tampilan menu
print(Fore.YELLOW + "=" * 60)
print(Fore.CYAN + "    Selamat datang di Program Pengunduh Video & Audio!    ")
print(Fore.YELLOW + "=" * 60)
for key, value in popular_sites.items():
    print(Fore.GREEN + f"{key}. {value}")
print(Fore.YELLOW + "=" * 60)

# Input pilihan situs
site_choice = input(Fore.CYAN + "Masukkan pilihan Anda (1-8): ").strip()

# Menentukan situs berdasarkan pilihan
if site_choice in popular_sites and site_choice != "8":
    site_name = popular_sites[site_choice]
elif site_choice == "8":
    print(Fore.YELLOW + "\nMenampilkan daftar situs yang didukung yt-dlp...\n")

    # Mengambil daftar extractor yt-dlp
    result = subprocess.run(["yt-dlp", "--list-extractors"], capture_output=True, text=True)
    extractors = result.stdout.split("\n")

    # Menampilkan daftar dengan nomor
    extractor_list = [e.strip() for e in extractors if e.strip()]
    for idx, site in enumerate(extractor_list, start=1):
        print(Fore.GREEN + f" {idx}. {site}")

    print(Fore.YELLOW + "=" * 60)

    # Memilih situs berdasarkan nomor
    while True:
        try:
            site_number = int(input(Fore.CYAN + "Masukkan nomor situs yang ingin Anda gunakan: ").strip())
            if 1 <= site_number <= len(extractor_list):
                site_name = extractor_list[site_number - 1]
                break
            else:
                print(Fore.RED + "Nomor tidak valid, coba lagi.")
        except ValueError:
            print(Fore.RED + "Masukkan angka yang Benar.")
else:
    print(Fore.RED + "Pilihan tidak valid. Program akan keluar.")
    exit()

# Input URL
url = input(Fore.CYAN + f"\nMasukkan URL video dari {site_name}: ").strip()
if not url:
    print(Fore.RED + "URL tidak boleh kosong.")
    exit()

# Pilih format (video/audio)
choice = input(Fore.CYAN + "\nPilih format (video/audio) atau tekan Enter untuk default (video): ").strip().lower()

# Konfigurasi yt-dlp
options = {
    "outtmpl": os.path.join(output_directory, "%(title)s.%(ext)s"),  # Nama file output
}

if choice in ["", "video"]:
    options.update({
        "format": "bestvideo+bestaudio/best",  # Download kualitas terbaik
        "merge_output_format": "mp4",  # Format output untuk video
    })
elif choice == "audio":
    options.update({
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    })
else:
    print(Fore.RED + "Pilihan tidak valid. Pilih antara 'video' atau 'audio'.")
    exit()

# Download menggunakan yt-dlp
print(Fore.YELLOW + f"\nSedang mendownload {choice if choice else 'video'} dari {site_name}...")
try:
    with YoutubeDL(options) as ydl:
        ydl.download([url])
    print(Fore.GREEN + f"\n{choice.capitalize() if choice else 'Video'} berhasil disimpan di folder {output_directory}")
except Exception as e:
    print(Fore.RED + f"Terjadi kesalahan: {e}")



import os
os.system("python downloader.py")
