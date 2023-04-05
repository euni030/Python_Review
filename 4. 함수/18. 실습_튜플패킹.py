def Sum(*data):
    p_sum=0
    n_sum=0
    
    for i in data:
        if i>0:
            p_sum+=i
        else:
            n_sum+=i
    
    return (p_sum,n_sum)

print(Sum(1, -2, 3.6, 5, -8.2, 4))
print(Sum(4, 2.5, -2, 4))
