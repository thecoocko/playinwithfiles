# from Modules.Reader import Reader
import random


global alphabet 
alphabet =  {'ENG':'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'UA':'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'}

def encryptor(text,lang):
    step = 2
    message = str(text).lower()
    encryptedMessage = ''
    for i in message:
        place = alphabet[lang].find(i)
        place = place + step
        if i in alphabet[lang]:
            encryptedMessage += alphabet[lang][place]
        else:
                encryptedMessage += i
    return encryptedMessage




