from instagram_private_api import Client, MediaRatios
from instagram_private_api_extensions import media
from dotenv import load_dotenv
import os
from function import *
# Muat variabel lingkungan dari file .env
load_dotenv()

# Mengambil nilai username dan password dari variabel lingkungan
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

login_pc(username, password)

# Membuat koneksi
# api = Client(username, password)

# photo_path = "./results/20230928/20230928.jpeg"
# caption = "Ini adalah caption untuk gambar Anda. #instabot #python"
# photo_data, photo_size = media.prepare_image(photo_path, aspect_ratios=MediaRatios.standard)
# response = api.post_photo(photo_data, photo_size, caption)

# # Periksa respons untuk memastikan foto berhasil diunggah
# if response.get('status') == 'ok':
#     print('Foto berhasil diunggah!')
# else:
#     print('Gagal mengunggah foto.')
