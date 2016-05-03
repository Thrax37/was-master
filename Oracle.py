import sys
import itertools
from copy import deepcopy


MOVES_REQUIRED = 3

FLIPPED = 0
UNFLIPPED = 1


def filter_neighbors(neighbors, me, size):
    limit = size - MOVES_REQUIRED
    for data in neighbors:
        i, _, flipped, unflipped = map(int, data.split('_'))
        position = (me - i) % size
        if MOVES_REQUIRED >= position or position >= limit:
            yield i, [flipped, unflipped]


class Player:
    def __init__(self, raw_data):
        _, me, coins, *data = raw_data.split(';')

        self.num_players = len(data)
        self._me = int(me)
        self._coins = int(coins)
        self._state = dict(filter_neighbors(data, self._me, self.num_players))

    def reset(self):
        self.me = self._me
        self.coins = self._coins
        self.state = deepcopy(self._state)
        self.my_state = self.state[self.me]

    def invalid_move(self, move):
        if move in 'NRT':
            return False

        if move in '123'[:self.coins]:
            return False

        flipped, unflipped = self.my_state
        if flipped and move == 'U':
            return False
        if unflipped and move == 'F':
            return False

        if move in 'AXBYCZ'[:2 * unflipped]:
            return False

        return True

    def N(self):
        return 0

    def one(self):
        self.coins -= 1
        self.my_state[UNFLIPPED] += 1
        return -1

    def two(self):
        self.coins -= 2
        self.my_state[UNFLIPPED] += 2
        return -2

    def three(self):
        self.coins -= 3
        self.my_state[UNFLIPPED] += 3
        return -3

    def A(self):
        self.coins += 1
        self.my_state[UNFLIPPED] -= 1
        return 1

    def B(self):
        self.coins += 2
        self.my_state[UNFLIPPED] -= 2
        return 2

    def C(self):
        self.coins += 3
        self.my_state[UNFLIPPED] -= 3
        return 3

    def X(self):
        self.my_state[UNFLIPPED] -= 1
        return 0

    def Y(self):
        self.my_state[UNFLIPPED] -= 2
        return 0

    def Z(self):
        self.my_state[UNFLIPPED] -= 3
        return 0

    def R(self):
        self.me = (self.me + 1) % self.num_players
        flipped, unflipped = self.my_state = self.state[self.me]
        return 2 * flipped - unflipped

    def T(self):
        self.me = (self.me - 1) % self.num_players
        flipped, unflipped = self.my_state = self.state[self.me]
        return 2 * flipped - unflipped

    def F(self):
        self.my_state[FLIPPED] += 1
        self.my_state[UNFLIPPED] -= 1
        return 2

    def U(self):
        self.my_state[FLIPPED] -= 1
        self.my_state[UNFLIPPED] += 1
        return -2

setattr(Player, '1', Player.one)
setattr(Player, '2', Player.two)
setattr(Player, '3', Player.three)


def scenarii(player):
    for tries in itertools.product('N123ABCXYZRTFU', repeat=MOVES_REQUIRED):
        player.reset()
        points = 0
        for try_ in tries:
            if player.invalid_move(try_):
                break
            points += getattr(player, try_)()
        else:
            yield points, ''.join(tries)


if __name__ == '__main__':
    player = Player(sys.argv[1])
    print(max(scenarii(player))[1])