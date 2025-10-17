← [[maths|Back to Math Dashboard]]
# Linear algebra

```dataviewjs
// Get all tasks from this page
const tasks = dv.current().file.tasks;
const totalTasks = tasks.length;
const completedTasks = tasks.filter(t => t.completed).length;
const percentage = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

// Create progress bar
const barLength = 100;
const filledBars = Math.round((percentage / 100) * barLength);
const emptyBars = barLength - filledBars;
const progressBar = "█".repeat(filledBars) + "░".repeat(emptyBars);

// Display progress
dv.paragraph(`## Progress: ${completedTasks}/${totalTasks} (${percentage}%)`);
dv.paragraph(`\`\`\`\n${progressBar} ${percentage}%\n\`\`\``);
```

---

# Linear Algebra for AI Curriculum

## [[Vectors, Scalars, and Dot Product]]

### Linear Algebra Topics

- [x] Understand scalars and vectors ✅ 2025-07-28
- [x] Practice vector addition and scalar multiplication ✅ 2025-07-28
- [x] Learn dot product and its geometric meaning ✅ 2025-07-28

### AI Concepts

- [x] Understand feature vectors ✅ 2025-07-28
- [x] Learn cosine similarity ✅ 2025-07-28
- [x] Explore embedding spaces (e.g., word embeddings) ✅ 2025-07-30

### Project: **Text Similarity Calculator**

- [x] Input two sentences ✅ 2025-07-28
- [x] Convert to TF-IDF vectors ✅ 2025-07-28
- [x] Compute cosine similarity with NumPy ✅ 2025-07-30
- [x] Output similarity score ✅ 2025-07-30
- [x] Return top-matching sentence from dataset ✅ 2025-07-30


---

## [[Matrix Operations & Linear Transformations]]

### Linear Algebra Topics

- [x] Learn matrix multiplication
- [x] Study matrix-vector products
- [x] Explore geometric intuition of linear transformations

### AI Concepts

- [x] Understand forward pass in neural networks
- [x] Explore linear layers / affine transformations

### Project: **Manual Neural Network Layer**

- [ ] Implement single-layer NN using matrix multiplication
- [ ] Add bias vector and ReLU activation
- [ ] Compare with `torch.nn.Linear`

---

## [[Inverses, Identity, and Solving Equations]]

### Linear Algebra Topics

- [ ] Study inverse matrices
- [ ] Understand identity matrix
- [ ] Learn to solve `Ax = b`

### AI Concepts

- [ ] Linear regression via normal equation
- [ ] Understand overfitting and regularization

### Project: **Linear Regression From Scratch**

- [ ] Generate synthetic data
- [ ] Solve using normal equation `(X^T X)^-1 X^T y`
- [ ] Compare with `sklearn.linear_model.LinearRegression`



---

## [[Eigenvalues, Eigenvectors, and PCA]]

### Linear Algebra Topics

- [ ] Learn eigenvectors and eigenvalues
- [ ] Understand diagonalization
- [ ] Study Principal Component Analysis (PCA)

### AI Concepts

- [ ] Dimensionality reduction
- [ ] Noise filtering

### Project: **PCA Visualizer**

- [ ] Use sklearn's PCA
- [ ] Apply on Iris or MNIST
- [ ] Reduce to 2D and plot

---

## [[SVD, Rank, and Recommender Systems]]

### Linear Algebra Topics

- [ ] Understand matrix rank
- [ ] Learn null space
- [ ] Study Singular Value Decomposition (SVD)

### AI Concepts

- [ ] Learn recommender system basics
- [ ] Understand Latent Semantic Analysis

### Project: **Movie Recommender via SVD**

- [ ] Load MovieLens dataset
- [ ] Create user-movie matrix
- [ ] Apply SVD
- [ ] Recommend top similar movies


---
