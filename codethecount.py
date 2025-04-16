import random

def running_count_value(card):
    if card in ['2', '3', '4', '5', '6']:
        return 1
    elif card in ['7', '8', '9']:
        return 0
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return -1
    return 0

def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def card_counting():
    print("\nStarting Black Jack Card Counting\n")

    decks = int(input("Enter the number of decks in play: "))
    cards_seen = 0
    total_cards = decks * 52
    running_count = 0
    all_cards_dealt = []

