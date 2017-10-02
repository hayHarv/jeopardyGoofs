from .random_clue import (conn,
                          get_question)
import random
import nltk

def n_samples(n=500):
    corpus = []
    query = conn.execute('select category from questions limit {};'.format(n))
    for idx in range(n):
        question = query.fetchone()[0].split(' ')
        for word in question:
            corpus.append(word)

    return corpus


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
        bigrams = list(nltk.bigrams(tokens))
        for bigram in bigrams:
            self._learn_key(bigram[0], bigram[1])
    
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
