

class ResponseAdapter:

    def __init__(self) -> None:
        pass

    def GetTickerList(self,create_dataclass,http_response:dict):


        if type(http_response) is not dict:
            raise Exception("Param 2 must be http response format as dict")

        
        data=http_response.get("data")
        items_collection=[]
    
        for items in data:
            item={"name":"","symbol":"","stock_exchange":""}
            item["name"]=items.get("name")
            item["symbol"]=items.get("symbol")
            item["stock_exchange"]=items.get("stock_exchange").get("name")
            items_collection.append(item)
        
        
        return create_dataclass(items_collection)


    def GetTickersData(self,create_dataclass,http_response:dict):

        pagination=http_response.get("pagination")
        data=http_response.get("data")
        
        limit=pagination.get("limit")
        count=pagination.get("count")
        total=pagination.get("total")
        offset=pagination.get("offset")

        open=[]
        high=[]
        low=[]
        close=[]
        date=[]
        content=[]
        symbol=""
        
        for item in data:

            content.append(item)
            open.append(item.get("open"))
            high.append(item.get("high"))
            low.append(item.get("low"))
            close.append(item.get("close"))
            date.append(item.get("date"))
            symbol=item.get("symbol")
    
        return create_dataclass(open,close,high,low,date,content,symbol,limit,count,total,offset)
        