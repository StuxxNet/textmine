#Importante! Esse código não funciona, por enquanto, para 
#documentos PDF que tenham sido escaneados!

import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join

def list_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def loop_files(files_list):
    for archive in files_list:
        print("Arquivo:{}".format(archive))

def load_file(file):
    try:
        return open(file,'rb')
    except Exception as e:
        print("Error during the load of the file.\nError:{}".format(e))

def create_python_pdf(pdf_file):
    try:
        return PyPDF2.PdfFileReader(arquivo_pdf)
    except Exception as e:
        print("Error during the generation of the PDF file.\nError:{}".format(e))

def read_pdf(pdf_object):
    try:
        num_pages = pdf_object.numPages
        count = 0
        while count < num_pages:
            pageObj = pdf_object.getPage(count)
            count +=1
            text += pageObj.extractText()
        print("PDF Content!\n\n{}".format(text))
    except Exception as e:
        print("Error during the PDF reading.\nError:{}".format(e))

if __name__ == '__main__':
    pass