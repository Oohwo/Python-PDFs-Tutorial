from PyPDF2 import PdfReader

myPDF = "BeeMovieScript.pdf" # filepath

reader = PdfReader(myPDF)
page = reader.pages[0]
print(page.extract_text())
