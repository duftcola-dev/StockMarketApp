
from .dependencies.FileManager import FilesModule


def CreateFolder(path:str)->bool:

    FilesModule.CreateDir(path)
    result=FilesModule.CheckDir(path)
    return result



def SaveData(path:str,file_name:str,data_csv:list,data_json:object):

    
    result=CreateCsvFile(path,file_name)

    if type(result) is bool :
        return False

    result=SaveDataCsv(result,data_csv)

    if result == False :
        return False


    result=CreateJsonFile(path,file_name)

    if type(result) is bool :
        return False

    result=SaveDataJson(result,data_json)

    if result == False :
        return False

    return result



def CreateCsvFile(path:str,file_name:str)->bool:

    file_name=file_name+".txt"
    creation_result=FilesModule.CreateFile(path,file_name)

    if type(creation_result) is bool:
        return False

    result=FilesModule.CheckFile(creation_result)

    if result == False:
        return False

    return creation_result



def CreateJsonFile(path:str,file_name:str)->bool:

    file_name=file_name+".json"
    creation_result=FilesModule.CreateFile(path,file_name)

    if type(creation_result) is bool:
        return False

    result=FilesModule.CheckFile(creation_result)
    
    if result==False:
        return result

    return creation_result




def SaveDataJson(path:str,data:object):

    result=FilesModule.CheckFile(path)

    if result == False:
        print("Cannot save data , Json file doesnt exist")
        return False
    
    result=FilesModule.WriteJsonFile(path,data)

    return result



def SaveDataCsv(path:str,data:list):

    result=FilesModule.CheckFile(path)

    if result == False:
        print("Cannot save data , CSV file doesnt exist")
        return False

    result=FilesModule.WriteCsvFile(path,data)

    return result



def GetData(path:str):

    result=FilesModule.ReadCsvFile(path)

    if type(result) is bool:
        return False

    return result

