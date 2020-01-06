from tesserocr import PyTessBaseAPI

with PyTessBaseAPI(path=r"C:\Users\Asish.Asish\Desktop\tesserocr-master\tesserocr-master\tessdata\tessdata") as api:
    api.SetImageFile("Code_snippet.png")
    print(api.GetUTF8Text())
    
    
# #or else we can do manually 
# from tesserocr import PyTessBaseAPI
# api = PyTessBaseAPI(path=r"C:\Users\Asish.Asish\Desktop\tesserocr-master\tesserocr-master\tessdata\tessdata")
# try:
#make sure the input file should be in the same directory
#     api.SetImageFile("Code_snippet.png")
#     print(api.GetUTF8Text())
# finally:
#     print(api.End())
   


    
