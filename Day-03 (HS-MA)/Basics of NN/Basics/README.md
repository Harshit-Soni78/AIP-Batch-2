# **Neural Networks**

## **1. Introduction to Neural Networks**

Artificial Neural Networks (ANNs) are computational models inspired by the human brain. They consist of layers of interconnected neurons that process data and learn patterns.

### **Key Components of a Neural Network:**

- **Neuron (Perceptron):** Basic unit of computation.
- **Weights & Biases:** Parameters that adjust during learning.
- **Activation Function:** Determines neuron output.
- **Layers:**
  - **Input Layer**: Takes raw data as input.
  - **Hidden Layers**: Process and learn patterns.
  - **Output Layer**: Provides the final result.

---

## **2. Structure and Function of a Single Neuron**

A single-layer perceptron computes a weighted sum of inputs and applies an activation function.

### **Mathematical Model:**

$$ y = f\left(\sum(w_i \cdot x_i) + b\right) $$
where:

- $$ x_i = Inputs  $$
- $$ w_i = Weights $$  
- $$ b = Bias  $$
- $$ f = Activation Function  

---

## **3. Hands-on: Implementing a Perceptron from Scratch**

```python
import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=10):
        self.weights = np.random.randn(input_size + 1)  # Including bias
        self.lr = lr
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def train(self, X, y):
        X = np.c_[X, np.ones(X.shape[0])]  # Adding bias term
        for _ in range(self.epochs):
            for i in range(X.shape[0]):
                y_pred = self.activation(np.dot(self.weights, X[i]))
                error = y[i] - y_pred
                self.weights += self.lr * error * X[i]

    def predict(self, X):
        X = np.c_[X, np.ones(X.shape[0])]
        return np.array([self.activation(np.dot(self.weights, x)) for x in X])

# Example: OR Logic Gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1])

model = Perceptron(input_size=2)
model.train(X, y)
print("Predictions:", model.predict(X))
```

**Explanation:** A perceptron is trained on OR gate logic using simple weight updates.

---

## **4. Multi-Layer Perceptron (MLP)**

MLPs consist of multiple layers with nonlinear activation functions to learn complex patterns.

### **Common Activation Functions:**

- **Sigmoid:** $$ f(x) = \frac{1}{1+e^{-x}} $$  
- **ReLU:** $$ f(x) = \max(0, x) $$  
- **Softmax:** Typically used in multi-class classification, expressed as $$ f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}} $$

### **Implementing a Multi-Layer Perceptron using TensorFlow**

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Sample Data: XOR Gate
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Building the MLP Model
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)
print("Predictions:", model.predict(X).round())
```

**Explanation:** An MLP learns the XOR function using a hidden layer with ReLU activation.

---

## **5. Differences Between ANN and Human Brain**

| Feature          | Artificial Neural Network | Human Brain               |
| ---------------- | ------------------------- | ------------------------- |
| Learning         | Supervised, Reinforcement | Unsupervised, Adaptive    |
| Processing Speed | Fast for computation      | Slower but more efficient |
| Parallelism      | Limited                   | Highly parallel           |
| Generalization   | Requires large data       | Learns from few examples  |

---

## **6. Applications of Neural Networks**

- Image Recognition (e.g., Face Detection)
- Speech Recognition (e.g., Google Assistant, Siri)
- Fraud Detection (e.g., Credit Card Fraud)
- Autonomous Vehicles (e.g., Self-driving cars)

---

## **7. Discussion Questions**

1. Why do neural networks require activation functions?
2. What challenges exist in training deep neural networks?
3. How does backpropagation optimize neural network weights?

## Author

**Harshit Soni**  
GitHub: [Harshit-Soni78](https://github.com/Harshit-Soni78)

---
Made with ❤️ by Harshit Soni
