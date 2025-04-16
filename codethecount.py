import random

def running_count_value(card):
    if card in ['2', '3', '4', '5', '6']:
        return 1
    elif card in ['7', '8', '9']:
        return 0
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return -1
    return 0