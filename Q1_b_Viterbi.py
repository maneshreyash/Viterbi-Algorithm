import sys


class Viterbi:
    def __init__(self, sequence):
        self.prob_start = {"hot": 0.8, "cold": 0.2}
        self.prob_hot = {1: 0.2, 2: 0.2, 3: 0.4, "cold": 0.3, "hot": 0.7}
        self.prob_cold = {1: 0.5, 2: 0.4, 3: 0.1, "hot": 0.4, "cold": 0.6}
        self.hot = []
        self.cold = []
        self.inp = sequence

    def preprocess(self):
        temp = str(self.inp)
        ice_cream_array = []
        for digit in temp:
            ice_cream_array.append(int(digit))
        return ice_cream_array

    def calculate(self):
        inp = self.preprocess()
        self.hot.append(self.prob_start.get("hot") * self.prob_hot.get(inp[0]))
        self.cold.append(self.prob_start.get("cold") * self.prob_cold.get(inp[0]))
        for i in range(1, len(inp)):
            print (self.cold[i-1], self.prob_hot.get(inp[i]), self.prob_hot.get("cold"))
            h_h = self.prob_hot.get("hot") * self.prob_hot.get(inp[i]) * self.hot[i-1]
            h_c = self.prob_cold.get("hot") * self.prob_cold.get(inp[i]) * self.hot[i-1]
            self.hot.append(max(h_h, h_c))
            c_h = self.prob_hot.get("cold") * self.prob_hot.get(inp[i]) * self.cold[i-1]
            c_c = self.prob_cold.get("cold") * self.prob_cold.get(inp[i]) * self.cold[i-1]
            self.cold.append(max(c_h, c_c))
        return self.hot, self.cold


if __name__ == "__main__":
    input_seq = sys.argv[1]
    viterbi = Viterbi(input_seq)
    all_hot, all_cold = viterbi.calculate()
    print (all_hot)
    print (all_cold)
