import  numpy  as  np

A = np.array([[3,2],[1,2]])


B  =  np.array([1,0])


sol  =  np.linalg.solve(A,B)

print(sol)