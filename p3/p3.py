# https://www.youtube.com/watch?v=tMrbN67U9d4
# The Dot Product

inputs = [1, 2, 3, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]

biases = [2, 3, 0.5]  # Optimiser eventually tunes the biases.

layer_outputs = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)

# Biases can convert output to positive e.g

some_value = -0.5
weight = 0.7
bias = 0.7

print(some_value * weight)
print(some_value + bias)

# Shapes must be homologous. Tensors are structure which can be represented as an Array.

# (4,) - Array, Vector
[1, 5, 6, 2]

# (2, 4) - 2d Array, Matrix
[
    [1, 5, 6, 2],
    [3, 2, 1, 3]
]

# (3, 2, 4) - 3d Array
[
    [
        [1, 5, 6, 2],
        [3, 2, 1, 3]
    ],
    [
        [3, 2, 4, 5],
        [2, 3, 4, 7]
    ],
    [
        [1, 5, 4, 2],
        [7, 3, 1, 5]
    ]
]
