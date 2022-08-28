from Modules.Reader import Reader
from Modules.Writer import Writer
from Modules.FileInformation import properties


def main():
    # filename = input('filename: ')
    # filename = 'someText.txt'
    # filename = 'someDoc.docx'
    # filename = 'someSheet.xlsx'
    filename = 'someJson.json'
    
    # text = {'asdasd':[1,2,3,4],'asdasdasdasdasdasd':[123213213,123123122131231231231231233123,444444,'f'],'sadasdsad':21}
    # text = 'asdasdasdasdasdasdasdl;asld;l; l;las;l akflk dn ndvn jfhg fjh'
    # writer = Writer(filename, text)
    # reader = Reader(filename)
    # print(reader.file_reader_json(filename))
    # print(reader.file_reader_doc(filename))
    # print(reader.file_reader_excel(filename))
    # print(writer.file_write_txt(filename, text))
    # print(writer.file_write_docx(filename,text))
    # print(writer.file_write_excel(filename,text))
    # print(writer.file_write_json(filename,text))
    # print(reader.file_reader_txt(filename))
    print(properties(filename))
    


if __name__ == '__main__':
    main()
