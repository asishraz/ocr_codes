from tesserocr import PyTessBaseAPI

with PyTessBaseAPI(path=r"C:\Users\Asish.Asish\Desktop\tesserocr-master\tesserocr-master\tessdata\tessdata") as api:
    api.SetImageFile("Code_snippet.png")
    print(api.GetUTF8Text())
    
    
