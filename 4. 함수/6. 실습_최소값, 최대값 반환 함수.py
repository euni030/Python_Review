def GetMinMax(data):
    min_v=data[0]
    max_v=-data[0]
    
    for i in range(1,len(data)):
        if data[i]<min_v:
            min_v=data[i]
        if data[i]>max_v:
            max_v=data[i]
    
    return (min_v,max_v)
    

min_value,max_value=GetMinMax([5,6,3,9,1,4])
print(f"최소값:{min_value}")
print(f"최대값:{max_value}")
