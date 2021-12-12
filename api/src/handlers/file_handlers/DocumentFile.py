
import abc
from .src.MetaFile import MetaFile
import os 

#Description General purpose iofile module. Reads and writes files.
#How to use: 
# Openfile() keeps the buffer enabled (the file remains open) until is decided to close it with CloseFile
# Author : Robin Viera
#Created : 7/11/2021
#Tested : No
#Last update : 7/11/2021

class DocFile(MetaFile):

    __instance=None
    
    def __init__(self, path, logs=None) -> None:
        super().__init__()
        
        if DocFile.__instance != None:
            raise Exception("ConfigFile instance can only be implemented once")

        DocFile.__instance=self
        self.file_buffer=None
        self.__path=path
        self.__logs=logs
        self.__modes=["r","w","a"]

    @staticmethod
    def GetInstance(path=None,logs=None):
        
        if DocFile.__instance == None:
            
            if path == None:
                raise Exception("DocFile is not instanciated. Instance requires at least one argument : path")
            
            DocFile(path,logs=logs)
            
        return DocFile.__instance



    def _FileExist(self) -> bool:
        
        return os.path.isfile(self.__path)



    def OpenFile(self,mode) -> bool:
        
        
        if self._FileExist() == False:
            return False

        
        if mode not in self.__modes:
            self.LogMessage(f"No valid mode was provided, valid modes for files are a,w,r","warning")
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
            if self.file_buffer.closed :
                self.LogMessage(f"File closed","info")
                return True
            else:
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
            content=self.file_buffer.read()
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

            self.file_buffer.write(data)
            
        
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