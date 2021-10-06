import os
from .dependencies.TreeGenerator_lite.DirectoryTreeGenerator_lite import TreeExplorer


def ScanDir(path:str):

    files=[]
    temp=os.scandir(path)

    for element in temp:

        files.append(element.name)

    return files




def GetAppFiles(root:str)->object:

    if type(root) is not str:
        return False

    e=TreeExplorer()
    e.ExploreDirectories(root)

    return e