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
    return [el for seq in seqs for el in seq]
    pass

## needs fixing!!
def transpose(matrix):
    tp = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    print(matrix[0][0])
    for ind_i, i in enumerate(matrix):
        for ind_j, j in enumerate(matrix[ind_i]):
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
    count = 0
    while count <= len(seq):
      yield seq[0:count]
      count += 1


def suffixes(seq):
    yield seq
    while seq:
      seq = seq[1:]
      yield seq

def slices(seq):
    i = 0
    j = 1
    while i < len(seq):
      while j <= len(seq):
        yield seq[i:j]
        j += 1
      i += 1
      j = i + 1

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    text = text.lower()
    text_as_list = text.split()
    return " ".join(text_as_list)

def no_vowels(text):
    without_vowels = [x for x in text if x.lower() not in ["a", "e", "i", "o", "u"]]
    return "".join(without_vowels)

def digits_to_words(text):
    out = []
    for letter in text:
        if letter == '0':
            out.append("zero")
        elif letter == '1':
            out.append("one")
        elif letter == '2':
            out.append("two")
        elif letter == '3':
            out.append("three")
        elif letter == '4':
            out.append("four")
        elif letter == '5':
            out.append("five")
        elif letter == '6':
            out.append("six")
        elif letter == '7':
            out.append("seven")
        elif letter == '8':
            out.append("eight")
        elif letter == '9':
            out.append("nine")
    if not out:
        return ""
    return " ".join(out)

def to_mixed_case(name):
    words = name.split("_")
    new_words = [x[0].upper() + x[1:].lower() if len(x) > 1 else x[0].upper() for x in words if x]
    if new_words:
        new_words[0] = new_words[0].lower()
    print(new_words)
    return "".join(new_words)

    

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        neg = []
        for coef in self.polynomial:
          neg.append((-coef[0], coef[1]))
        return Polynomial(neg)

    def __add__(self, other):
        first, second = list(self.polynomial), list(other.polynomial)
        return Polynomial(first + second)

    def __sub__(self, other):
        other = -other
        return self + other

    def __mul__(self, other):
        out = []
        for i in self.polynomial:
          for j in other.polynomial:
            coef = i[0] * j[0]
            power = i[1] + j[1]
            out.append((coef, power))
        return Polynomial(out)

    def __call__(self, x):
        return sum([t[0] * x**t[1] for t in list(self.polynomial)])

    def simplify(self):
        p = sorted(self.polynomial, key=lambda poly : poly[1], reverse=True)
        out = []
        pow = p[0][1]
        sum = 0
        for entry in p:
          if entry[1] == pow:
            sum += entry[0]
          else:
            if sum != 0:
              out.append((sum, pow))
            sum = entry[0]
            pow = entry[1]
        if sum:
          out.append((sum, pow))
        if not out:
          out = [(0, 0)]
        self.polynomial = tuple(out)

    def __str__(self):
        poly = self.polynomial
        out = []

        for index, entry in enumerate(poly):
          coef = entry[0]
          pow = entry[1]
          # take care of signs:
          # neg with no space for negative first entry
          if index == 0 and coef < 0:
            out.append("-")
          # positive non-first entry
          elif index != 0 and coef >= 0:
            out.append(" + ")
          # negative non-first entry
          elif index != 0:
            out.append(" - ")
          
          coef = abs(coef)
          #don't print coefficient if it's 1 unless the power is 0
          if coef == 1 and pow != 0:
            if pow == 1:
              out.append("x")
            else:
              out.append("x^" + str(pow))
          # if the power is 0 ONLY print the coefficient
          elif pow == 0:
            out.append(str(coef))

          # if the power is 1 don't print the power symbol
          elif pow == 1:
            out.append(str(coef) + "x")
          
          # typical entry
          else:
            out.append(str(coef) + "x^" + str(pow))
        return "".join(out)

############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
    out = []
    for mat in list_of_matrices:
        for element in mat.flat:
            out.append(element)
    return sorted(out, reverse=True)

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def POS_tag(sentence):
    sentence = sentence.lower()
    tokens = nltk.word_tokenize(sentence)
    stop_words = stopwords.words("english")
    sentence = [word for word in tokens if word not in stop_words and word.isalnum()]
    sentence = nltk.pos_tag(sentence)
    return sentence

############################################################
# Section 8: Feedback
############################################################

feedback_question_1 = """
Difficult to estimate because I worked on it in a lot of small chunks, but probably 4-5 hours in total.
"""

feedback_question_2 = """

I had never used generators, so I found that part challenging conceptually. 
Watching the portion of the recitaion about it as well as looking up examples of generator functions helped. 

I also thought some of the list comprehensions took a lot of tries to wrap my head around.

"""

feedback_question_3 = """
I liked that we had this assignment to get used to python, and I thought writing the polynomial class was especially fun.
"""