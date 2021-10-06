
from .TreeGenerator_lite.DirectoryTreeGenerator_lite import TreeExplorer
import json


class ConfigurationLoader():

    def __init__(self,path) -> None:

        self.__path=path
        self.__explorer=TreeExplorer()
        self.configuration={}



    def GetConfiguration(self)->dict:

        try:
            file_path=self.__GetConfigurationFile(self.__path)
            file=open(file_path,"r")
            content=json.load(file)
            self.configuration=content
            file.close()

            return self.configuration

        except:

            return False




    def __GetConfigurationFile(self,path)->str:
        
        try:
            self.__explorer.ExploreDirectories(path=path)
            file_path=self.__explorer.Files_Registry.get("config.json")

            return file_path

        except Exception:

            return False




    def Test(self):

        return 1