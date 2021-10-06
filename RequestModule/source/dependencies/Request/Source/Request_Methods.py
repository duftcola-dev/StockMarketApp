
import requests
from requests.models import HTTPError


#Author : Robin Viera
#Date : 29/09/2021
#Description : HTTP client for general purpose.



def Ping(url:str)->bool:

    result=None
    try:
        result=requests.get(url)

        if result != None:
            return True
            
    except HTTPError as httpError: 

        return False

    except Exception:

        return False




def Get(url:str,header:dict=None,data:dict=None)->dict:


    if not CheckTypes(url,data):

        return False
        
    try:

        if data==None :
            result=requests.get(url)
        else:
            if header==None:
                result=requests.get(url,params=data)
            else:
                result=requests.get(url,headers=header,params=data)
        
        return result

    except HTTPError :

        return False

    except Exception:

        return False




def Post(url:str,header:dict=None,data:dict=None):


    if data == None:
        return False

    if not CheckTypes(url,data):

        return False

    try:

        if header==None:
            result=requests.post(url,data=data)
        else:
            result=requests.post(url,headers=header,data=data)

        return result

    except HTTPError :

        return False

    except Exception:

        return False





def Put(url:str,header:dict=None,data:dict=None):

    if data == None:
        return False

    if not CheckTypes(url,data):

        return False

    try:

        if header==None:
            result=requests.put(url,data=data)
        else:
            result=requests.put(url,headers=header,data=data)
        
        return result

    except HTTPError :

        return False

    except Exception:

        return False




#++++++++++++Chechks section+++++++++++++++++++++++++

def CheckTypes(url:str="",data:dict=""):

    if url=="" or data =="":
        return False

    if data==None:# data is optional
        result2=True
        result1=CheckUrlType(url)
    else:
        result2=CheckDictType(data)
        result1=CheckUrlType(url)

    if result1==False or result2==False:
        return False

    return True



def CheckDictType(data:dict)->bool:

    if type(data) == dict:

        return True

    return False



def CheckUrlType(data:str)->bool:

    if type(data) ==str:

        return True

    return False



def FormatResponse(response)->dict:

    try:

        result={}
        result["status"]=response.status_code
        result["url"]=response.url
        result["text"]=response.text
        result["encoding"]=response.encoding
        result["bcontent"]=response.content
        result["content"]=response.content.decode(response.encoding)

        return result

    except Exception:

        return False
    



def FormatResponseJson(response)->dict:

    try:
        result=""
        result=response.json()
        return result

    except requests.exceptions.JSONDecodeError:

        print("Response may be not json type")
        return False
    except Exception:

        print("Unkown error on json decoding operation")
        return False