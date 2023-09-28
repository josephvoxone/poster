from generate import generate_quotes

# Contoh penggunaan fungsi dengan teks kutipan dan teks kredit
with open("./quote.text", "r") as file:
    quotes = file.read().splitlines()

# Iterate through the quotes and generate images
quote_color = "#000"
quote_background = "#e8ccbc;#f2f2f2;#d0c9bf;#d7c9b5;#d3e8e1;#b0bea2;#cdb0b0;#b9deea"
quote_credit = "@everydaywillbeokay"

for quote_text in quotes:
    generate_quotes(quote_text, quote_color, quote_background, quote_credit)