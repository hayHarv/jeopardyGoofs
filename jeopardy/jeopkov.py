from .random_clue import (conn,
                          get_question)
import random
import nltk


def n_samples(type='category', n=500):
    '''
    Selects  n-items from jeopardy database

    Parameters
    ----------
    type: str
        'category' selects jeopardy categories
        'question_text' selects jeopardy clues

    Returns
    ----------
    List of tokens
    '''
    tokens = []
    query = conn.execute('select {} from questions where category != \'final\' limit {};'.format(type, n))
    for idx in range(n):
        question = query.fetchone()[0].split(' ')
        for word in question:
            tokens.append(word)

    return tokens


class MarkovChain:
    '''
    Markov Chain for Learning n-grams


    '''
    def __init__(self):
        self.memory = {}

    def _learn_key(self, key, value):
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append(value)

    def learn(self, tokens):
        '''
        learn markov chain from tokens

        Parameters
        ----------
        tokens : list of tokens in order of appearance
        '''
        bigrams = list(nltk.bigrams(tokens))
        for bigram in bigrams:
            if '' not in bigram:
                self._learn_key(bigram[0], bigram[1])
            else:
                pass
    
    def _next(self, current_state):
        next_possible = self.memory.get(current_state)

        if not next_possible:
            next_possible = self.memory.keys()

        return random.sample(next_possible, 1)[0]

    def babble(self, amount, state=''):
        if not amount:
            return state
        
        next_word = self._next(state)
        return state + ' ' + self.babble(amount -1, next_word)
    
    def fresh_babble(self, amount):
        return self.babble(amount)
