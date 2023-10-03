from generate import generate_quotes

# Contoh penggunaan fungsi dengan teks kutipan dan teks kredit
with open("./quote.text", "r") as file:
    quotes = file.read().splitlines()

# Iterate through the quotes and generate images
quote_color = "#000"
quote_background = "#deebf3;#e7dcc6;#fff;#e7dcc6;#f1ebdf;#f2eadf;#e9e7da"
quote_credit = "@everydaywillbeokay"

for quote_text in quotes:
    generate_quotes(quote_text, quote_color, quote_background, quote_credit)
    # Menyimpan kutipan yang sudah digenerate ke dalam file quote_generated.txt
    # with open("quote_generated.txt", "a") as file:
    #     file.write(quote_text + "\n")
