from instagram_private_api import Client, ClientCompatPatch
from dotenv import load_dotenv
import os

# Muat variabel lingkungan dari file .env
load_dotenv()

# Mengambil nilai username dan password dari variabel lingkungan
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

api = Client(username, password)
media_path = "./results/20230927/20230927.png"
caption = "Ini adalah caption untuk gambar Anda. #instabot #python"
size = (1080, 1080)

with open(media_path, 'rb') as photo_file:
    photo_data = photo_file.read()

# Menggunakan foto_file sebagai konten foto
api.post_photo(photo_data, size, caption=caption, to_reel=False)
