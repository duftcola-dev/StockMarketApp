import sys
import os
from inspect import  currentframe, getframeinfo
import threading
import datetime


# Author : Robin
# Description : General purpose log class  mostly meant to be inherited and used within another class. 
# Tested : yes
# last update : 1/9/2021

class Logs():


    def __init__(self,log_file:str=None) -> None:
        self.__message=""
        self.__log_file=log_file
        pass


    def LogMessage(self,message_type,message:str):

        self.__type=["warning","error","info"]
    
        if message_type in self.__type:
            
            date=self.__GetDate()

            self.__message=""
            self.__message=date+" | "+message_type+" | "+message+"\n"

            if message_type == "error" and self.__log_file !=None:
                self.__SaveLogMessage(self.__message)

            sys.stdout.write(self.__message)



    def __SaveLogMessage(self,message):
        
        try:
            file=open(self.__log_file,"a")
            file.write(message)
            file.close()
        
        except FileExistsError as err:

            print(f" ERR file doesnt exist {err}")

        except FileNotFoundError as err:

            print(f"ERR File not found : {err}")


        except Exception:

            print("Err unknown exception")



    def __GetDate(self):
        
        x=datetime.datetime.now()
        Year=str(x.year)
        Month=str(x.month)
        Day=str(x.day)
        Hour=str(x.hour)
        Minute=str(x.minute)
        Second=str(x.second)
        
        return Day+"|"+Month+"|"+Year+" - "+Hour+":"+Minute+":"+Second


