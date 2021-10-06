from os import stat_result
from .dependencies.DataClasses.ApiResponse import ApiResponse





def FormatResponseData(items:dict)->object:
    
    try:
        def FormatDate(string:str):

            end=string.find("T")
            temp=""
            for char in range(0,end) :

                temp=temp+string[char]

            return temp

        
        def GetValuesList(string_dict:dict):

            temp=string_dict
            temp.pop("adj_close")
            temp.pop("adj_low")
            temp.pop("adj_open")
            temp.pop("adj_high")
            temp.pop("adj_volume")
            temp.pop("symbol")
            temp.pop("exchange")
            temp.pop("split_factor")
            temp["date"]=FormatDate(temp["date"])

            return list(temp.values())

        
        pagination=items.get("pagination")
        data=items.get("data")
    
        limit=pagination.get("limit")
        offset=pagination.get("offset")
        count=pagination.get("count")
        total=pagination.get("total")
        split_factor=data[0].get("split_factor")
        symbol=data[0].get("symbol")
        exchange=data[0].get("exchange")

        response=ApiResponse(
            [],[],[],[],[],[],
            {},
            items,
            symbol,
            exchange,
            split_factor,
            limit,
            count,
            total,
            offset,
            )

        for item in data:
        
            response.data.append(item)
            response.open.append(item.get("open"))
            response.close.append(item.get("close"))
            response.high.append(item.get("high"))
            response.low.append(item.get("low"))
            response.date.append(item.get("date"))
            count+=1


        response.date=[FormatDate(string) for string in response.date]

        csv_index=["open","high","low","close","volume","date"]
        response.csv_format=[GetValuesList(item) for item in data]
        response.csv_format.insert(0,csv_index)

        
        return response
        
    except Exception :

        print("unknown error")
        return False

