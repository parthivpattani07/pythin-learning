def fibonacci(x):
    i=0
    sequence=[0,1]
    for _ in range(2,x):
        sequence.append(sequence[-1]+sequence[-2])
    
    return sequence
        
        



        



print(fibonacci(5))
