import time

start_time = time.time()

def fiboIter(steps):
    A = 0
    B = 1
    steps -= 2
    print(f"{A}")
    print(f"{B}")
    while steps > 0:
        A = A + B
        print(f"{A}")
        steps -= 1
        if (steps > 0):
            B = A + B
            print(f"{B}")
        steps -= 1

# def fiboRecu(steps, A, B):
#     print(f"{A}")
#    C = A + B
#     steps -= 1
#     if (steps > 0):
#         D = B + C 
#         print(f"{B}")
#         steps -= 1
#     if (steps > 0):
#         fiboRecu(steps, C, D)
#     return();

def fiboRecu2(steps, A, B):
    print(f"{A}")
    if (steps > 0):
        fiboRecu2(steps-1, B, A+B)
    return();

def fiboRecuSlow(n):
    print(n)
    if (n == 1):
        return (0)
    elif (n == 2):
        return (1)
    return(fiboRecuSlow(n-1)+fiboRecuSlow(n-2))

# ~0.25 - 0.60sec
#fiboIter(1900)

# ~0.19 - 0.40sec
#fiboRecu(1900, 0, 1)

# ~0.004 - 0.020sec
# fiboRecu2(500, 0, 1)

# Lmao.
#fiboRecuSlow(50)

print(f"\nTime taken: {time.time() - start_time} seconds")