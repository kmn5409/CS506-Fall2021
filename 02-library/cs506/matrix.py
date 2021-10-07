def get_matrix_minor(M,i,j):
    return [row[:j] + row[j+1:] for row in (M[:i]+M[i+1:])]

def get_determinant(M):
    if len(M) == 2 and len(M[0]) == 2:
        val = M[0][0] * M[1][1] - M[1][0] * M[0][1]
        return val

    det = 0
    for c in range(len(M)):
        det += ((-1)**c)*M[0][c]*get_determinant(get_matrix_minor(M,0,c))
    return det

#print(get_determinant([[1,2], [3,4]]))
#print(get_determinant([ [1,2,4,5], [3,4,4,5],[4,5,7,3],[4,5,6,8] ]))
#print(get_determinant([ [1,2,4,5,5], [3,4,4,5,4],[4,5,7,3,2],[4,5,6,8,9] ]))
print(get_determinant([ [10,11,12,13], [3,4,4,5],[4,5,7,3],[4,5,6,8] ]))

