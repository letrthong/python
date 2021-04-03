# pip install fpdf
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
imagelist =[]
imagelist.append('./image/photo_2021-04-03_17-28-42.jpg')

x,y,w,h = 0,0,200,250
for image in imagelist:
    pdf.add_page()
    pdf.image(image ,x,y,w,h)
pdf.output("yourfile.pdf", "F")
