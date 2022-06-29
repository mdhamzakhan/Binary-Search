def naive_search(li,target):
    
    for i in range(len(li)):
        if li[i] == target:
            return i
        
    return -1

def binary_search(li,target,low=None,high=None):
    
    if low == None:
        low = 0
    if high == None:
        high = len(li)-1
    if high < low:
        return -1
    
    midpoint = (low+high)/2
    a = int(midpoint)
    if li[a] == target:
        return  a
    elif target <li[a]:
        return binary_search(li, target,low,a-1)
    else:
        return binary_search(li, target,a,high)  

if __name__=='__main__':
    li = [1,3,5,6,10,12,15]
    target = 10 
    print(naive_search(li, target))
    print(binary_search(li, target))
