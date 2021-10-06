import abc
import os
import sys
# Author Robin Viera 
# Data 07/05/2021
# Description: This class scan directories recursively creating lists and dictionaries of all 
# the diles and directories present in the target folder.


class TreeExplorer():



    def __init__(self):

        self.Files_Registry={}
        self.Dir_Registry={}
        self.Files_List=[]
        self.Dir_List=[]
        self.w_slash=""
        self.path=""
        self.new_path=""



    def ExploreDirectories(self,path:str="",mode:str="absolute")->list:
        
        self.Files_Registry={}
        self.Dir_Registry={}
        self.Files_List=[]
        self.Dir_List=[]


        if sys.platform == "linux":
            self.w_slash="/"
        else:
            self.w_slash="\\"

        current_dir=""
        if path=="" and mode=="":  
            current_dir=os.getcwd()
        elif mode=="absolute" and  path !="":
            current_dir=path
        elif mode=="relative" and path !="":
            current_dir=os.getcwd()
            current_dir=current_dir+self.w_slash+path

        if os.path.isdir(current_dir):
            self.path=current_dir
            self.__Create_Directory_Tree()
        else:
            return False
            


 
    def Get_Root_Folder_Path(self)->str:
        
        if(self.path != ""):
            return self.path
        else:
            print(" Path not defined ")
            return False




    def __Create_Directory_Tree(self):
        
        self.__Explore_Directories(self.path)
      



    def __Explore_Directories(self,root:str):

        Current_Dir_Entries=os.scandir(root)

        for entry in Current_Dir_Entries:

            self.new_path=root+self.w_slash+entry.name
            name=str(entry.name)
            path=str(entry.path)

            if entry.is_dir():

                self.Dir_Registry.update({name:path})
                self.Dir_List.append(path)
                self.__Explore_Directories(self.new_path)

            else:

                self.Files_Registry.update({name:path})
                self.Files_List.append(path)
                
         

                
    