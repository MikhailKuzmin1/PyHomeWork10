class Matrix:
    def __init__(self, list_matr):
        self.list_matr = list_matr

    def transp_matrix(self):
        zip_matrix = zip(*self.list_matr)
        return [list(i) for i in zip_matrix]
    

one = Matrix([[1,2,3],[4,5,6]])
print(one.transp_matrix())