# PDF to Images
# pip install PyMuPDF
import fitz

import sys, fitz  # import the bindings
doc = fitz.open("a.pdf")   # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG


##Extract image from pdf
doc = fitz.open("a.pdf") # open a document

for page_index in range(len(doc)): # iterate over pdf pages
	page = doc[page_index] # get the page
	image_list = page.get_images()

	# print the number of images found on the page
	if image_list:
		print(f"Found {len(image_list)} images on page {page_index}")
	else:
		print("No images found on page", page_index)

	for image_index, img in enumerate(image_list, start=1): # enumerate the image list
		xref = img[0] # get the XREF of the image
		pix = fitz.Pixmap(doc, xref) # create a Pixmap

		if pix.n - pix.alpha > 3: # CMYK: convert to RGB first
			pix = fitz.Pixmap(fitz.csRGB, pix)

		pix.save("page_%s-image_%s.png" % (page_index, image_index)) # save the image as png
		pix = None

##Extract text from pdf
doc = fitz.open("a.pdf") # open a document
out = open("output.txt", "wb") # create a text output
for page in doc: # iterate the document pages
	text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
	out.write(text) # write text of page
	out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()

##Merger 2 PDF
doc_a = fitz.open("a.pdf") # open the 1st document
doc_b = fitz.open("b.pdf") # open the 2nd document

doc_a.insert_pdf(doc_b) # merge the docs
doc_a.save("a+b.pdf")

##Merging PDF files with other types of file
doc_a = fitz.open("a.pdf") # open the 1st document
doc_b = fitz.open("b.svg") # open the 2nd document

doc_a.insert_file(doc_b) # merge the docs
doc_a.save("a+b.pdf") # save the merged document with a new filename

##Adding a watermark to a PDF
doc = fitz.open("document.pdf") # open a document

for page_index in range(len(doc)): # iterate over pdf pages
	page = doc[page_index] # get the page

	# insert an image watermark from a file name to fit the page bounds
	page.insert_image(page.bound(),filename="watermark.png", overlay=False)

doc.save("watermarked-document.pdf") # save the document with a new filename

##Adding an image to a PDF
doc = fitz.open("document.pdf") # open a document

for page_index in range(len(doc)): # iterate over pdf pages
	page = doc[page_index] # get the page

	# insert an image logo from a file name at the top left of the document
	page.insert_image(fitz.Rect(0,0,50,50),filename="my-logo.png")

doc.save("logo-document.pdf") # save the document with a new filename

##Rotating a PDF
doc = fitz.open("test.pdf") # open document
page = doc[0] # get the 1st page of the document
page.set_rotation(90) # rotate the page
doc.save("rotated-page-1.pdf")

##Cropping a PDF
doc = fitz.open("test.pdf") # open document
page = doc[0] # get the 1st page of the document
page.set_cropbox(fitz.Rect(100, 100, 400, 400)) # set a cropbox for the page
doc.save("cropped-page-1.pdf")

##Attaching Files

doc = fitz.open("test.pdf") # open main document
attachment = fitz.open("my-attachment.pdf") # open document you want to attach

page = doc[0] # get the 1st page of the document
point = fitz.Point(100, 100) # create the point where you want to add the attachment
attachment_data = attachment.tobytes() # get the document byte data as a buffer

# add the file annotation with the point, data and the file name
file_annotation = page.add_file_annot(point, attachment_data, "attachment.pdf")

doc.save("document-with-attachment.pdf") # save the document

##Embedding Files

doc = fitz.open("test.pdf") # open main document
embedded_doc = fitz.open("my-embed.pdf") # open document you want to embed

embedded_data = embedded_doc.tobytes() # get the document byte data as a buffer

# embed with the file name and the data
doc.embfile_add("my-embedded_file.pdf", embedded_data)

doc.save("document-with-embed.pdf") # save the document

##Deleting Pages

doc = fitz.open("test.pdf") # open a document
doc.delete_page(0) # delete the 1st page of the document
doc.save("test-deleted-page-one.pdf") # save the document

doc = fitz.open("test.pdf") # open a document
doc.delete_pages(from_page=9, to_page=14) # delete a page range from the document
doc.save("test-deleted-pages.pdf") # save the document