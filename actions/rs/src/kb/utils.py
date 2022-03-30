''' 
Author: Nguyen Phuc Minh
Lastest update: 23/3/2022
'''

from scipy import spatial
from typing import List

def get_cosine_similarity(d1:List,d2:List) -> float:
    ''' Compute cosine similarity between 2 list
    ''' 
    result = 1 - spatial.distance.cosine(d1, d2)
    return result