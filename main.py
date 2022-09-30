from fileinput import filename
from Modules.Encrypt import encryptor
from Modules.Reader import Reader
from Modules.Writer import Writer
from Modules.FileInformation import properties
from Modules.FileSearch import run_fast_scandir


def main():
    
    subfolders, filesrun_fast_scandir = run_fast_scandir('D:\\рандом параша\\trainproject',[".txt"])
    print(filesrun_fast_scandir)
    filename = input("Input your filename:\t")
    reader = Reader(filename)
    LANG = input('ENG - english, UA - ukranian:\t').upper()
    text = encryptor(reader.file_reader_txt(filename),LANG)
    writer = Writer(filename, text)
    print(writer.file_write_txt(filename, text))
    print(reader.file_reader_txt(filename))
    # filename = input('filename: ')
    # filename = 'someDoc.docx'
    # filename = 'someSheet.xlsx'
    # filename = 'someJson.json'
    # print(filesrun_fast_scandir)
    # text = {'asdasd':[1,2,3,4],'asdasdasdasdasdasd':[123213213,123123122131231231231231233123,444444,'f'],'sadasdsad':21}
    # text = 'asdasdasdasdasdasdasdl;asld;l; l;las;l akflk dn ndvn jfhg fjh'
    # print(reader.file_reader_json(filename))
    # print(reader.file_reader_doc(filename))
    # print(reader.file_reader_excel(filename))
    
    # print(writer.file_write_docx(filename,text))
    # print(writer.file_write_excel(filename,text))
    # print(writer.file_write_json(filename,text))
   
    # print(properties(filename))
    
    
    


if __name__ == '__main__':
    main()
