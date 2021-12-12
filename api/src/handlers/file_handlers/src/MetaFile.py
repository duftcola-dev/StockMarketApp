import abc


class MetaFile(abc.ABC):


    def __init__(self) -> None:
        pass
        
    @abc.abstractstaticmethod
    def GetInstance():
        raise NotImplementedError    

    @abc.abstractmethod
    def _FileExist(self)->bool:
        
        raise NotImplementedError

    @abc.abstractmethod
    def OpenFile(self,mode)->bool:
        """Opens the file with the specified mode r,w,a and keeps the buffer open
        until the method CloseFile is executed or fails

        Args:
            mode ([str]): specifies how the file should be opened r,w,a

        Raises:
            NotImplementedError: Method must be implemented

        Returns:
            bool: True if the file is reached or successfully open
        """
        raise NotImplementedError

    @abc.abstractmethod
    def CloseFile(self)->bool:
        
        raise NotImplementedError

    @abc.abstractmethod
    def ReadFile(self)->bool:
        
        raise NotImplementedError

    @abc.abstractmethod
    def WriteFile(self,data)->bool:
        
        raise NotImplementedError
    
    @abc.abstractmethod
    def LogMessage(self,message,message_type=""):
        
        raise NotImplementedError

