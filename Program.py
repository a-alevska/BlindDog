from Environment import *
from PZ1 import *
from agents import *
from utils import *


def program(percepts):
    '''Returns an action based on the dog percepts'''
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'