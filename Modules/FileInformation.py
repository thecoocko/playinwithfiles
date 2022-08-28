import os.path, time, re


def properties(file):
    FILE_PROPERTIES = {
        'FILE_NAME':os.path.basename(file),
        'DATE_OF_CREATION':time.ctime(os.path.getctime(file)),
        'DATE_OF_MODIFICATION':time.ctime(os.path.getctime(file)),
        'TYPE_OF_FILE':re.search('\.[a-zA-z]+',os.path.basename(file)).group(),
        'SIZE':f"{os.path.getsize(file)/1000} KB"
        }
    return FILE_PROPERTIES



