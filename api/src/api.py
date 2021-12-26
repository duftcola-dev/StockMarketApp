
import os
from .handlers.FileExplorer import FileExplorer
from .handlers.FileHandler import  FileHandler
from .handlers.utils.utils import FormatSymbols
from .logs.Logs import Logs
from .request.Request import Request
from .models.ApiResponse import ApiResponse
from .adapter.Adapter import ResponseAdapter


#mapping files
path=os.getcwd()
file_explorer=FileExplorer()
file_explorer.MapFiles(path,ignore_this_files=["mapping","request","handlers","__pycache__"])

#path
configuration_path=file_explorer.GetFilePath("config.json")
log_path=file_explorer.GetFilePath("logs.txt")


#instanciating utils
logs=Logs(log_file=log_path)
handler=FileHandler(configuration_path,logs=logs.GetInstance())
http_request=Request(configuration=handler.GetConfiguration(),log=logs.GetInstance())




class Api(ResponseAdapter,ApiResponse):

    def __init__(self) -> None:
        super().__init__()

        self.api=None
        self.logs=logs.GetInstance()
        self.request=http_request
        self.__GetApiConfig(handler.GetConfiguration())
        self.__FormatSymbols=FormatSymbols

        if self.api==None:
            self.logs.LogMessage("error","Failed to load api configuration")
            raise Exception("Failed to load api configuration")
        else: 
            self.logs.LogMessage("info","api configuration loaded.")


    def __GetApiConfig(self,configuration):
        
        self.api=configuration.get("api")


    def GetTickers(self):

        url=self.api.get("tickers")
        params=self.api.get("params")
        response=self.request.Get(url,header=None,params=params)

        if response!= False:
            return self.GetTickerList(self.CreateTickersList,response)

        self.logs.LogMessage("error","Api --> GetTickers : No response")
        return None
        
    
    def GetData(self,tickers:list,type="eod")->dict:

        url=self.api.get(type)
        params=self.api.get("params")
        params=self.__FormatSymbols(params,tickers)
        response=self.request.Get(url,header=None,params=params)

        if response != False:
            return self.GetTickersData(self.CreateTickersData,response)

        self.logs.LogMessage("error","Api --> GetData : No response")
        return None




