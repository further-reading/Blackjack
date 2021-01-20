import random


FACES = [
    'Ace',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'Jack',
    'Queen',
    'King',
]

SUITS = [
    'Hearts',
    'Spades',
    'Diamonds',
    'Clubs',
]


class Card:
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face

    def __eq__(self, other):
        return self.face == other.face

    def __str__(self):
        return f'{self.face} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                card = Card(face, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card_out = self.cards.pop(0)
        return card_out


class Player:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.aces_to_burn = 0

    def update_hand(self, new_card):
        self.hand.append(new_card)
        if new_card.face.isnumeric():
            self.score += int(new_card.face)
        elif new_card.face in ['Jack', 'Queen', 'King']:
            self.score += 10
        elif new_card.face == 'Ace':
            self.score += 11
            self.aces_to_burn += 1

        if self.score > 21 and self.aces_to_burn:
            self.score -= 10
            self.aces_to_burn -= 1

    def state_score(self):
        return f'Score is {self.score} with {self.aces_to_burn} aces to burn'

    def state_hand(self):
        return f'Hand is {", ".join(self.hand)}'


class Game:
    def play(self):
        while True:
            self.play_round()
            again = input('Do you want to play again? (y)es or (n)o')
            if again != 'y':
                break

    def play_round(self):
        print('Welcome to Blackjack!')
        human = Player()
        dealer = Player()
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        self.deck.shuffle()

        new_card_down, new_card_up = self.deck.deal(), self.deck.deal()
        print(f'Dealer face-up is {new_card_up}')
        dealer.update_hand(new_card_down)
        dealer.update_hand(new_card_up)

        self.play_hand(human, False)

        if human.score > 21:
            print('You Busted - YOU LOSE!')
            return

        print(f'Dealer\'s pair is {new_card_down}, {new_card_up} - value: {dealer.score}')
        self.play_hand(dealer, True)
        print(f'Your score is {human.score} and dealer score is {dealer.score}')
        self.get_victor(human, dealer)

    def play_hand(self, player, is_dealer):
        while not self.ended(player):
            if not is_dealer:
                hit_or_stay = input('Do you want to (h)it or (s)tay?')
                if hit_or_stay == 's':
                    break
            else:
                input('Dealer prepares to draw a card')

            new_card = self.deck.deal()
            print(f'Dealer draws {new_card}')
            player.update_hand(new_card)
            if is_dealer:
                print(f'Dealer score is {player.score}')
            else:
                print(f'Your score is {player.score}')
            if is_dealer and player.score > 17:
                break

    def ended(self, player):
        return player.score >= 21

    def get_victor(self, player, dealer):
        if dealer.score > 21:
            print(f'Dealer has bust - YOU WIN!')
        elif dealer.score == player.score == 21:
            if len(player.hand) == len(dealer.hand):
                print(f'Tie! You LOSE!')
            elif len(player.hand) == 2:
                print(f'Blackjack on 2 cards - YOU WIN!')
            elif len(dealer.hand) == 2:
                print(f'Dealer Blackjack on 2 cards - YOU LOSE!')
        elif dealer.score == player.score:
            print(f'Tie! You LOSE!')
        elif player.score > dealer.score:
            print(f'You are higher - YOU WIN!')
        elif player.score < dealer.score:
            print(f'You are lower - YOU LOSE!')


if __name__ == '__main__':
    game = Game()
    game.play()
