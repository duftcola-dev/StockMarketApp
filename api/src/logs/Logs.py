
import threading
import datetime
import sys
from typing import ForwardRef
from .src.interface.MetaLog import MetaLogMessage
from .src.InternalLogs import Logs as Int_Logs
from .src._CheckType import CheckType


# Author: Robin
# Description : This module containes different implementations of the log class
# to be used at convenience . 
# A general purpose method for loggin messages .
# A general purpose factory method that returns log class instance.
# A singleton class for an unique implementation of the log class.
# version 3.1
# tested : yes
# last update: 7/11/2021

#Singleton Log class
class Logs(MetaLogMessage):

    __instance=None

    def __init__(self,log_file=None) -> None:

        if Logs.__instance != None:
            raise Exception("Logs can only be implemented once")

        self.__message=""
        Logs.__instance=self
        self.__log_file=log_file
        

    @staticmethod
    def GetInstance():

        if Logs.__instance==None:
            Logs("")
        
        return Logs.__instance


    
    def LogMessage(self,message_type,message:str):

        self.__type=["warning","error","info"]
    
        if message_type in self.__type:
            
            date=self.__GetDate()
            
            self.__message=""
            self.__message=date+" | "+message_type+" | "+message+"\n"
            
            if message_type == "error" and self.__log_file != None:
                self.__SaveLogMessage(self.__message)

            sys.stdout.write(self.__message)



    def __SaveLogMessage(self,message):
        
        try:
            file=open(self.__log_file,"a")
            file.write(message)
            file.close()
        except FileExistsError:

            sys.stdout.write("ERROR , log class cannot find log file ")

        except Exception as err:

            sys.stdout.write("Log class : Unknown error"+str(err)) 



    def __GetDate(self):
        
        x=datetime.datetime.now()
        Year=str(x.year)
        Month=str(x.month)
        Day=str(x.day)
        Hour=str(x.hour)
        Minute=str(x.minute)
        Second=str(x.second)
        
        return Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second




#Use for inheritance of for debbugin inner class logic
@CheckType
def GetLogInstance(log_file_path=""):

    logs=Int_Logs(log_file=log_file_path)

    return logs


#General purpose log method
@CheckType
def LogMessage(message:str):

    x=datetime.datetime.now()
    Year=str(x.year)
    Month=str(x.month)
    Day=str(x.day)
    Hour=str(x.hour)
    Minute=str(x.minute)
    Second=str(x.second)
    
    message=Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second+" | "+message+"\n"

    sys.stdout.write(message)


