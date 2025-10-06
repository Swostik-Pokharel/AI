[[Vectors, Scalars, and Dot Product|back->]] 
# Vectors
A vector can be understood as an arrow in space, which means by definition it has a direction. If a vector is an arrow in space the length of the arrow is the magnitude and the direction of the arrowhead is the direction. The direction can also be understood as the angle made by the vector with the origin (a vector might not touch origin but we can always extend to find the angle)

## Basis vectors 
Basis vectors are like the vectors that map the length of a unit for any given vector space along all possible dimensions meaning:

```
number of basis vectors = number of dimensions
```

Generally we denote basis vectors with: I hat (î) and J hat (ĵ)
![[Gemini_Generated_Image_n3opbkn3opbkn3op.png|300]]

## Vector Addition:
Adding two vectors is the geometric equivalent of starting from one vector and going to its tip then drawing the second vector from the tip of the first vector and moving to the tip of that. The vector then formed by connecting the starting point and the ending of those two is the resultant vector. Vector addition is pretty simple.
![[Gemini_Generated_Image_wpvgnswpvgnswpvg.png|500]]

## Scalar multiplication
If you multiply a vector with a scalar it is either stretched or squished in some direction. In essence you are simply just scaling the vector itself. This also brings in the idea of a span, the span refers to all the sets of points that can be reached through given pair of vectors.This means you need atleast 2 vectors to span an infinite sheet and atleast 3 vectors ro span an infinite cube of space . 
#### Linearly dependent and independent vectors

If any given vector falls in the span of another vector, the vectors are linearly dependent, and if not, they are linearly independent. It’s just a fancy way of saying that if in a pair of vectors, one vector can be obtained by scaling another vector, they are linearly dependent. So for single dimension, all the vectors that lie within the line of the initial vector are linearly dependent. For 2D, all vectors that lie in the plane made by both the basis vectors are linearly dependent, and for 3D, all vectors that lie in the space spanned by the 3 basis vectors are linearly dependent.
