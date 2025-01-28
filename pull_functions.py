import os

import reportlab
from reportlab.pdfgen import canvas



def create_pdf(path: str, images_path: str = "images"):
    os.makedirs(name: f"pdfs", exist_ok=True)

    new_pdf = canvas.Canvas(f"{name}.pdf")
    new_pdf.drawString(x:100, y:100, text:"New PDF")

    images_list = os.listdir(image_path)

    for image in images_list:
        new_pdf.drawImage(image: f"./{images_path}/{image}", x=100, y=y)

    new_pdf.save()