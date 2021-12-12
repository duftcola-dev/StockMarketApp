from dataclasses import dataclass
from typing import List




@dataclass
class TickersData:
    
    open:List[float]
    close:List[float]
    high:List[float]
    low:List[float]
    date:List[str]
    content:List[dict]
    symbol:str=""
    limit:int=0
    count:int=0
    total:int=0
    offset:int=0



@dataclass
class TickersList:

    tickers: List[dict]


class ApiResponse:

    def __init__(self) -> None:
        pass

    def CreateTickersList(self,items:list):
        
        tickers=TickersList(items)
        return tickers

    def CreateTickersData(self,open,close,high,low,date,content,symbol,limit,count,total,offset):

        data=TickersData(
            open,
            close,
            high,
            low,
            date,
            content,
            symbol,
            limit,
            count,
            total,
            offset
        )

        return data