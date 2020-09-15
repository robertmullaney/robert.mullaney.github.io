def specialSort(toSort):
    count=0
    even=[]
    odd=[]
    for item in toSort:
        if count%2==0: 
            even.append(item)
        else:
            odd.append(item)
        count +=1
    return even+odd