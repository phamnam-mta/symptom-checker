''' 
Author: Nguyen Phuc Minh
Lastest update: 23/3/2022
'''

import os
import Levenshtein

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from typing import Any, List
from actions.rs.src.kb.utils import get_cosine_similarity

class NLPOutput:
    def __init__(self,str1:str, str2:str, method:int, threshold:float, score:float, result:bool) -> None:
        self.str1 = str1
        self.str2 = str2
        self.method = method
        self.threshold = threshold
        self.score = score
        self.result = result

    def update(self,score):
        self.score = score
        self.result = bool(self.score >= self.threshold)
        
class NLP:
    ''' A class handles NLP technique
    Supported features:
    - compare_string() compare string
    '''
    def __init__(self) -> None:
        pass
        # if os.path.exists(W2V_PATH):
        #     print(f"Reading word2vec at {W2V_PATH}")
        #     from gensim.models import KeyedVectors
        #     self.model = KeyedVectors.load_word2vec_format(W2V_PATH)

    def compare_string(self,str1:str,str2:str,method:str,threshold:float) -> Any:
        ''' Compute string distance between str1 & str2
        Args:
            - method (str)
            - threshold (float) : 
        '''
        assert method in ['fuzzy','semantic','edit']

        result = NLPOutput(
            str1 = str1,
            str2 = str2,
            method = method,
            threshold = threshold,
            score = 0,
            result = False
        )
        str1 = str1.lower()
        str2 = str2.lower()

        if method == 'fuzzy':
            score = self.compute_fuzzy(str1,str2)
        
        if method == 'edit':
            score = self.compute_edit(str1,str2)

        if method == 'semantic':
            score = self.compute_semantic(str1,str2)

        # Update result
        result.update(score)
        return result

    @staticmethod
    def compute_edit(str1:str,str2:str) -> int:
        return Levenshtein.distance(str1, str2)
    
    @staticmethod
    def compute_fuzzy(str1:str,str2:str) -> float:
        return fuzz.ratio(str1,str2)

    @staticmethod
    def compute_semantic(str1:str,str2:str) -> float:
        ''' Return cosine similarity between 2 string
        '''
        try:
            v1 = get_sentence_presentation(str1)
            v2 = get_sentence_presentation(str2)
            result = get_cosine_similarity(v1,v2)
        except:
            print("Model w2v at {W2V} may not exists. Please download or change W2V_PATH at src/constants/kb.py")
            result = 0
        return result

    @staticmethod
    def is_included(str1:str,str2:str) -> bool:
        str1 = str1.lower()
        str2 = str2.lower()
        a = str1.split(' ')
        b = str2.split(' ')
        return bool(set(a) & set(b))

    
    def get_sentence_presentation(self,name:str) -> List:
        ''' Return a list (d-dimention) represents given name
        '''
        presentation_vector = []
        for token in name.strip().lower().split(' '):
            w = self.model.wv[token] #(100,)
            presentation_vector.append(w)

        result = [sum(sub_list) / len(sub_list) for sub_list in zip(*presentation_vector)]
        return result