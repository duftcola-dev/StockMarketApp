from .dependencies.ApiRequest import ApiRequest
from .dependencies.ConfigurationLoader import ConfigurationLoader


class Stock:

    def __init__(self,path:str):

        self.configuration=ConfigurationLoader(path)
        self.configuration_data=self.configuration.GetConfiguration()
        self.request=ApiRequest(self.configuration_data)



    def UpdateParams(self,symbol:str,date_from:str="",date_to:str="",limit:str=""):

        if symbol =="" or type(symbol) is not str:
            return False

        params=self.configuration_data.get("api_params")
        params["symbols"]=symbol
        params["date_from"]=date_from
        params["date_to"]=date_to
        params["limit"]=limit
        
        #return only the params that will be used
        to_use_params={}

        for item in params:

            if params[item]!="":
                to_use_params.update({item:params[item]})
        
        return to_use_params



    def GetStockData(self,params:dict=""):
        
        if params == "":
            return False

        if type(params) is not dict:
            return False

        if params.get("symbols") == "":
            return False

        response=self.request.SendRequest(params=params)
        return response


