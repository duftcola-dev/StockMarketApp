
def FormatSymbols(params:dict,items:list):

    if type(items) is str:
        result=items

    if type(items) is list and  len(items) ==1:
        result=items[0]

    if type(items) is list and  len(items) >1:

        result=""
        length=len(items)
        for i in range(length):

            result=result+items[i]
            if i !=(length-1) : 
                result=result+","

    params.update({"symbols":result})

    return params