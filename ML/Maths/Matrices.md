#vectors 
#notes
### Matrices
In linear algebra, a matrix can be understood as a group of vectors written side by side. Each column of a matrix is a vector. The number of rows tells you the dimension of the space those vectors live in. For example, an m × n matrix has n column vectors, each living in R^mth dimension .
### Matrix–vector multiplication / Linear transformation

Multiplying a vector with a matrix is the geometric equivalent of taking the space around that vector and replacing the basis vectors of that space with the columns of the matrix. If this is done in a way where the grid lines of the space remain parallel and evenly spaced, the operation is called a linear transformation.

**Example:**  
In 2D, multiplying by the matrix
`[2  0]`
`[0  1]`

will stretch all vectors horizontally by 2 while leaving the vertical direction unchanged.
**Important notes:**

- You can only multiply a matrix and a vector when the number of columns of the matrix matches the number of entries (rows) in the vector.
    
- When you multiply two matrices, the result is another matrix. Geometrically, this is the same as applying the two transformations one after the other.
### Linear vs Affine Transformations

- **Linear Transformation:**
    
    - The origin stays fixed.
        
    - Vectors can rotate, stretch, compress, or shear.
        
    - Grid lines remain parallel and evenly spaced.
        
    - Example: Rotate or stretch vectors without moving the origin.
        
- **Affine Transformation:**
    
    - Can include a linear transformation **plus translation** (moving the origin).
        
    - Straight lines stay straight, but the grid can shift.
        
    - Example: Shift all vectors by `[3, 2]` or rotate then move.
        

**Key idea:**

> If the start of the vector stays at the same spot, it’s linear. If the base moves, it’s affine.


