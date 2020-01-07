# #import all the packages
# from PIL import Image
# import pytesseract
# import argparse
# import cv2
# import os

# #argument construct and parsing it

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help=r"C:\Users\Asish.Asish\Documents\EXE\HK_OCR_Engine\Tesseract-OCR-4.0\tessdata\example3.jpg")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocess to be done")
# args = vars(ap.parse_args())

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())