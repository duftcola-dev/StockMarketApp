
from json.decoder import JSONDecodeError
from .src.MetaFile import MetaFile
import os 
import json

#Description General purpose iofile module. Reads and writes json files.
#How to use: 
# Openfile() keeps the buffer enabled (the file remains open) until is decided to close it with CloseFile
# Author : Robin Viera
#Created : 7/11/2021
#Tested : No
#Last update : 7/11/2021


class JsonFile(MetaFile):
    
    __instance=None

    def __init__(self, path, logs=None) -> None:
        super().__init__()

        if JsonFile.__instance != None:
            raise Exception("JsonFile is already implemented")
        
        JsonFile.__instance=self
        self.file_buffer=None
        self.__path=path
        self.__logs=logs
        self.__modes=["r","w"]


    @staticmethod
    def GetInstance(path=None,logs=None):
        
        if JsonFile.__instance== None:
            if path==None :
                raise Exception("JsonFile instance is not instanciated, this instance requires at least one argument : path")
            JsonFile(path,logs=logs)

        return JsonFile.__instance



    def _FileExist(self) -> bool:
        
        return os.path.isfile(self.__path)



    def OpenFile(self,mode) -> bool:
        
        
        if self._FileExist() == False:
            return False

        
        if mode not in self.__modes:
            self.LogMessage(f"No valid mode was provided, valid modes for JSON files are w,r","warning")
            return False

        try:

            self.file_buffer=open(self.__path,mode)
            self.LogMessage(f"Access to file : {self.__path}","info")
            return True

        except FileExistsError as err:
            
            self.LogMessage(f"File does not exist {err}","error")
            return False

        except FileNotFoundError as err:

            self.LogMessage(f"File not found {err}","error")
            return False

        except  Exception as err:

            self.LogMessage(f"Unknown error , cannot read/open file : {err}","error")
            return False



    def CloseFile(self) -> bool:
        
        if self._FileExist() == False:
            return False

        if self.file_buffer==None:
            return False
        
        try:
            self.file_buffer.close()
            if self.file_buffer.closed:
                self.LogMessage(f"File closed","info")
                return True
            
            self.LogMessage(f"Cannot confirm file have been closed","warning")
            return False

        except FileExistsError as err:
            
            self.LogMessage(f"File does not exist {err}","error")
            return False

        except FileNotFoundError as err:

            self.LogMessage(f"File not found {err}","error")
            return False

        except  Exception as err:

            self.LogMessage(f"Unknown error , cannot read/open file : {err}","error")
            return False
       
                

    def ReadFile(self) -> bool:
        
        try:
            json_content=self.file_buffer.read()
            content=json.loads(json_content)
            return content

        except Exception as err:

            self.LogMessage(f"Cannot read file, file buffer broken or intrrupted {err}","error")
            return False



    def WriteFile(self,data) -> bool:
        
        if self._FileExist() == False:
            return False

        if self.file_buffer==None:
            return False

        try:
            json_content=json.dumps(data,indent=4)
            self.file_buffer.write(json_content)
        
        except FileExistsError as err:
            
            self.LogMessage(f"File does not exist {err}","error")
            return False

        except FileNotFoundError as err:

            self.LogMessage(f"File not found {err}","error")
            return False

        except  Exception as err:

            self.LogMessage(f"Unknown error , cannot write file : {err}","error")
            return False
       



    def LogMessage(self, message, message_type=""):
        
        if self.__logs==None:

            print(message)

        else:
            self.__logs.LogMessage(message,message_type)