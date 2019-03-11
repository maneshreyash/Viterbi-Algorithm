# Implement the Viterbi algorithm to compute the most likely weather sequence and probability for any given
# observation sequence.
# Example observation sequences: 331, 122313, 331123312, etc.
#
# @author: Shreyash Sanjay Mane


import sys


class Viterbi:
    # Initialise the class
    # @param:   sequence- The sequence of input observations taken form parameters
    def __init__(self, sequence):

        # Define all the states
        self.states = ['S', 'C', 'H']

        # State transition probabilities mapped with respect to the state array
        self.state_graph = [[0, 0.2, 0.8], [0, 0.6, 0.4], [0, 0.3, 0.7]]

        # Probabilities for ice-creams for each state ranging from 0 to 3 inclusive
        self.observation_probabilities = [[0, 0, 0, 0], [0, 0.5, 0.4, 0.1], [0, 0.2, 0.4, 0.4]]
        self.inp = sequence

    # Function to convert the input to an array of numbers which act as the observations
    # @return:  ice_cream_array- The array of all observations as numbers
    def preprocess(self):
        temp = str(self.inp)
        ice_cream_array = [0]
        for digit in temp:
            ice_cream_array.append(int(digit))
        return ice_cream_array

    # Calculation of probabilities and finding the most probable sequence by
    # implementing viterbi algorithm.
    def calculate(self):
        inp = self.preprocess()

        # create arrays to store the computed maximum values for each of the state probabilities
        viterbi = [[0] * (len(inp)+1) for i in range(len(self.states))]
        backtrack = [[0] * (len(inp)+1) for i in range(len(self.states))]

        # Initialise the arrays with incoming from start states
        for s in range(1, len(self.states)):
            viterbi[s][1] = self.state_graph[0][s] * self.observation_probabilities[s][inp[1]]
            backtrack[s][1] = 0

        # Calculation of the probabilities and only storing the maximum of probabilities
        for t in range(2, len(inp)):
            for s in range(1, len(self.states)):
                max_prob = 0
                index = 0

                for i in range(1, len(self.states)):
                    if max_prob < viterbi[i][t - 1] * self.state_graph[i][s] * self.observation_probabilities[s][inp[t]]:
                        max_prob = viterbi[i][t - 1] * self.state_graph[i][s] * self.observation_probabilities[s][inp[t]]
                        index = i

                viterbi[s][t] = max_prob
                backtrack[s][t] = index

        # An array the best possible path for the given input sequence
        trellis = []

        for i in range(0, len(inp)):
            trellis.append(0)

        prob = 0
        index = 0
        for i in range(1, len(self.states)):
            if prob < viterbi[i][len(inp) - 1]:
                prob = viterbi[i][len(inp) - 1]
                index = i

        # Total path probability at the last index and the value at state type.
        total_path_prob = prob
        trellis[len(inp) - 1] = index

        for i in range(len(inp) - 1, 1, -1):
            trellis[i - 1] = backtrack[trellis[i]][i]

        # Final sequence in the form of state names to be displayed as the final output
        final_sequence = ""
        for i in range(1, len(trellis)):
            final_sequence = final_sequence + " " + self.states[trellis[i]]

        return total_path_prob, final_sequence


if __name__ == "__main__":
    input_seq = sys.argv[1]
    viterbi = Viterbi(input_seq)
    sequence_prob, likely_sequence = viterbi.calculate()
    print ("For the input sequence: " + input_seq)
    print ("\nMost likely sequence generated is: " + likely_sequence)
    print ("Total probability of the sequence: " + str(sequence_prob))

