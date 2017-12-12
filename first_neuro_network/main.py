# python notebook for Make Your Own Neural Network
# (c) Tariq Rashid, 2016
# license is GPLv2
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
import random


# neural network class definition
class neuralNetwork:
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate
        self.lr = learningrate

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        # targets = numpy.array(targets_list).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        print('Ошибки на выходе: ', output_errors)
        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

# number of input, hidden and output nodes
input_nodes = 2
hidden_nodes = 6
output_nodes = 1

# learning rate is 0.3
learning_rate = 0.01

data = []

for i in range(100):
    a_in = random.random()
    b_in = random.random()
    # c_in = random.random()
    data.append([a_in, b_in, a_in + b_in])
    # print(data[i])

# create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# test query (doesn't mean anything useful yet)
# print(n.query([1.0, 0.5, -1.5]))
index = 0
print('Один элемент данных: ', data[0])
list_output = n.query([data[index][0], data[index][1]])
print('Расчетные выходные данные', list_output)
list_correct_output = numpy.array([data[index][2]], ndmin=2).T
print('Эталонные выходные данные', list_correct_output)
print(list_correct_output[0, 0])

print(abs(list_output[0, 0] - list_correct_output[0, 0]))

while abs(list_output[0, 0] - list_correct_output[0, 0]) > 0.1:
    print(abs(list_output[0, 0] - list_correct_output[0, 0]))
    print('Расчетные выходные данные', list_output)
    print('Эталонные выходные данные', list_correct_output)
    index = random.randint(0, 99)
    n.train([data[index][0], data[index][1]], [data[index][2]])

