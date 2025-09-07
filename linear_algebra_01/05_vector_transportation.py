import numpy as np
x = np.array([25,2,5])

# Transposing a regular 1-D array has no effect...
x_t = x.T
print("x_t =", x_t)

# Zero Vectors
z = np.zeros(3)
print("z =", z)


### L^2 Norm

y = (25**2 + 2**2 + 5**2)**(1/2)
print("y =", y)

# So, if units in this 3-dimensional vector space are meters, then the vector x has a length of 25.6m
lin_alg = np.linalg.norm(x)
print("lin_alg =", lin_alg)

### L^1 Norm

l1 = np.abs(25) + np.abs(2) + np.abs(5)
print("l1 =", l1)


### Squared L^2 Norm
sl2 = (25**2 + 2**2 + 5**2)
print("sl2 =", sl2)
sl22 = np.dot(x, x)
print("sl22 =", sl22)


### Max Norm
mn = np.max([np.abs(25), np.abs(2), np.abs(5)])
print("mn =", mn)


### Orthogonal Vectors
i = np.array([1, 0])
j = np.array([0, 1])
ij = np.dot(i, j) 
print("ij =", ij)

# Matrices (Rank 2 Tensors) in NumPy
# Use array() with nested brackets:
X = np.array([[25, 2], [5, 26], [3, 7]])
print(X.shape)
print(X.size)
# Select left column of matrix X (zero-indexed)
print(X[:,0])

# Select middle row of matrix X:
print(X[1,:])

# Another slicing-by-index example:
print(X[0:2, 0:2])