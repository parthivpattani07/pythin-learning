def fibonacci(x):
    i=0
    sequence=[0,1]
    for _ in range(2,x):
        sequence.append(sequence[-1]+sequence[-2])
    
    if x==0 :
        return []
    if x==1:
        return [0]

    return sequence
        
        
"""
input:
print(fibonacci(7))
print(fibonacci(1))
print(fibonacci(0))
output: 
[ 0 1 1 2 3 5 8 ]
[0]
[]

"""
