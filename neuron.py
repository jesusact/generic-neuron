class Neuron:
    def __init__(self, weights, bias, activation_function):
        self.weights = weights
        self.bias = bias
        self.activation_function = activation_function

    def activate(self, total):
        if self.activation_function == "relu":
            return max(0, total)
        elif self.activation_function == "linear":
            return total
        elif self.activation_function == "sigmoid":
            import math
            return 1/(1 + math.exp(-total))
        elif self.activation_function == "binary_step":
            return 1 if total >= 0 else 0
        elif self.activation_function == "tanh":
            import math
            return math.tanh(total)
        else:
            raise ValueError("Activation function not recognized")

    def run(self, inputs):
        if len(inputs) == len(self.weights):
            total = sum([i*w for i, w in zip(inputs, self.weights)]) + self.bias
            return self.activate(total)
        else:
            raise ValueError("The number of inputs does not match the number of weights")
    
    def change_bias(self, new_bias):
        self.bias = new_bias

    