''' opening and extracting the first page of the pdf

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()

'''

''' decrypting the encrypted pdf 
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
pdfReader.getPage(0)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)

'''
