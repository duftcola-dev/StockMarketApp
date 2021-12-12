from .mapping.DirectoryTreeGenerator_lite import TreeExplorer


class FileExplorer():

    def __init__(self) -> None:
        
        self.__file_explorer=TreeExplorer()


    def MapFiles(self,path="",ignore_this_files=[]):
        """
        Description : 
            Fetches files recursively starting from the  passed directory.

        args:
            path:str --> file path.

            ignore_this_files:list --> list with filenames or direcotry names to be ignored be the fetching process.
        """

        self.__file_explorer.ExploreDirectories(path,mode="absolute",ignore=ignore_this_files)


    def GetFilePath(self,file_name):

        """Description : fetches file by name and returns full file path.
        **When providing file name dont forget to include the file type ,example :
        
        file_name = 'logs.txt'
        """
        files_registry=self.__file_explorer.GetFilesDict()
        file_path=files_registry.get(file_name)
        if file_path == None:
            raise Exception("File explorer error : file not found")

        return file_path