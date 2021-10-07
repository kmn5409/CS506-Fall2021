from cs506 import matrix

def test_get_determinant():
    assert matrix.get_determinant(get_determinant([[1,2], [3,4]])) == -2
    assert matrix.get_determinant([ [10,11,12,13], [3,4,4,5],[4,5,7,3],[4,5,6,8] ]) == 43
