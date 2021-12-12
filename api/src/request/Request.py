import requests
from requests import HTTPError
from json import JSONDecodeError
from .Source.Meta_Request import IRequest



#Author : Robin Viera
#Date : 29/09/2021
#Version : 1.0
#Tested : No
#Description : Class for general purpose http requests. Singleton class arch.
#last update : 14/10/2021


class Request(IRequest):

    """Description : 
    General purpose http request module.
    The module is quite simple to use. It accepts 4 types of operations so far.
    This module is a singleton and can only be implemented once.

    *Get
    *Post
    *Put
    *Ping

    Ping is a GET method for testing connections urls.
    Parameres for GET are optional.

    The class accepts a configuration in the form of dict passed as optional
    parameter.Use the GetConfigurationField() to get the name of the exact field 
    in the configuration file this class requires:
    

    The class acccepts a log message instance passed as optional parameter.

    Args :

    -->configuration:dict (optional)  . Field name   : request
    
    -->log:log_message_instance(optional)
    
    """


    __instance=None

    def __init__(self,configuration:dict=None,log=None) -> None:

        if Request.__instance != None:
            raise Exception("Request instance can only be implemented once!")
    
        self.__json_response=False
        self.__logs=log
        self.__configuration_field="request"
        self.__configuration_subfield=("json_response","True")
        self.__GetConfiguration(configuration)

        Request.__instance=self


    @staticmethod
    def GetInstance():
        if Request.__instance==None:
            Request()
        
        return Request.__instance


    def Ping(self,url:str):

        return self.__PING(url)


    def Get(self,url:str,header:dict=None,params:dict=None)->dict:

        response=self.__GET(url,header=header,data=params)
        return self.__ResponseHandler(response)


    def Post(self,url:str,header:dict=None,params:dict=None)->dict:

        response=self.__POST(url,header=header,data=params)
        return self.__ResponseHandler(response)


    def Put(self,url:str,header:dict=None,params:dict=None)->dict:

        response=self.__PUT(url,header=header,data=params)
        return self.__ResponseHandler(response)



    def __PING(self,url:str):
        
        result=None
        try:
            result=requests.get(url)

            if result != None:
                return True
                
        except HTTPError as httpError: 

            return False

        except Exception:

            return False




    def __GET(self,url:str,header:dict=None,data:dict=None):

        response=""
        if data==None :
                response=requests.get(url)
        else:
            if header==None:
                self.__LogMessage("info",f"request : {url} {data}")
                response=requests.get(url,params=data)
            else:
                self.__LogMessage("info",f" request : headers:{header} | uri: {url} | params : {data}")
                response=requests.get(url,headers=header,params=data)
        
        return response




    def __POST(self,url:str,header:dict=None,data:dict=None):

        response=""
        if header==None:
            self.__LogMessage("info",f"request : {url} {data}")
            response=requests.post(url,data=data)
        else:
            self.__LogMessage("info",f" request : headers:{header} | uri: {url} | params : {data}")
            response=requests.post(url,headers=header,data=data)

        return response




    def __PUT(self,url:str,header:dict=None,data:dict=None):

        response=""
        if header == None:
            self.__LogMessage("info",f"request : {url} {data}")
            response=requests.put(url,data=data)
        else:
            self.__LogMessage("info",f" request : headers:{header} | uri: {url} | params : {data}")
            response=requests.put(url,headers=header,data=data)
        return response



    def __ResponseHandler(self,response):

        foramted_response=None
        if self.__json_response==True:
            foramted_response=self.__FormatResponseJson(response)
        else:
            foramted_response=self.__FormatResponse(response)

        return foramted_response


    def __FormatResponse(self,response)->dict:

        try:

            result={}
            result["status"]=response.status_code
            result["url"]=response.url
            result["text"]=response.text
            result["encoding"]=response.encoding
            result["bcontent"]=response.content
            if result["encoding"] != None:
                result["content"]=response.content.decode(response.encoding)
            else:
                result["content"]=response.content

            self.__LogMessage("info",f"response : {response.status_code}")
            if response.status_code !=200:
                return False
                
            return result

        except Exception as err:
            self.__LogMessage("error",f"Error while formating response : {err}")
            return False
        



    def __FormatResponseJson(self,response)->dict:

        try:
    
            self.__LogMessage("info",f"response : {response.status_code}")
            result=response.json()

            if result==None:
                return False

            return result

        except JSONDecodeError:

            self.__LogMessage("error","Request module -> Response may be not json type")
            return False
        except Exception:

            self.__LogMessage("error","Request module -> Unknown error on json decoding operation")
            return False



    def __GetConfiguration(self,configuration):

        if configuration==None or type(configuration) is not dict:
            self.__LogMessage("info","Request module -> no configuration provided")
            return

        http_configuration=configuration.get(self.__configuration_field)

        if http_configuration == None:
            self.__LogMessage("warning","Request module -> Configuration not found")
            return

        if http_configuration.get(self.__configuration_subfield[0],None)==self.__configuration_subfield[1]:

            self.__json_response=True
            self.__LogMessage("info","Request module -> configuration loaded. Set to format json reponse")
        else:
            self.__LogMessage("warning","Request module -> Response type format configuration not found")




    def __LogMessage(self,message_type,message):

        if self.__logs==None:
            print(message+"\n")
        else:
            self.__logs.LogMessage(message_type,message)



