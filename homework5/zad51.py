#!/usr/bin/python3
import os

def find_pdf_size(top):
    pdf_bytes = 0   # the number of bytes taken by PDF files
    for root, dirs, files in os.walk(top):   # walking top-down (default)
        for file in files:
            if file.lower().endswith(".pdf"):   # for *.PDF files
                path = top + "\\" + file
                pdf_bytes += os.stat(path).st_size  #muszę podawać całą ścieżkę, dlaego wyżej zrobiłam path, natomiast powinno działać z samym file (jak na wykładzie), u mnie nie działa
    return pdf_bytes

top = "E:\kurs_Python" 
pdf_bytes = find_pdf_size(top)


print("Size of PDF files in {} directory is {}".format(top, pdf_bytes))
input()