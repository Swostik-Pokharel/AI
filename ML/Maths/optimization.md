← [[maths|Back to Math Dashboard]]
optimization

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
# Optimization Theory for AI Curriculum

## [[Introduction to Optimization & Cost Functions]]

### Optimization Concepts

- [ ] What is optimization?
- [ ] Objective (cost/loss) functions
- [ ] Local vs. global minima
- [ ] Convexity and convex functions

### AI/ML Concepts

- [ ] Understanding loss functions in linear regression
- [ ] Role of optimization in training models
- [ ] Cost function landscapes

### Project: **Linear Regression from Scratch**

- [ ] Implement linear regression using gradient descent
- [ ] Visualize cost function convergence
- [ ] Compare with analytical solution



---

## [[Gradient Descent and Its Variants]]

### Optimization Concepts

- [ ] Gradient descent (GD) algorithm
- [ ] Stochastic Gradient Descent (SGD)
- [ ] Mini-batch gradient descent
- [ ] Learning rate and convergence issues

### AI/ML Concepts

- [ ] Training neural networks with backpropagation
- [ ] Loss landscapes visualization
- [ ] Batch size effects on training

### Project: **Neural Network from Scratch**

- [ ] Train a simple neural network (2 layers) on MNIST using NumPy
- [ ] Implement different GD variants
- [ ] Compare convergence behavior


---

## [[Advanced Optimization Techniques]]

### Optimization Concepts

- [ ] Momentum optimization
- [ ] Nesterov accelerated gradient
- [ ] RMSProp algorithm
- [ ] Adam optimizer and variants

### AI/ML Concepts

- [ ] Impact of optimizer choice in deep learning
- [ ] Convergence speed vs. accuracy trade-offs
- [ ] Adaptive learning rates

### Project: **Optimizer Comparison**

- [ ] Compare training performance of different optimizers on CIFAR-10
- [ ] Use TensorFlow/PyTorch for implementation
- [ ] Visualize training curves and final accuracy



---

## [[Constrained Optimization]]

### Optimization Concepts

- [ ] Lagrange multipliers method
- [ ] Equality and inequality constraints
- [ ] KKT (Karush-Kuhn-Tucker) conditions
- [ ] Dual problem formulation

### AI/ML Concepts

- [ ] Resource allocation in ML systems
- [ ] Hyperparameter tuning with constraints
- [ ] Regularization as constrained optimization (L1/L2)

### Project: **Constrained Hyperparameter Tuning**

- [ ] Hyperparameter tuning on Support Vector Machine
- [ ] Implement grid search with constraints
- [ ] Compare constrained vs. unconstrained optimization



---

## [[Real-world Applications & Advanced Topics]]

### Optimization Concepts

- [ ] Review of all optimization techniques
- [ ] Non-convex optimization challenges
- [ ] Simulated annealing algorithm
- [ ] Genetic algorithms introduction

### AI/ML Concepts

- [ ] Optimization in reinforcement learning
- [ ] GAN training optimization
- [ ] Transformer model optimization

### Capstone Project: **Advanced AI System**

- [ ] Implement a GAN to generate handwritten digits
- [ ] OR train a simple DQN reinforcement learning agent
- [ ] Apply advanced optimization techniques



---
