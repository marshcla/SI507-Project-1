# Do not change import statements.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained
# in the code description file works as that file says.
# If you have correctly written the tests,
# at least 3 tests should fail. If more than 3 tests fail,
# it should be because multiple of the test methods address the same
# problem in the code.
# You may write as many TestSuite subclasses as you like,
# but you should try to make these tests well-organized
# and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)


###########

class CardVariables(unittest.TestCase):

    def test_suit_names_list(self):
        d = Card()
        self.assertEqual(d.suit_names, ["Diamonds", "Clubs",
                                        "Hearts", "Spades"], "Test suit_names")

    def test_rank_levels_list(self):
        e = Card()
        self.assertEqual(e.rank_levels, [1, 2, 3, 4, 5, 6,
                                         7, 8, 9, 10, 11, 12, 13])

    def test_faces_dict(self):
        f = Card()
        self.assertEqual(f.faces, {1: "Ace", 11: "Jack",
                                   12: "Queen", 13: "King"}, "Testing face")


class CardConstructor(unittest.TestCase):

    def test_card_constructor1(self):

        g = Card(1, 5)
        self.assertTrue(g.suit == "Clubs", "Testing suit")

    def test_card_constructor2(self):

        h = Card(1, 5)
        self.assertTrue(h.rank <= 13, "Testing rank")
        self.assertTrue(h.rank >= 0, "Testing rank")

    def test_card_constructor3(self):

        i = Card(0, 12)
        self.assertTrue(i.suit == "Diamonds", "Testing .suit")
        self.assertTrue(i.rank == "Queen" or type(g.rank) == int,
                        "Testing .rank")
        self.assertTrue(type(i.rank_num) == int, "Testing .rank_num")

    def test_card_constructor4(self):

        j = Card(0, 12)  # Fails
        k = str(j)
        self.assertEqual(type(k), type("string"),
                         "Testing class Card's string method")
        self.assertEqual(k, "Queen of Diamonds",
                         "Testing class Card's string method")


class TestDeck(unittest.TestCase):

    def test_deck_constructor(self):

        d = Card(0, 12)
        e = Deck()
        f = e.cards
        self.assertTrue(type(f) == type([1, 2, 3]), "Testing .cards")

    def test_deck_string_method(self):

        f = Card(0, 12)
        g = Deck()
        h = g.__str__()
        i = h.split('\n')
        self.assertEqual(len(i), 52, "Testing string method of class Deck")

    def test_pop_card(self):

        f = Card(0, 12)
        g = Deck()
        h = g.pop_card()
        i = g.cards
        count = 52
        while (count > 0):
            return h
            count = count - 1
        else:
            self.assertEqual(len(i), 0, "Testing pop_card")

    def test_replace_card(self):

        f = Card(0, 1)
        d_test = Deck()
        g = Deck()
        h = g.pop_card(0)
        i = g.replace_card(f)
        g.sort_cards()
        self.assertTrue(str(d_test) == str(g), "Testing replace_card")

    def test_sort_cards(self):

        d = Deck()
        d2 = Deck()
        e = d.shuffle()
        f = d.sort_cards()
        self.assertTrue(str(d) == str(d2), "Testing sort_cards")

    def test_deal_hand(self):  # Fails  # For this test, I worked with Nikhil

        b = Deck()

        try:
            c = b.deal_hand(52)
            hand_list = [str(d) for d in c]

        except IndexError:
            assert False

    def test_shuffle(self):

        d = Deck()
        e = Deck()
        c = d.shuffle()
        self.assertFalse(e == d, "Testing shuffle")


class TestPlayWarGame(unittest.TestCase):

    def test_pwg1(self):

        c = play_war_game(testing=True)
        self.assertTrue(c[0] in ['Player1', 'Player2', 'Tie'],
                        "Testing play_war_game")

    def test_pwg2(self):

        w = play_war_game(testing=True)
        self.assertEqual(type(w[1]), int, "Testing play_war_game")

    def test_pwg3(self):

        c = play_war_game(testing=True)
        self.assertEqual(type(c), tuple, "Testing play_war_game")

    def test_pwg4(self):

        w = play_war_game(testing=True)
        if w[0] == 'Player1':
            self.assertTrue(w[1] > w[2])
        elif w[0] == 'Player2':
            self.assertTrue(w[2] > w[1])
        else:
            self.assertTrue(w[1] == w[2])


class TestShowSong(unittest.TestCase):

    def test_ss1(self):
        song1 = show_song()
        self.assertIsInstance(song1, Song, "Testing show_song")

    def test_ss2(self):  # Fails
        song2 = show_song("Wonderwall")
        self.assertTrue("Wonderwall" in str(song2), "Testing search term")

if __name__ == '__main__':
    unittest.main(verbosity=2)