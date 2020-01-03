from PIL import Image
img = Image.open("receipt_1.jpg")
gray = img.convert('L')
bnw = gray.point(lambda x: 0 if x < 240 else 255, '1')
bnw.save("receipt_1bnw.jpg")
