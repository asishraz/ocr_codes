try:
	from PIL import Image
except ImportError:
	import Image

import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Asish.Asish\AppData\Local\Tesseract-OCR\tesseract.exe"


print(pytesseract.image_to_string(Image.open("test.jpg")))

pdf = pytesseract.image_to_pdf_or_hocr("test.png", extension="pdf")
with open("test.pdf", "w+b") as f:
	f.write(pdf)

