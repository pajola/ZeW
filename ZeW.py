'''
    Implementation of Zero-Width space attack (ZeW)

    version 0.2
    created: 25 December 2019
    author: Pajola Luca
    affiliation: University of Padova


    log:
        v 0.1:
            * Implementation of the class
            * Mask1 / light: insertion of a specified character in the middle of
                the given word
            * Mask2 / full: insertion of a specified chatacter between every
                character of the given word
        v 0.2:
            * Sanitization function
            * Addition of random index selection
'''
import numpy as np

class ZeroWidthSPaceAttack:
    '''define list of malicious characters'''
    def __init__(self):
        #define the list of malicious symbols
        self.symbols = [u'\u200b', u'\u200c', u'\u200d', u'\u200e', u'\u200f', #U+200x
                      u'\u202a', u'\u202b', u'\u202c', u'\u202d', #U+202x
                      u'\u2060', u'\u2061', u'\u2062', u'\u2063', u'\u2064',
                      u'\u2065', u'\u2066', u'\u2067', u'\u2068', u'\u2069',
                      u'\u206a', u'\u206b', u'\u206c', u'\u206d', u'\u206e' #U+206x
                      ]

        # self.symbols =[
        #     u'\u200b', #zero-width space
        #     u'\u200c', #Zero-Width Non-Joiner
        #     u'\u200d', #Zero-Width Joiner
        #     u'\u'
        # ]


        self.num_malicius_chars = len(self.symbols)


    '''insertion of malicious input in the middle of a given word;
        for example, given the word "love", the result is "loXve".
    '''
    def mask1(self, word, index = 0, random = True):
        '''word = target word \n index = index of malicious symbols from the
        given list\nrandom = if random True, a randomic index is selected\n'''

        #check the index
        if index < 0 or index > len(self.symbols):
            raise Exception("Invalid index.")

        #sample the index, if required
        if random:
            index = np.random.randint(len(self.symbols))

        #get the target character
        code = self.symbols[index]

        #prepare the result. it must to be unicode
        poison = []

        #calculate the middle of the word
        mid = len(word) // 2

        #create the final message
        poison.append(word[:mid])
        poison.append(code)
        poison.append(word[mid:])

        poison = ''.join(poison)

        return poison

    '''insertion of malicious input between each character of the word;

        for example, given the word "love", the result is "lXoXvXe".
    '''
    def mask2(self, word, index = 0, random = True):
        '''word = target word\nindex = index of malicious symbols from the
        given list\nrandom = if random True, a randomic index is selected\n'''

        #check the index
        if index < 0 or index > len(self.symbols):
            raise Exception("Invalid index.")

        #prepare the result. it must to be unicode
        poison = []

        for c in word:
            #select the zero-width space character
            #sample the index, if required
            if random:
                index = np.random.randint(len(self.symbols))

            #get the target character
            code = self.symbols[index]

            poison.append(c)
            poison.append(code)

        poison = ''.join(poison)

        return poison

    ''' define a function that remove Zero-Width SPace (ZWSP) characters '''
    def sanitization(self, sentence):
        #blacklist characters removal
        res = ''.join([c for c in sentence if c not in self.symbols])

        return res
