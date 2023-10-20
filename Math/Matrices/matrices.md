A matrix is a collection of numbers arranged into rows and columns. It is a way to organize and manipulate sets of numbers which can represent a multitude of things such as systems of equations, transformations, and much more. Each number in a matrix is referred to as an element. The position of a element is defined by two indices - the row number and the column number.

### Different Types of Matrices

1. **Row Matrix**: A matrix with a single row and multiple columns.
2. **Column Matrix**: A matrix with a single column and multiple rows.
3. **Square Matrix**: A matrix with the same number of rows and columns.
4. **Diagonal Matrix**: A square matrix where all elements outside the main diagonal are zero.
```
5 & 0 & 0 \\ 
0 & 3 & 0 \\ 
0 & 0 & 2 \\ 
\end{pmatrix} \]
```
1. **Identity Matrix**: A special diagonal matrix where all elements on the main diagonal are ones.
```
1 & 0 & 0 \\ 
0 & 1 & 0 \\ 
0 & 0 & 1 \\ 
\end{pmatrix} \]
```
1. **Zero Matrix**: A matrix where all elements are zero.
```
0 & 0 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 0 \\ 
\end{pmatrix} \]
```

### Basic Operations

**Addition and Subtraction**

Matrices can be added as subtracted element-wise if they have the same dimensions. This means, to add or subtract two matrices, they must have the same number of rows and the same number of columns. Each element in the resulting matrix is the sum or difference of the corresponding elements in the given matrices.
Example:

$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} , B = \begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$
$A + B = \begin{pmatrix} 5 & 5 \\ 5 & 5 \end{pmatrix}$
$A - B = \begin{pmatrix} -3 & -1 \\ 1 & 3 \end{pmatrix}$

**Matrix Multiplication**

Multiplication of matrices is a bit more complex. It's not performed element-wise, but rather, the product of two matrices is obtained by multiplying each row of the first matrix by each column of the second matrix. The number of columns in the first matrix must equal the number of rows in the second matrix to perform the multiplication.
Example:

$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} , B = \begin{pmatrix} 4 & 3 \\ 2 & 1 \end{pmatrix}$
$AB = \begin{pmatrix} 8 & 5 \\ 20 & 15 \end{pmatrix}$

#math 