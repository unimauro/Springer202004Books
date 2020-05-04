#############################################
###
### Download Springer Books
### Corona Virus Time
###
### carlos@cardenas.pe
###
###  GPL 3.0 v
###
### 27/04/2020
###
#############################################
import PyPDF2
import urllib3
import os
import wget


def download_book_from_page(page_url):
    http = urllib3.PoolManager()

    res = http.request('GET', page_url)

    title = ''.join(res.data.decode('utf-8').split('h1')[1].split('>')[1].split('<')[0].split('/')[0])+".pdf"
    
    # skip books already downloaded
    if os.path.isfile(title):
        return

    download_url = "https://link.springer.com/content/"+res.data.decode('utf-8').split('Download book PDF')[0].split('content/')[1].split('title')[0].split('.pdf')[0]+".pdf"

    wget.download(download_url, title)


def process_books_in_pdf(pdf):
    for i in range(0, pdf.numPages):
        lines = pdf.getPage(i).extractText().split('\n')

        for i in range(len(lines)):
            if lines[i].startswith("http://"):
                # changing protocol from http to https
                url = "https://"+lines[i][7:]
                print(url)
                download_book_from_page(url)


def main():
    file = open('Spring.pdf', 'rb')
    pdf = PyPDF2.PdfFileReader(file)
    process_books_in_pdf(pdf)


main()
