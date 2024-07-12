# Using reportLab to create pdfs which are going to manage all of the invoice creation.
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import helperFunctions
from tkinter import *
from tkinter.ttk import *

# functions used in the UI:
label_font_reg = ("Myriad", 12)
label_font_bold = ("Myriad", 12, "bold")
label_font_italic = ("Myriad", 12, "italic")

def displayInfo():
    label_text = "Select the Information to generate an invoice."
    Label(root, text = label_text, font = label_font_reg).pack()

def invoiceNumLabel():
    label_text = "Invoice number ?"
    Label(root, text = label_text, font = label_font_reg).pack(side=LEFT)
    Button(root, text = "Submit").pack(side=RIGHT)
    Entry(root, width=15).pack(side=RIGHT)
# MAIN:

# Set up the UI window
root = Tk()
root.title('Invoice Generator')
root.geometry(f"{500}x{500}")

# Design the window
displayInfo()
invoiceNumLabel()

# Run the window
root.mainloop()

my_title = helperFunctions.createInvoiceTitle(256)
#canvas = Canvas(my_title, pagesize= (8.5 * inch, 11 * inch))
#canvas.setFont("Times-Roman", 12)
#canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
#canvas.save()
