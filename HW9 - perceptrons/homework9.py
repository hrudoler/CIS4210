############################################################
# CIS 521: Perceptrons Homework
############################################################

student_name = "Helen Rudoler."

############################################################
# Imports
############################################################

import perceptrons_data as data
# import matplotlib.pyplot as plt
import math

# Include your imports here, if any are used.



############################################################
# Section 1: Perceptrons
############################################################

def dot(w, x):
    sum = 0
    for x_i, v_i in x.items():
        sum += w.get(x_i, 0) * v_i
    return sum

def sign(x):
    if x > 0:
        return True
    if x <= 0:
        return False
    # return 1

def argmax(ws, ys, x):
    max = float("-inf")
    argmax = None
    for y in ys:
        # print(y)
        d = dot(ws[y], x)
        if d > max:
            max = d
            argmax = y
    return argmax

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.w = {}
        for _ in range(iterations):
            for x, y in examples:
                y_hat = sign(dot(self.w, x))
                if y_hat != y:
                    for x_i, v_i in x.items():
                        if y:
                            self.w[x_i] = self.w.get(x_i, 0) + v_i
                        else:
                            self.w[x_i] = self.w.get(x_i, 0) - v_i


    def predict(self, x):
        return sign(dot(self.w, x))

class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.ys = {label for (_, label) in examples}
        self.ws = {y:{} for y in self.ys}
        for _ in range(iterations):
            for x, y in examples:
                y_hat = argmax(self.ws, self.ys, x)
                if y_hat != y:
                    for x_i, v_i in x.items():
                        self.ws[y][x_i] = self.ws[y].get(x_i, 0) + v_i
                        self.ws[y_hat][x_i] = self.ws[y_hat].get(x_i, 0) - v_i

    def predict(self, x):
        return argmax(self.ws, self.ys, x)

############################################################
# Section 2: Applications
############################################################

class IrisClassifier(object):

    def __init__(self, data):
        self.examples = [({i: x_i for i, x_i in enumerate(d[0])}, d[1]) for d in data]
        self.c = MulticlassPerceptron(self.examples, 5)

    def classify(self, instance):
        instance = ({i: x_i for i, x_i in enumerate(instance)})
        return self.c.predict(instance)

class DigitClassifier(object):

    def __init__(self, data):
        self.examples = [({i: x_i for i, x_i in enumerate(d[0])}, d[1]) for d in data]
        self.c = MulticlassPerceptron(self.examples, 10)

    def classify(self, instance):
        instance = ({i: x_i for i, x_i in enumerate(instance)})
        return self.c.predict(instance)

class BiasClassifier(object):

    def __init__(self, data):
        self.examples = [({1: d[0], "bias": 5}, d[1]) for d in data]
        self.c = BinaryPerceptron(self.examples,20)

    def classify(self, instance):
        instance = {1: instance, "bias": 5}
        return self.c.predict(instance)

class MysteryClassifier1(object):

    def __init__(self, data):
        self.examples = [({1:(d[0][0]**2 + d[0][1]**2) - 4}, d[1]) for d in data]
        self.c = BinaryPerceptron(self.examples,4)

    def classify(self, instance):
        # print(instance)
        instance = {1:(instance[0]**2 + instance[1]**2) - 4}
        return self.c.predict(instance)

class MysteryClassifier2(object):

    def __init__(self, data):
        self.examples = [({1:(d[0][0] * d[0][1] * d[0][2])}, d[1]) for d in data]
        self.c = BinaryPerceptron(self.examples, 4)

    def classify(self, instance):
        instance = {1:(instance[0] * instance[1] * instance[2])}
        return self.c.predict(instance)

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = 4

feedback_question_2 = """
This assignment was fun, I liked the plant classifier example. 
"""

feedback_question_3 = """
The mystery classifiers were a challenge, 
especially because I didn't really grasp what the goal was at first.
I think clearer directions on what the goal is would have been helpful.  
"""

# c = MysteryClassifier2(data.mystery2)
# print([c.classify(x) for x in ((1, 1, 1), (-1, -1, -1), (1, 2, -3), (-1, -2, 3))])