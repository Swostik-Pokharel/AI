← [[maths|Back to Math Dashboard]]
# Statistics and probability

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
# Probability & Statistics for AI Curriculum

## [[Basics of Probability & Descriptive Statistics]]

### Core Concepts

- [ ] Probability rules (addition, multiplication, complements)
- [ ] Sample space and events
- [ ] Descriptive statistics: mean, median, mode, variance, std deviation

### AI Concepts

- [ ] Data preprocessing
- [ ] Data visualization and exploration
- [ ] Understanding distributions in datasets

### Project: **Data Profiling & Visualization Tool**

- [ ] Load a real dataset (e.g., Titanic or Iris)
- [ ] Compute descriptive stats (mean, std, etc.)
- [ ] Plot histograms, box plots, and correlation matrix


---

## [[Conditional Probability & Bayes' Theorem]]

### Core Concepts

- [ ] Conditional probability
- [ ] Bayes' Theorem
- [ ] Independence

### AI Concepts

- [ ] Naive Bayes classifier
- [ ] Inference under uncertainty

### Project: **Spam Classifier using Naive Bayes**

- [ ] Load SMS Spam dataset
- [ ] Vectorize text into features
- [ ] Implement Naive Bayes or use sklearn
- [ ] Evaluate accuracy and visualize confusion matrix

---

## [[Distributions & Random Variables]]

### Core Concepts

- [ ] Discrete vs. continuous distributions
- [ ] Bernoulli, Binomial, Normal distributions
- [ ] Expectation and variance

### AI Concepts

- [ ] Understanding model assumptions
- [ ] Probabilistic modeling
- [ ] Loss functions derived from distributions (cross-entropy, MSE)

### Project: **Distribution Fitter & Simulator**

- [ ] Simulate random variables from common distributions
- [ ] Plot histograms and compare with theoretical PDF/PMF
- [ ] Use in modeling likelihood of real-world data


---

## [[Maximum Likelihood Estimation & Inference]]

### Core Concepts

- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Log likelihood
- [ ] Parameter estimation

### AI Concepts

- [ ] Logistic regression
- [ ] Model fitting via likelihood maximization
- [ ] Estimating parameters in probabilistic models

### Project: **Logistic Regression From Scratch**

- [ ] Simulate binary classification dataset
- [ ] Implement logistic regression using MLE
- [ ] Compare with sklearn implementation

---

## [[Hypothesis Testing & Confidence]]

### Core Concepts

- [ ] Hypothesis tests (Z-test, t-test)
- [ ] p-values and significance
- [ ] Confidence intervals
- [ ] Type I and II errors

### AI Concepts

- [ ] A/B testing
- [ ] Model evaluation
- [ ] Statistical comparison of models

### Project: **A/B Test Simulator**

- [ ] Simulate web conversion data (e.g., button A vs. B)
- [ ] Perform hypothesis test to check significance
- [ ] Visualize p-value distribution and confidence intervals
