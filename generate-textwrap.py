from PIL import Image, ImageDraw, ImageFont, ImageColor
import datetime
import os
import textwrap


def generate_quotes(quote_text, quote_color, quote_background):
    # Mendapatkan tanggal hari ini
    today = datetime.date.today()
    formatted_date = today.strftime("%Y%m%d")

    # Mengubah format warna ke RGB (jika warna dalam format HEX)
    text_color = ImageColor.getrgb(quote_color)
    background_color = ImageColor.getrgb(quote_background)

    # Membuat gambar kosong
    image = Image.new('RGB', (1080, 1080), color=background_color)

    # Membuat objek draw
    draw = ImageDraw.Draw(image)

    # Menambahkan teks
    text_wrap_size = 40
    font_size = 58
    font = ImageFont.truetype('./fonts/tentang-nanti/demo.otf', size=font_size)
    # font = ImageFont.truetype('./fonts/single-day/regular.ttf', size=font_size)
    # font = ImageFont.truetype('./fonts/something-shine/demo.otf', size=font_size)
    # font = ImageFont.truetype('./fonts/poppin/demo.otf', size=font_size)
    # font = ImageFont.truetype('./fonts/mungil/demo.ttf', size=font_size)

    # Mengukur lebar dan tinggi teks menggunakan textbbox
    text_bbox = draw.textbbox((0, 0), quote_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Menentukan posisi tengah secara horizontal dan vertical
    x_position = (image.width - text_width) // 2
    y_position = (image.height - text_height) // 2

    # Mengatur jarak antar baris
    line_spacing = 10
    # Membuat nama direktori (folder) berdasarkan tanggal hari ini
    result_folder = os.path.join("results", formatted_date)
    # Membuat direktori jika belum ada
    os.makedirs(result_folder, exist_ok=True)
    # Membuat nama file gambar
    image_filename = os.path.join(result_folder, f"{formatted_date}.png")
    # Menggunakan textwrap untuk pembungkus kata
    # Ganti 30 dengan panjang maksimum baris teks yang Anda inginkan
    wrapped_text = textwrap.wrap(quote_text, width=text_wrap_size)

    # Menggambar teks dengan jarak antar baris
    for line in wrapped_text:
        line_bbox = draw.textbbox((0, 0), line, font=font)
        line_width = line_bbox[2] - line_bbox[0]
        line_height = line_bbox[3] - line_bbox[1]
        x_position = (image.width - line_width) // 2
        draw.text((x_position, y_position), line, fill=text_color, font=font)
        y_position += line_height + line_spacing  # Menambahkan jarak antar baris

    # Menyimpan gambar dengan nama berdasarkan tanggal
    image.save(image_filename)


# Contoh penggunaan fungsi dengan teks kutipan
quote_text = "Yesus, berlubang paku di tangan-Nya,\nBukti kasih-Nya untuk kita selalu.\nDalam penderitaan, Ia mengasihi kita,\nKeselamatan abadi oleh darah-Nya."
quote_color = "#fff"
quote_background = "#0231aa"

generate_quotes(quote_text, quote_color, quote_background)
