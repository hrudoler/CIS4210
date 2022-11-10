############################################################
# CIS 521: Language Models Homework 
############################################################

student_name = "Helen Rudoler."

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import string
import random

############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    tokens = []
    word = ""
    for char in text:
        if char == " ":
            if word != "":
                tokens.append(word)
            word = ""
        elif char in string.punctuation:
            if word != "":
                tokens.append(word)
            tokens.append(char)
            word = ""
        else:
            word += char
    if word != "":
        tokens += word
    return tokens


def ngrams(n, tokens):
    n_grams = []
    tokens.append("<END>")
    for index, token in enumerate(tokens):
        n_gram = ()
        for i in range(n - 1):
            back_index = index - i - 1
            if back_index < 0:
                n_gram = ("<START>",) + n_gram
            else: n_gram = (tokens[back_index],) + n_gram
        n_grams.append((n_gram, token))
    return n_grams


class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.n_gram_count = {}

    def update(self, sentence):
        n_grams = ngrams(self.n, tokenize(sentence))
        for context, token in n_grams:
            if context in self.n_gram_count:
                if token in self.n_gram_count[context]:
                    self.n_gram_count[context][token] += 1
                else: 
                    self.n_gram_count[context][token] = 1
            else: 
                self.n_gram_count[context] = {}
                self.n_gram_count[context][token] = 1

    def context_count(self, context):
        total_count = 0
        if context in self.n_gram_count:
            total_count = sum(self.n_gram_count[context].values())
        return total_count
        

    def prob(self, context, token):
        total_count = self.context_count(context)
        prob = 0
        if total_count > 0:
            if token in self.n_gram_count[context]:
                token_count = self.n_gram_count[context][token]
            else: token_count = 0
            prob = token_count/total_count
        return prob


    def random_token(self, context):
        r = random.random()
        tokens = list(self.n_gram_count[context].keys())
        weights = list(self.n_gram_count[context].values())
        return random.choices(tokens, weights)[0]

    def random_text(self, token_count):
        pass

    def perplexity(self, sentence):
        pass

def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 0

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""


if __name__ == '__main__':
    # ngrams(3, ["a", "b", "c"])
    m = NgramModel(2)
    m.update("a b c d")
    m.update("a b a b")
    print(m.n_gram_count)
    random.seed(2)
    print([m.random_token(("b",))
      for i in range(6)])
