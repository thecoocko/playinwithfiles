import json
import docx 
import pandas as pd
from Modules.Reader import Reader


class Writer(Reader):
    def __init__(self, file, text):
        Reader.__init__(self,file)
        self.text = text

    def notification():
        return f"Source has been updated\n"
    
    @staticmethod
    def file_write_txt(file,text):
        # for i in range(len(text)):
        #     if isinstance(text[i],int) or isinstance(text[i], float):
        #         text[i] = str(text[i])
        with open(file, 'a') as buffer:
            buffer.write(text)
        return  Writer.notification() + str(Reader.file_reader_txt(file))
    
    @staticmethod
    def file_write_docx(file,text):
        doc = docx.Document(file)
        for i in range(len(text)):
            if isinstance(text[i],int) or isinstance(text[i], float):
                text[i] = str(text[i])
        doc.add_paragraph(' '.join(text))
        doc.save(file)
        return Writer.notification() + Reader.file_reader_doc(file)
            
    
    @staticmethod
    def file_write_excel(file,text):
        try:
            table = pd.read_excel(file)
            tdata  = pd.DataFrame(table)
            for i in text.keys():
                tdata[i] = text[i]
            tdata.to_excel(file, index=False)
            return Writer.notification() + Reader.file_reader_excel(file)
        except ValueError:
                print("Value should be a dict type")
    
    @staticmethod
    def file_write_json(file,text):
        with open(file,'a') as buffer:
            json.dump(text,buffer)

        return Writer.notification() + Reader.file_reader_txt(file) 



