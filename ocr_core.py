try:
	from PIL import Image
except ImportError:
	import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Asish.Asish\AppData\Local\Tesseract-OCR\tesseract.exe'

def ocr_core(sample):
	""" 
	processing of images
	"""

	text = pytesseract.image_to_string(Image.open(sample))

	return text

print(ocr_core('random_image.jpg'))

'''
basic understanding for the OCR recognition'
