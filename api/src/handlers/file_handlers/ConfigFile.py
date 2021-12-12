from .src.MetaFile import MetaFile
import os 
import json

#Description General purpose iofile module. Reads and writes files.
#How to use: 
# OpenConfigurationFile() get the content of the configuration file once and the close it
# GetConfiguration() return a dictionary with the specified field within the configuraion file
# Author : Robin Viera
#Created : 7/11/2021
#Tested : No
#Last update : 7/11/2021

class ConfigFile():

    __instance=None
    
    def __init__(self, path, logs=None) -> None:
        
        super().__init__()
        if ConfigFile.__instance != None:
            raise Exception("ConfigFile instance can only be implemented once")
        
        ConfigFile.__instance=self
        self.__configuration=None
        self.__path=path
        self.__logs=logs
   
   
   
    @staticmethod
    def GetInstance(path=None,logs=None):
        
        if ConfigFile.__instance == None:
            
            if path == None :
                raise Exception("ConfigFile is not instanciated. Instance requires at least one argument : path")
            ConfigFile(path,logs=logs)

        return ConfigFile.__instance
        
        

    def _FileExist(self) -> bool:
        
        return os.path.isfile(self.__path)



    def OpenConfigurationFile(self) -> bool:
        
        
        if self._FileExist() == False:
            return False

        try:

            file=open(self.__path,"r")
            self.LogMessage(f"Access to file : {self.__path}","info")
            content=file.read()
            self.__configuration=json.loads(content)
            file.close()
            if file.closed == True:
                self.LogMessage(f"File closed","info")
                return True
            
            self.LogMessage(f"File cannot closed","error")
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



    def GetConfiguration(self)->dict:
        
        if self.__configuration==None:
            self.LogMessage(f"Configuration not loaded yet","warning")
            return False
                
        return self.__configuration
            




    def LogMessage(self, message, message_type=""):
        
        if self.__logs==None:

            print(message)

        else:
            self.__logs.LogMessage(message,message_type)