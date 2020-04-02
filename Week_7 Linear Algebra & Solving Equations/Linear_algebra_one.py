import  numpy  as  np

A = np.array([[3,2],[1,2]])

print(A)

B  =  np.array([1,0])

print(B)

a  =  (np.linalg.inv(A))

sol = np.dot(a,B)

print(sol)