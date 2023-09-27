from PIL import Image, ImageDraw, ImageFont

# Membuat gambar kosong
image = Image.new('RGB', (800, 600), color='white')

# Membuat objek draw
draw = ImageDraw.Draw(image)

# Menambahkan teks
font = ImageFont.truetype('arial.ttf', size=36)
text = "Yesus, berlubang paku di tangan-Nya,\nBukti kasih-Nya untuk kita selalu.\nDalam penderitaan, Ia mengasihi kita,\nKeselamatan abadi oleh darah-Nya."
draw.text((100, 100), text, fill='black', font=font)

# Menyimpan gambar
image.save('generated_image.png')