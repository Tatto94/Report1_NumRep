class MyMatrix:

    matrix= [[]]

#constructors

    def __init__(self, m, n):
        self.rows   = m  #number of rows
        self.columns= n #number of columns
        self.matrix= [[0 for j in range(n)] for i in range(m)]

    def set_matrix(self, data):
         if self.rows==len(data) and self.columns==len(data[0]):
            self.matrix=data
         else:
             print("the dimensions of the data do not match the dimensions of the matrix") 

#primitive access methods

    def set_element(self, i, j, element):
        self.matrix[i][j]=element
    

    def get_element(self, i, j):
        return self.matrix[i][j]

    def get_columns(self):
        return self.columns

    def get_rows(self):
        return self.rows

    def check_dimensions(self, matrix):
        if self.rows==matrix.get_rows() and self.columns== matrix.get_columns():
           return True
 
        else:
           return false   

 #operation methods

    def __add__(self, matrix):
        return self.add(matrix)

    def add(self, matrix):
        if self.check_dimensions(matrix):
           result= Matrix(self.rows, self.columns)
           for i in range(self.rows):
               for j in range(self.columns):
                   result.set_element(i, j, self.get_element(i, j)+ matrix.get_element(i, j))
           return result
        else:
             print("Matrices have different dimensions")
             return 0

    def __mult__(self, operand):
        return self.mult(matrix)

    def mult(self, operand):
         if self.columns== operand.get_rows():
            result= Matrix(self.rows, operand.get_columns())
            for i in range(self.rows):
                for j in range(operand.get_columns()):
                    element= 0
                    for k in range(self.columns):
                        element += self.get_element(i, k)*operand.get_element(k,j)
                        result.set_element(i, j,element)
            return result 
         else: 
            print("Error: matrices are of wrong dimensions for multiplication")
            return 0


 #print method 
    def __str__(self):
        for i in range(self.rows):
            print( str(self.matrix[i]))
        return " "
                

           
       
   
