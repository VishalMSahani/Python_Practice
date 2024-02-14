import numpy as np

a = np.array([[1, 2, 3, 45], [4, 5, 6, 6],
              [5, 6, 9, 75], [45, 56, 9, 54]])

#Reshaping Matrix
m = np.reshape(a,(4,4))
print(m)

print("\nAccessing element")
print(a[1])

#Appending in Matrix
m =  np.append(m,[[1, 2, 3, 45]],0)
print(m)
