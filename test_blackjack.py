import blackjack


def test_make_card():
    card = blackjack.Card('10', 'hearts')
    expected_suit = 'hearts'
    expected_face = '10'
    assert card.suit == expected_suit
    assert card.face == expected_face


def test_make_deck():
    deck = blackjack.Deck()
    assert len(deck.cards) == 52


def test_deal_from_deck():
    deck = blackjack.Deck()
    expected_card = blackjack.Card('Ace', 'Hearts')

    card = deck.deal()
    assert card == expected_card
