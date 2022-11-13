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
        if context not in self.n_gram_count:
            return None
        tokens = list(self.n_gram_count[context].keys())
        weights = list(self.n_gram_count[context].values())
        return random.choices(tokens, weights)[0]


    def random_text(self, token_count):
        if self.n == 1: starting_context = ()
        else: starting_context = tuple(["<START>" for x in range(self.n - 1)])
        context = starting_context
        out_string = ""
        isnt_first = False
        for _ in range(token_count):
            if isnt_first:
                out_string += " "
            token = self.random_token(context)
            out_string += (str(token))
            if token == "<END>":
                context = starting_context
            elif self.n > 1:
                context = context[1:] + (str(token),)
            isnt_first = True
        return out_string

    def perplexity(self, sentence):
        if self.n == 1: starting_context = ()
        else: starting_context = tuple(["<START>" for x in range(self.n - 1)])

def create_ngram_model(n, path):
    m = NgramModel(n)
    with open(path) as f: 
        sentences = f.readlines()
        for sentence in sentences:
            m.update(sentence)
    return m
    

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 3

feedback_question_2 = """
I'm somewhat perplexed by the perplexity. 
"""

feedback_question_3 = """
generating the realisic sentences was so cool!!
"""


if __name__ == '__main__':
    # ngrams(3, ["a", "b", "c"])
    # m = NgramModel(2)
    # m.update("a b c d")
    # m.update("a b a b")
    # random.seed(2)
    # print(m.random_text(15))
    m = create_ngram_model(3, "austen.txt")
    print(m.random_text(30))
