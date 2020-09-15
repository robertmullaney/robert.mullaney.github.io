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
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(specialSort(lst))
lst2= ['this', 'is', 'special', 'right', 'sort']
print(specialSort(lst2))