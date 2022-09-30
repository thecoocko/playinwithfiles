from Modules.Encrypt import encryptor
from Modules.Encrypt import alphabet


class Decrypt:
    def __init__(self,text,lang,step):
        self.text = text
        self.lang = lang
        self.__step = step

    @property
    def step(self):
        return self.__step
   
    @step.setter
    def step(self,step):
        self.__step=step
    
    def decryptor():
        decryptedMessage = ''
        for i in encryptedMessage:
            place = alphabet[lang].find(i)
            place = place - step
            if i in alphabet[lang]:
                encryptedMessage += alphabet[lang][place]
            else: 
                decryptedMessage += i
        return decryptedMessage