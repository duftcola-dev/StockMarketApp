import os 

from .source.stock_api import Stock
from .source import data_processing
from .source import data_manager
from .source import app_files

#Author : Robin Viera
#version : 1.0
#description : Entry point of the Request moduel. This module makes http requests
# to a stock market api. dowloads the results and created two files. 
# on file in csv format and another in json format both ready to be used for data analysis.
#tested : yes 06/10/2021

class AppRequest:

    def __init__(self) -> None:

        self.response_data={}
        self.path=os.getcwd()
        self.stock=Stock(self.path)
        self.__UpdateAppFilesPaths()



    def RequestStockData(self,symbol:str,date_from="",date_to="",limit="")->bool:

        request_params=self.stock.UpdateParams(symbol,date_from=date_from,date_to=date_to,limit=limit)
        response=self.stock.GetStockData(params=request_params)

        if response == False:
            return False

        self.response_data=data_processing.FormatResponseData(response)
        
        if self.response_data==False:

            return False
            
        return True




    def SaveData(self,file_name:str)->bool:

        path=self.__myfolders.get("data")
        result=data_manager.SaveData(path,file_name,self.response_data.csv_format,self.response_data)
        return result



    def GetData(self,file_name:str)->list:

        self.__UpdateAppFilesPaths()
        path=self.__myfiles.get(file_name)
        return data_manager.GetData(path)




    def GetCsvFilesList(self)->list:
        
        path=self.__myfolders.get("data")
        data_files_list=app_files.ScanDir(path)
        return data_files_list


       
    def __UpdateAppFilesPaths(self):

        self.__app_map=app_files.GetAppFiles(self.path)
        self.__myfiles=self.__app_map.Files_Registry
        self.__myfolders=self.__app_map.Dir_Registry






