#!usr/bin/python
import sys, base64, numpy, cv2, Image
import pyPdf
import PythonMagick

"""this function extract out the pages from a given pdf file as jpgs within the given range starting from first page.
Run: python pdf_to_imagetest.py template_image.pdf 2

compilation syntax:python filename inputpdffilename numberofpages
"""
def pdf2imageextract(pdffilename, pages):
	pdf_im = pyPdf.PdfFileReader(file(pdffilename, "rb"))
	npage = pdf_im.getNumPages() #It gives the number of pages in given input pdf file

	if int(pages) <= npage:
		for p in range(int(pages)):
			im = PythonMagick.Image()
			print type(im)
			im.density('300')
			im.read('{}[{}]'.format(pdffilename,str(p)))#format strings
			im.write('{0}{1}{2}'.format('file_out-',str(p),'.png'))
			blob = PythonMagick.Blob()
			im.write(blob, "png")
			print blob.data
			print type(blob)
			data = PythonMagick.get_blob_data(blob)
			print type(data)
	else:
		print "Page Limit Exceeded"
	

if __name__ == '__main__':
	pdf2imageextract(sys.argv[1],sys.argv[2])
