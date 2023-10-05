from PIL import Image
import pytesseract
import os

# Definisikan direktori folder dengan file JPG
folder_path = "./faithfulfootprints"

# Definisikan nama file output TXT
output_file = "faithfulfootprints.txt"

# Fungsi untuk mengonversi gambar ke teks dan menyimpannya dalam file TXT
def convert_image_to_text(image_path):
    try:
        # Buka gambar
        image = Image.open(image_path)
        
        # Ekstrak teks menggunakan Tesseract
        text = pytesseract.image_to_string(image)
        
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")
        return ""

# Membuka file TXT untuk menyimpan hasil
with open(output_file, "w", encoding="utf-8") as txt_file:
    # Loop melalui semua file dalam folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            extracted_text = convert_image_to_text(image_path)
            
            # Menyimpan teks ke dalam file TXT
            if extracted_text:
                txt_file.write(f"===== {filename} =====\n")
                txt_file.write(extracted_text)
                txt_file.write("\n\n")
                
print("Proses selesai. Hasil disimpan dalam", output_file)
