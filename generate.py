from PIL import Image, ImageDraw, ImageFont, ImageColor
import datetime
import os
import random
import uuid
import textwrap

def generate_unique_filename():
    # Menghasilkan UUID (Universally Unique Identifier)
    unique_id = uuid.uuid4()
    return str(unique_id)

def generate_quotes(quote_text, quote_color, quote_background, quote_credit):
    # Mendapatkan tanggal hari ini
    today = datetime.date.today()
    formatted_date = today.strftime("%Y%m%d")

    # Pisahkan daftar warna latar belakang menjadi sebuah daftar Python
    background_colors = quote_background.split(';')
    selected_background = random.choice(background_colors)

    # Mengubah format warna ke RGB (jika warna dalam format HEX)
    text_color = ImageColor.getrgb(quote_color)
    background_color = ImageColor.getrgb(selected_background)

    # Membuat gambar kosong
    image = Image.new('RGB', (1080, 1080), color=background_color)

    # Membuat objek draw
    draw = ImageDraw.Draw(image)

    # Menambahkan efek grain ke latar belakang
    for _ in range(5000):  # Jumlah butiran (sesuaikan dengan keinginan Anda)
        x = random.randint(0, image.width - 1)
        y = random.randint(0, image.height - 1)
        draw.point((x, y), fill=(random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)))

    # Menambahkan teks
    font_size = 58
    font_style = "original;one;two"
    font_selected = font_style.split(';')
    font_path = f'./fonts/tentang-nanti/{random.choice(font_selected)}.otf'
    font = ImageFont.truetype(f'./fonts/tentang-nanti/{random.choice(font_selected)}.otf', size=font_size)

    # Mengukur lebar dan tinggi teks menggunakan textbbox
    text_bbox = draw.textbbox((0, 0), quote_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Menentukan posisi tengah secara horizontal dan vertical
    x_position = (image.width - text_width) // 2

    # Ganti 60 dengan panjang maksimum baris teks yang Anda inginkan
    text_wrap_size = 40
    wrapped_text = textwrap.wrap(quote_text, width=text_wrap_size)

    # Menghitung tinggi total dari semua baris teks yang di-"word wrap"
    total_text_height = len(wrapped_text) * (text_height + 10)

    # Menentukan posisi tengah secara vertikal
    y_position = (image.height - total_text_height) // 2

    # Mengatur jarak antar baris
    line_spacing = 10

    # Membuat nama direktori (folder) berdasarkan tanggal hari ini
    result_folder = os.path.join("results", formatted_date)
    # Membuat direktori jika belum ada
    os.makedirs(result_folder, exist_ok=True)
    # Membuat nama file gambar dengan UUID yang unik
    unique_filename = generate_unique_filename()
    # Membuat nama file gambar
    image_filename = os.path.join(result_folder, f"{formatted_date}_{unique_filename}.png")

    # Menggambar teks dengan jarak antar baris
    for line in wrapped_text:
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_width = line_bbox[2] - line_bbox[0]
        line_height = line_bbox[3] - line_bbox[1]
        x_position = (image.width - line_width) // 2
        draw.text((x_position, y_position), line, fill=text_color, font=font)
        y_position += line_height + line_spacing  # Menambahkan jarak antar baris

    # Menambahkan teks kredit
    credit_font_size = 32
    credit_font = ImageFont.truetype('./fonts/tentang-nanti/demo.otf', size=credit_font_size)
    credit_text_bbox = draw.textbbox((0, 0), quote_credit, font=credit_font)
    credit_text_width = credit_text_bbox[2] - credit_text_bbox[0]
    credit_text_height = credit_text_bbox[3] - credit_text_bbox[1]
    credit_x_position = (image.width - credit_text_width) // 2
    credit_y_position = image.height - credit_text_height - 50  # Mengatur posisi vertikal di bagian bawah
    draw.text((credit_x_position, credit_y_position), quote_credit, fill=text_color, font=credit_font)

    # Menyimpan gambar dengan nama berdasarkan tanggal
    image.save(image_filename)