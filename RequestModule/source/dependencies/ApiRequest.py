from unittest import signals

from requests.models import HTTPError, Response
from .Request.Request import Request



class ApiRequest:


    def __init__(self,configuration) -> None:

        self.__configuration=configuration
        self.__api={}
        self.__params={}
        self.request=Request(configuration)
        self.__GetApiQueries()



    def SendRequest(self,params=None):

        if params == None:
            http_params=self.__params
        else:
            http_params=params

        url=self.__api.get("url")
        
        response=None
        response=self.request.Get(url,header=None,data=http_params)

        if response == None:
            return False
        else:
            return response

        

    def SetSymbol(self,symbol:str):
        
        if self.__params.get("& symbols") != None:
            self.__params["& symbols"]=symbol
            return True
        return False
    

    def GetParams(self):

        return self.__params


    def GetCurrentSymbol(self)->str:

        if self.__params.get("& symbols") != None:
            return self.__params.get("& symbols")
        return False



    def __GetApiQueries(self):

        self.__api=self.__configuration.get("api_url")
        self.__params=self.__configuration.get("api_params")