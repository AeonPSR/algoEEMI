S = 1
N = 3
output = 0
 
while S-1 < N:
    output = output + pow((N-(S-1)), 2)
    S += 1
print(output)