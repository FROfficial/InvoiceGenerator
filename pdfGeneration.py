# Using reportLab to create pdfs which are going to manage all of the invoice creation.
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("invoice.pdf")