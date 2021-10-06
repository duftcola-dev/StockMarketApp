import csv
import os
import sys
import json
import dataclasses


def CheckFile(path:str)->bool:

    return os.path.isfile(path)




def CheckDir(path:str)->bool:

    return os.path.isdir(path)




def CreateDir(folder_path:str):

    if type(folder_path) is not str:
        return False

    try:
        os.mkdir(folder_path)
        return True
    
    except NotImplementedError:

        print(f"Cannot create directory : {folder_path}")
        return False

    except Exception as Err:

        print(f"unknown exception {Err} ")
        return False




def CreateFile(folder_path:str,file_name:str)->str:

    if type(folder_path) is not str or type(file_name) is not str:
        return False

    if os.path.isdir(folder_path)==False:
        return False

    try:

        if file_name[0] != "/" or file_name[0] != "\\":

            if sys.platform != "linux":

                file_name="\\"+file_name
            else:
                 file_name="/"+file_name
 
        path=folder_path+file_name    
        file=open(path,"w")
        file.write("")
        file.close()
        return path

    except Exception as ERR:

        print(f"cannot create file {ERR}")
        return False




def WriteCsvFile(file_path:str,csv_list:list)->bool:

    if type(csv_list) is not list:
        return False

    if len(csv_list) ==0:
        return False

    file=None
    if os.path.isfile(file_path) == False:

        print("Csv file was not created")
        return False

    file=open(file_path,"w")

    csv_writer=csv.writer(file,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)  
    
    for row in csv_list:

        csv_writer.writerow(row)

    file.close()
    
    return True




def WriteJsonFile(path:str,data:object)->bool:

    if dataclasses.is_dataclass(data)==False :
        print("data parameter must be a ApiResponse dataclass object ")
        return False

    try:
        json_content={
            "data":data.data,
            "open":data.open,
            "close":data.close,
            "high":data.high,
            "low":data.low,
            "date":data.date,
            "csv_format":data.csv_format,
            "symbol":data.symbol,
            "exchange":data.exchange,
            "factor":data.factor,
            "limit":data.limit,
            "count":data.count,
            "total":data.total,
            "offset":data.offset           
        }
        
        json_content=json.dumps(json_content,indent=4)
        file=open(path,"w")
        file.write(json_content)
        file.close
    
    except FileNotFoundError:

        print("File not found ")
        return False

    except Exception:

        print("unknown error")
        return False

    return True



def ReadCsvFile(file_path:str):
        
    result=[]
    try:
        
        csv_file=open(file_path,"r")
        for line in csv_file:
            result.append(line)
        csv_file.close()

    except FileExistsError:
        
        print("file doesnt exsist")
        return False

    except FileNotFoundError:

        print("File not found")
        return False

    except Exception:

        print("unknown error")
        return False
    
    return result   
    

