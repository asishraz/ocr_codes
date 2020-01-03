try:
	from PIL import Image
except ImportError:
	import Image

import pytesseract

#tesseract-executable file path: C:\Users\Asish.Asish\AppData\Local\Tesseract-OCR\tesseract.exe

#for including the tesseract executable file:
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Asish.Asish\AppData\Local\Tesseract-OCR\tesseract.exe"

#showing  image to string using image_to_string function
# print(pytesseract.image_to_string(Image.open("test.png")))

#shwoing image to french text using the same function used as above
# img = r"test-european.jpg"
# print(pytesseract.image_to_string(Image.open(img)))


# print(pytesseract.image_to_string("test.png"))
# print("first image is above")

print("##########################################################")
# print(pytesseract.image_to_string("images.txt"))



# #timeout the tesseract job after some period of time
# try:
# 	print(pytesseract.image_to_string("test.jpg", timeout=2))
# 	print(pytesseract.image_to_string("test.jpg", timeout=0.5))
# except RunTimeError as timeout_error:
# 	#tesseract processing is terminated
# 	pass


#getting bounding box estimates
# print(pytesseract.image_to_boxes(Image.open("test.png")))

#getting verbose data inc boxes, line and page numbers
# print(pytesseract.image_to_data(Image.open("test.png")))


#getting info about orientation and script detection
# print(pytesseract.image_to_osd(Image.open("test.png")))


# #getting a searchable pdf
# pdf = pytesseract.image_to_pdf_or_hocr("test.png", extension="pdf")
# with open("test.pdf", "w+b") as f:
# 	f.write(pdf)

# #getting HOCR output
# hocr = 	pytesseract.image_to_pdf_or_hocr("test.png", extension="hocr")


