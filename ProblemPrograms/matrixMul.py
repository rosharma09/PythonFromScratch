from numpy import *

m1 = matrix('1 2 ; 3 4')
m2 = matrix('1 2 3 ; 4 5 6')

m3 = m1 * m2;
print(m3)

# to print the rows and columns for the matrix

print(m3.shape)