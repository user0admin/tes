#!/bin/bash

# Menyiapkan akses ke penyimpanan
termux-setup-storage

# Memperbarui paket dan sistem
pkg update && pkg upgrade -y

# Menginstal paket yang diperlukan di Termux
pkg install libexpat openssl python -y
pkg install ffmpeg -y
pip install colorama

# Menginstal dependensi Python
pip install -U "yt-dlp[default]"
pip install mutagen
