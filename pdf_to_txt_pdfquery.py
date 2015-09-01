"""
this program uses pdfquery to load and search for the given label in the input pdf.
It displays the policy number as output.
"""
import pdfquery
pdf = pdfquery.PDFQuery("template_image.pdf")
pdf.load()
label = pdf.pq('LTTextLineHorizontal:contains("Policy Number")')[0]
left_corner = float(label.get('x0'))
bottom_corner = float(label.get('y0'))
height = float(label.get('height'))
width = float(label.get('width'))
text = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner, bottom_corner, left_corner+width, bottom_corner+height)).text()
num_of_instances = len(pdf.pq('LTTextLineHorizontal'))
print text#printing out the text matching for the given label

