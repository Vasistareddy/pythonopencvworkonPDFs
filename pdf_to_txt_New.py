import sys
import pdfquery

#compile with filename and search content as the command-line arguments
"""This function will search for the given content in the input pdffile and display the page numbers of the pdf if content found.
compilation: python pdf_to_txt_New.py template_image.pdf policy
output:
1

2

policy not found in 3
content found in the pages [1, 2]
"""
def extract_text(page, content):
	try:
		name_element = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal:contains("%s")' % (page, content))
		x = float(name_element.attr('x0'))
		y = float(name_element.attr('y0'))
		h = float(name_element.attr('height'))
		w = float(name_element.attr('width'))
		text = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (x+138.397, y, x+138.397+w, y+h)).text()#static dimensions
		print page
		#print name_element
		print text
		pages.append(page)
	except TypeError:
		print "{1} not found in {0}".format(page,content)
    	
 
if __name__ == "__main__":
	pdf = pdfquery.PDFQuery(sys.argv[1])
	pdf.load()
	pages_in_pdf = len(pdf.pq('LTPage')) #Number of pages
	pages = []
	for page in range(1, pages_in_pdf + 1):
		extract_text(page, sys.argv[2])
	print "content found in the pages {}".format(pages)
	
