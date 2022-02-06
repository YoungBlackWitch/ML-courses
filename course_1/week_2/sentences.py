import pandas as pd 
import scipy as sc
import numpy as np
import re
from scipy import spatial


def read_file():
    text = []
    frequency = {}

    with open('course_1\week_2\sentences.txt', 'r') as f:

        for line in f.readlines():
            tmp = []

            for el in filter(lambda x: bool(x), re.split('[^a-z]',line.lower())):
                tmp.append(el)

                if el not in frequency:
                    frequency[el] = len(frequency)

            text.append(tmp) 

    return text, frequency


text, frequency = read_file()

matrix = np.zeros([22,254])

for i, line in enumerate(text):
    
    for j, el in enumerate(line):
        matrix[i,frequency[el]] += 1

cos = 1
k = 0

for i in range(1,len(matrix)):
    if cos >= spatial.distance.cosine(matrix[0],matrix[i]):
        cos = spatial.distance.cosine(matrix[0],matrix[i])
        g = k
        k = i

print(k, g)