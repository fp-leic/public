#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:40:53 2019

@author: Geir Arne Hjelle
Real Python, Python Type Checking (Guide), Jan 07, 2019
https://realpython.com/python-type-checking/#example-play-some-cards
"""

import random

# card suits
SUITS : list[str] = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS : list[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

# a card is a tuple of (suit,rank); each of these is a string
Card = tuple[str, str]
# a deck is a list of cards (in some order)
Deck = list[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(suit, rank) for rank in RANKS for suit in SUITS]
    #if shuffle:
    #    random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names: list[str], start=None) -> list[str]:
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def play() -> None:
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names: list[str] = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while len(hands[start_player]) > 0:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()

if __name__ == "__main__":
    play()

