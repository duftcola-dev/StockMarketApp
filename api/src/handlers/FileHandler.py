from .file_handlers.ConfigFile import ConfigFile


class FileHandler():

    def __init__(self,configuration_path,logs=None) -> None:
        
        self.__configuration=ConfigFile(configuration_path,logs=logs)
        self.__configuration.OpenConfigurationFile()



    def GetConfiguration(self)->dict:

        return self.__configuration.GetConfiguration()