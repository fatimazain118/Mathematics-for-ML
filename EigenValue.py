#Eigen Values and Eigen Vectors
import numpy as np

A = np.mat("0 1 ; -2 -3")
print("A : \n ", A)

print("Eigen values : ", np.linalg.eigvals(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eig : ", eigenvalues)
print("First tuple of eig : \n ", eigenvectors)