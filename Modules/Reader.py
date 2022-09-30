import docx 
import pandas as pd
import json


class Reader:
    def __init__(self, file):
        self.__file=file

    @property
    def filename(self):
        return self.__file
   
    @filename.setter
    def filename(self,file):
        self.__file=file
    
    @staticmethod
    def file_reader_excel(file):
        table = pd.read_excel(file)
        tdata  = pd.DataFrame(table)
        return tdata

    @staticmethod
    def file_reader_doc(file):
        text = []
        t = docx.Document(file)
        for word in t.paragraphs:
            text.append(word.text)
        return text

    @staticmethod
    def file_reader_json(file):
        text=""
        with open(file,'r') as buffer:
            text = json.load(buffer)
        return text

    @staticmethod
    def file_reader_txt(file):
        text = []
        with open(file, 'r') as buffer:
            for line in buffer:
                text.append(line)
        return text


