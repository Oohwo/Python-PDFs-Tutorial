# Request PDF from website
import requests

url = "https://www3.nd.edu/~instres/CDS/2021-2022/CDS_2021-2022.pdf"

print("Downloading file: ")
response = requests.get(url)
  
pdf = open("CDS.pdf", 'wb')
pdf.write(response.content)
pdf.close()
print("File downloaded")
  
print("All PDF files downloaded")

# Print first page of PDF
reader = PdfReader("CDS1.pdf")
page = reader.pages[0]
print(page.extract_text())
