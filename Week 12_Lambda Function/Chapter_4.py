cuber =[2,4,5,12,18]

def solver(n):
    return n*n*n

print(list(map(solver,cuber)))

# We use a map function here
# map takes two arguments 1st is the function,
# second is iterator
# (func,iter)
# list is also built-in of python