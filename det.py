"""
Simple Python Determiant Calculator
Created by Paul Bitutsky

This program calculates the determinant of an n*n matrix using 
cofactor expansion across any row or down any column.
Example usage:
>>> A = [[1, 3, 5], [2, 1, 1], [3, 4, 2]]
>>> det(A)
20
>>> medA = [[6, 0, 0, 5], [1, 7, 2, -5], [2, 0, 0, 0], [8, 3, 1, 8]]
>>> det(medA)
10
>>> hardA = [[4, 0, -7, 3, -5],
...          [0, 0, 2, 0, 0],
...          [7, 3, -6, 4, -8],
...          [5, 0, 5, 2, -3],
...          [0, 0, 9, -1, 2]]
>>> det(hardA, 2, False)
6
"""

def det(A, cof=0, row=True):
	#assert A is square
	if len(A) == 0:
		return 0
	elif len(A) == 1:
		return A[0][0]
	elif len(A) == 2:
		a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
		# print((a*d) - (b*c))
		return (a*d) - (b*c)
	else:
		determinant = 0
		n = len(A)
		if (row):
			for i in range(0, n):
				alt_sign = pow(-1, i+cof)
				# print(str(alt_sign*A[cof][i]) + " * " + str(splice(A, cof, i)))
				determinant += alt_sign*(A[cof][i]*det(splice(A, cof, i)))
		if (not row): #if col
			for j in range(0, n):
				alt_sign = pow(-1, j+cof)
				# print(str(alt_sign*A[j][cof]) + " * " + str(splice(A, j, cof)))
				determinant += alt_sign*(A[j][cof]*det(splice(A, j, cof)))
		return determinant

#even better than slice!
def splice(A, r, c):
	B = []
	for i in range(0, len(A)):
		row = []
		if (i != r):
			for j in range(0, len(A)):
				if (j != c):
					row.append(A[i][j])
			B.append(row)
	return B



