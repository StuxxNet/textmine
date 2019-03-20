import PyPDF2, sys
from os import listdir
from os.path import isfile, join

def list_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def loop_files(files_list):
    try:
        for archive in files_list:
            pdf_loaded = load_file(archive)
            pdf_object = create_python_pdf(pdf_loaded)
            read_pdf(pdf_object,archive)
    except Exception as e:
        print("Error during the loop of files.\nError:{}".format(e))    

def load_file(file):
    try:
        return open("data/{}".format(file),"rb")
    except Exception as e:
        print("Error during the load of the file.\nError:{}".format(e))

def create_python_pdf(pdf_file):
    try:
        return PyPDF2.PdfFileReader(pdf_file)
    except Exception as e:
        print("Error during the generation of the PDF file.\nError:{}".format(e))

def read_pdf(pdf_object,archive):
    try:
        num_pages = pdf_object.numPages        
        count = 0
        text = ""
        while count < num_pages:
            pageObj = pdf_object.getPage(count)
            count +=1
            text += pageObj.extractText()
        encoded_text = text.encode("utf16")
        export = open("/export/{}.txt".format(archive), "wb")
        export.write(encoded_text)
    except Exception as e:
        print("Error during the PDF reading.\nError:{}".format(e))

if __name__ == '__main__':
    pdfs = list_files("/data")
    loop_files(pdfs)