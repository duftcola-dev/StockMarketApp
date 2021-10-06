
from .Source.Interfaces.Meta_Request import MethodsInterface
from .Source import Request_Methods


#Author : Robin Viera
#Date : 29/09/2021
#Version : 1.0
#Tested : None
#Description : Class for general purpose http requests.





class Request(MethodsInterface):

    def __init__(self,configuration:dict="") -> None:
        
        self.json_response=False
        self.Configuration(configuration)
        



    def Ping(self,url:str):

        return Request_Methods.Ping(url)



    def Get(self,url:str,header:dict=None,data:dict=None)->dict:

        return self.__HttpMethods("GET",url,header,data)



    def Post(self,url:str,header:dict=None,data:dict=None)->dict:

        return self.__HttpMethods("POST",url,header,data)



    def Put(self,url:str,header:dict=None,data:dict=None)->dict:

        return self.__HttpMethods("PUT",url,header,data)




    def __HttpMethods(self,method,url,header,data):

        response=""
        if method =="GET":
            response=Request_Methods.Get(url,header=header,data=data)
        if method =="POST":
            response=Request_Methods.Post(url,header=header,data=data)
        if method =="PUT":
            response=Request_Methods.Put(url,header=header,data=data)

        if self.json_response==False:
            return Request_Methods.FormatResponse(response)
        else:
            return Request_Methods.FormatResponseJson(response)


    def Configuration(self,configuration:dict):
        
        if type(configuration) is dict:
            try:

                requestconf=configuration.get("request")
                if requestconf.get("json_response")=="True":
                        self.json_response=True
                    
                        return True
                else:
                    return False
            except:
                return None # No configuration added


