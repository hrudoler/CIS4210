############################################################
# CIS 521: Python Skills Homework
############################################################

student_name = "Helen Rudoler"

# This is where your grade report will be sent.
student_email = "hrudoler@seas.upenn.edu" 

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """""
    python is both statically and dynamically typed depending on the scenario. An example of dynamic typing is 
    that the same variable can be redeclared to be a different type. 
"""

python_concepts_question_2 = """
    Dictionary keys must be distinct an immutable. Therefore using a list as a key is not allowed as lists can be modified. 
    A simple solution in this case would be to swap the key-value pairs, as strings can be used as keys (and a single location 
    will never have more than one coordinate!)
"""

python_concepts_question_3 = """
    Using join will be significantly faster. The for loop requires python to allocate space for each intermediary string as
    more and more strings are added, but the using python's built in functionatiy can avoid this.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    # [for seq in seqs]
    pass

def transpose(matrix):
    tp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for ind_i, i in matrix:
        for ind_j, j in matrix[i]:
            tp[ind_j][ind_i] = j
    return tp

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[0:len(seq):2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    pass

def suffixes(seq):
    pass

def slices(seq):
    pass

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    pass

def no_vowels(text):
    pass

def digits_to_words(text):
    pass

def to_mixed_case(name):
    pass

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass

############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
	pass

import nltk
def POS_tag(sentence):
	pass

############################################################
# Section 8: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

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

def main():
    def test_bool(x):
        if x % 2 == 0:
            return True
        return False
    def test_func(x):
        return x*x
    extract_and_apply([1, 2, 3], test_bool, test_func)

if __name__ == 'main':
    main()
    print("hello")