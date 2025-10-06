← [[maths|Back to Math Dashboard]]
# Discrete Maths

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
# Discrete Mathematics for AI Curriculum

## [[Set Theory, Functions & Relations]]

### Concepts

- [ ] Sets, subsets, unions, intersections
- [ ] Cartesian products
- [ ] Functions, domains, codomains
- [ ] Relations, equivalence relations

### AI Applications

- [ ] Word embeddings (word2vec uses relations)
- [ ] Similarity metrics in ML (based on set operations)

### Project: **Word Similarity Visualizer**

- [ ] Use Gensim to load pre-trained word2vec
- [ ] Create a function to find common similar words using set operations
- [ ] Display results using matplotlib

---

## [[Logic, Propositions & Proof Techniques]]

### Concepts

- [ ] Propositions, truth tables
- [ ] Logical connectives (AND, OR, NOT, IMPLIES)
- [ ] Predicate logic, quantifiers
- [ ] Proofs: direct, contradiction, contrapositive

### AI Applications

- [ ] Symbolic AI, expert systems
- [ ] Rule-based reasoning (e.g. Prolog)
- [ ] Explainable AI (XAI)

### Project: **Mini Inference Engine**

- [ ] Build a basic rule engine in Python using propositional logic
- [ ] Input: rules and facts
- [ ] Output: inferred new facts


---

## [[Combinatorics & Counting]]

### Concepts

- [ ] Permutations & combinations
- [ ] Product rule, sum rule
- [ ] Binomial coefficients
- [ ] Pigeonhole principle

### AI Applications

- [ ] Neural Architecture Search (NAS)
- [ ] Hyperparameter tuning
- [ ] Generative models sampling (like GANs)

### Project: **Model Combo Generator**

- [ ] Generate all combinations of model hyperparameters
- [ ] Count total search space size
- [ ] Select random configs to try with dummy classifier



---

## [[Graph Theory Basics]]

### Concepts

- [ ] Graphs: vertices, edges, degree
- [ ] Directed vs undirected graphs
- [ ] Trees, cycles, connectivity
- [ ] Graph traversal algorithms

### AI Applications

- [ ] Knowledge graphs
- [ ] Social network analysis
- [ ] Graph Neural Networks (GNNs)

### Project: **AI Concept Map Explorer**

- [ ] Use networkx to build and visualize a graph of AI concepts
- [ ] Show how topics interlink (e.g. supervised → linear models → SVM)
- [ ] Implement basic graph algorithms

### Video Resources

- [ ] WilliamFiset - Graph Theory Playlist
- [ ] Khan Academy - Introduction to Graphs
- [ ] MIT OpenCourseWare - Graph Theory

### Problem-Solving Resources

- [ ] LeetCode - Graph Problems
- [ ] Brilliant.org - Graph Theory practice
- [ ] HackerRank - Graph Theory challenges

---

## [[Finite Automata & State Machines]]

### Concepts

- [ ] Deterministic Finite Automata (DFA)
- [ ] Non-deterministic Finite Automata (NFA)
- [ ] Transition tables, states
- [ ] Regular expressions and finite automata

### AI Applications

- [ ] Sequence models (e.g., RNNs)
- [ ] NLP tokenization & regex engines
- [ ] Event-driven agents

### Project: **Regex Pattern Validator using DFA**

- [ ] Create a DFA that validates basic regex-like patterns
- [ ] Simulate transitions in Python
- [ ] Visualize the automaton

### Video Resources

- [ ] Neso Academy - Automata Theory
- [ ] Easy Theory - Finite Automata Explained
- [ ] MIT OpenCourseWare - Computation Theory

### Problem-Solving Resources

- [ ] JFLAP Software for building DFA
- [ ] Brilliant.org - Finite Automata practice
- [ ] Theory of Computation textbook exercises

---