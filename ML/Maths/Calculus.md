← [[maths|Back to Math Dashboard]]
# Calculus
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
# Calculus for AI Curriculum

## [[Foundations of Calculus & Functions in ML]]

### Math Focus

- [ ] Functions and limits
- [ ] Derivatives (single-variable)
- [ ] Chain rule

### AI/ML Concepts

- [ ] Activation functions (ReLU, Sigmoid, Tanh)
- [ ] Why smoothness matters
- [ ] Basics of model training

### Project: **Activation Function Visualizer**

- [ ] Plot and compare activation functions
- [ ] Visualize their derivatives
- [ ] Compare smoothness properties


---

## [[Partial Derivatives & Loss Functions]]

### Math Focus

- [ ] Multivariable functions
- [ ] Partial derivatives
- [ ] Gradient vectors

### AI/ML Concepts

- [ ] Loss surfaces
- [ ] Visualizing cost landscapes
- [ ] Gradient direction in multivariate models

### Project: **Loss Surface Visualizer**

- [ ] Implement and visualize MSE loss surface for linear regression
- [ ] Create 3D plots of cost landscapes
- [ ] Explore different parameter combinations

---

## [[Gradients & Optimization]]

### Math Focus

- [ ] Gradient vectors
- [ ] Directional derivatives
- [ ] Optimization intuition

### AI/ML Concepts

- [ ] Gradient Descent algorithm
- [ ] Local minima and saddle points
- [ ] Learning rates and convergence

### Project: **Gradient Descent Animator**

- [ ] Animate gradient descent on a cost surface
- [ ] Use matplotlib for visualization
- [ ] Compare different learning rates



---

## [[Backpropagation & Chain Rule]]

### Math Focus

- [ ] Multivariable chain rule
- [ ] Jacobians (introduction)
- [ ] Composite function derivatives

### AI/ML Concepts

- [ ] Backpropagation in neural networks
- [ ] How gradients flow through layers
- [ ] Computational graphs

### Project: **Neural Network from Scratch**

- [ ] Manually implement backprop for 2-layer neural net in NumPy
- [ ] Compare with automatic differentiation
- [ ] Visualize gradient flow

---

## [[Advanced Topics & Real AI Systems]]

### Math Focus

- [ ] Implicit differentiation (introduction)
- [ ] Optimization with constraints
- [ ] Lagrange multipliers (basics)

### AI/ML Concepts

- [ ] Regularization techniques
- [ ] Softmax and cross-entropy loss
- [ ] Vanishing and exploding gradients

### Project: **Regularized Logistic Regression**

- [ ] Implement L2-regularized logistic regression
- [ ] Compare with non-regularized version
- [ ] Visualize regularization effects


---
