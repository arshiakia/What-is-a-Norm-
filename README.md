# What-is-a-Norm-
A norm is a function that measures the size or length of a vector. It gives a sense of how "long" or "large" the vector is in space.

---

1. Calculating the p-Norm
A general way to measure vector length by raising each element to a power "p", summing them up, and taking the p-th root. Different values of "p" give you different styles of measuring distance.

2. L₀ Norm
Not a real norm mathematically, but useful in practice. It simply counts how many non-zero elements are in the vector — often used in sparse data or feature selection.

3. L₁ Norm
Also called the Manhattan norm. It adds up the absolute values of all the vector's elements — like walking in a grid city, moving only along blocks.

4. Euclidean Norm (L₂ Norm)
The most common norm — gives the actual geometric length of a vector, like using a ruler from the origin to the point.

5. Squared Euclidean Norm
Same as the L₂ norm, but squared — no square root. It's used when you care about magnitude but want to avoid the computational cost of a root.

6. Maximum Norm (Infinity Norm)
Just grabs the biggest absolute value in the vector. Useful when the largest component dominates or matters most.

7. Matrix Norm: Frobenius Form
Like the Euclidean norm, but for matrices. It measures the "size" of a matrix by treating all elements as if they were part of one giant vector.

8. Describing the Dot Product Using Norms
The dot product relates to norms and angles — it tells you how much two vectors align. If they point the same way, it's big. If they're perpendicular, it's zero.
