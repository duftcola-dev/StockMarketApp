from dataclasses import dataclass
from typing import List


@dataclass
class ApiResponse:
    
    data:List[dict]
    open:List[float]
    close:List[float]
    high:List[float]
    low:List[float]
    date:List[str]
    csv_format:List[List]
    content:dict
    symbol:str=""
    exchange:str=""
    factor:float=0.0
    limit:int=0
    count:int=0
    total:int=0
    offset:int=0
