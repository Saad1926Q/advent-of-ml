"""
Write a Python function that simulates a single neuron with sigmoid activation, 
and implements backpropagation to update the neuron's weights and bias. 
The function should take a list of feature vectors, associated true binary labels, initial weights, initial bias, a learning rate, 
and the number of epochs. The function should update the weights and bias using gradient descent based on the MSE loss, 
and return the updated weights, bias, and a list of MSE values for each epoch, each rounded to four decimal places.

Example:
Input:
features = [[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]], labels = [1, 0, 0], initial_weights = [0.1, -0.2], initial_bias = 0.0, learning_rate = 0.1, epochs = 2
Output:
updated_weights = [0.1036, -0.1425], updated_bias = -0.0167, mse_values = [0.3033, 0.2942]

"""
import numpy as np


def sigmoid(X):
    exp=np.exp(-X)
    return 1/(1+exp)



def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    mse_values=[]
    n=features.shape[0]
    for epoch in range(epochs):
        logits=np.matmul(features,initial_weights)+initial_bias
        y_hat=sigmoid(logits)
        grad_w=(2/n)*(features.T)@((y_hat-labels)*(y_hat)*(1-y_hat)) # (m,n)x(n,)=> (m,) where m is no of features and n is no of training examples
        grad_b=2*(y_hat-labels)*(y_hat)*(1-y_hat)  # shape =>(n,)
        grad_b=grad_b.mean() #scalar

        mse_values.append(np.round(np.mean((labels-y_hat)**2),4).item())

        
        # ∂L/∂W_i = (2/n) * Σ [(y_hat - y) * y_hat * (1 - y_hat) * x_i]
        # ∂L/∂b   = (2/n) * Σ [(y_hat - y) * y_hat * (1 - y_hat)]


        initial_weights=initial_weights-learning_rate*grad_w
        initial_bias=initial_bias-learning_rate*grad_b

        
    final_bias=round(initial_bias,4)
    final_weights=np.round(initial_weights,4)
        


    return final_weights,final_bias,mse_values

train_neuron(features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]), labels = np.array([1, 0, 0]), initial_weights = np.array([0.1, -0.2]), initial_bias = 0.0, learning_rate = 0.1, epochs = 2)