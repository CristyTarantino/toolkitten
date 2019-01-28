"""
Description - Test Week 2 homework for 1mwtt program
Author - Cristina Tarantino
Date - August 2018
"""

# Intro to Python testing
# Testing Taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# Python unittest reference https://docs.python.org/3/library/unittest.html

from io import StringIO
import unittest
from unittest import mock
import random


import soc_wk2_cert_cristina_tarantino as homework


class TestCharFrequencyListFromAlphabet(unittest.TestCase):
    def test_char_frequency_list_from_alphabet_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = [['a', 2], ['b', 0], ['c', 2], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 4],
                           ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 2], ['o', 4], ['p', 0], ['q', 0], ['r', 1],
                           ['s', 2], ['t', 1], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]

        self.assertEqual(homework.char_frequency_list_from_alphabet(test_text), expected_result)

    def test_char_frequency_list_from_alphabet_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = [['a', 9804], ['b', 1746], ['c', 3003], ['d', 5469], ['e', 15396], ['f', 2383], ['g', 2944],
                           ['h', 7890], ['i', 8634], ['j', 235], ['k', 1290], ['l', 5211], ['m', 2466], ['n', 8053],
                           ['o', 9480], ['p', 1968], ['q', 220], ['r', 6612], ['s', 7269], ['t', 12204], ['u', 3979],
                           ['v', 963], ['w', 2952], ['x', 176], ['y', 2584], ['z', 80]]

        self.assertEqual(homework.char_frequency_list_from_alphabet(read_data), expected_result)

    def test_char_frequency_list_from_alphabet_non_alpha(self):
        test_text = "Ciao. 1 50170 Cristina!!!"
        expected_result = [['a', 2], ['b', 0], ['c', 2], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 3],
                           ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 1], ['o', 1], ['p', 0], ['q', 0], ['r', 1],
                           ['s', 1], ['t', 1], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]

        self.assertEqual(homework.char_frequency_list_from_alphabet(test_text), expected_result)


class TestCharFrequencyListOnlyPresentAlphas(unittest.TestCase):
    def test_char_frequency_dict_only_present_alphas_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = [['a', 2], ['c', 2], ['i', 4], ['n', 2], ['o', 4], ['r', 1], ['s', 2], ['t', 1]]

        self.assertEqual(homework.char_frequency_list_only_present_alphas(test_text), expected_result)

    def test_char_frequency_dict_only_present_alphas_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = [['a', 9804], ['b', 1746], ['c', 3003], ['d', 5469], ['e', 15396], ['f', 2383], ['g', 2944],
                           ['h', 7890], ['i', 8634], ['j', 235], ['k', 1290], ['l', 5211], ['m', 2466], ['n', 8053],
                           ['o', 9480], ['p', 1968], ['q', 220], ['r', 6612], ['s', 7269], ['t', 12204], ['u', 3979],
                           ['v', 963], ['w', 2952], ['x', 176], ['y', 2584], ['z', 80]]

        self.assertEqual(homework.char_frequency_list_only_present_alphas(read_data), expected_result)

    def test_char_frequency_dict_only_present_alphas_non_alpha(self):
        test_text = "Ciao. 1 50170 Cristina!!!"
        expected_result = [['a', 2], ['c', 2], ['i', 3], ['n', 1], ['o', 1], ['r', 1], ['s', 1], ['t', 1]]

        self.assertEqual(homework.char_frequency_list_only_present_alphas(test_text), expected_result)


# https://learnbyexample.gitbooks.io/python-basics/content/Testing.html#using-unittest.mock-to-test-user-input-and-program-output
class TestNumbersToLetters(unittest.TestCase):

    # capture the console into a mock
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_numbers_to_letters(self, mock_stdout):
        expected_result = 'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ' \
                          '\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n'
        homework.numbers_to_letters()

        # get the value captured in the mock and compare it to the expected result
        self.assertEqual(mock_stdout.getvalue(), expected_result)


class TestCypherMessage(unittest.TestCase):
    def test_cypher_message(self):
        test_text = "Ciao io sono Cristina e ti amo tanto"
        expected_result = [67, 105, 97, 111, 32, 105, 111, 32, 115, 111, 110, 111, 32, 67, 114, 105, 115, 116, 105,
                           110, 97, 32, 101, 32, 116, 105, 32, 97, 109, 111, 32, 116, 97, 110, 116, 111]

        # when the console requires an input return the value specified
        with mock.patch('builtins.input', return_value=test_text):
            self.assertEqual(homework.cypher_message(), expected_result)


class TestEncryptionCeaserCypher(unittest.TestCase):
    def test_encryption_ceaser_cypher_string(self):
        num = 3
        test_text = "Ciao io sono Cristina"
        expected_result = "Fldr lr vrqr Fulvwlqd"

        # when the console requires an input return the values specified
        # (by using side_effect you can specify an array of inputs)
        # please refer to https://docs.python.org/3/library/unittest.mock.html for more info
        # due to time constrains I only checked those subjects superficially
        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.encryption_ceaser_cypher(), expected_result)

    def test_encryption_ceaser_cypher_number(self):
        num = 3
        test_text = "Ciao io sono Cristina and I love the number 29"
        expected_result = "Fldr lr vrqr Fulvwlqd dqg L oryh wkh qxpehu 29"

        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.encryption_ceaser_cypher(), expected_result)

    def test_encryption_ceaser_cypher_roman_number(self):
        num = 3
        test_text = "Ciao io sono Cristina and I love the number IXXX"
        expected_result = "Fldr lr vrqr Fulvwlqd dqg L oryh wkh qxpehu LAAA"

        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.encryption_ceaser_cypher(), expected_result)


class TestDecryptionCeaserCypher(unittest.TestCase):
    def test_encryption_ceaser_cypher_string(self):
        num = 3
        test_text = "Fldr lr vrqr Fulvwlqd"
        expected_result = "Ciao io sono Cristina"

        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.decryption_ceaser_cypher(), expected_result)

    def test_encryption_ceaser_cypher_number(self):
        num = 3
        test_text = "Fldr lr vrqr Fulvwlqd dqg L oryh wkh qxpehu 29"
        expected_result = "Ciao io sono Cristina and I love the number 29"

        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.decryption_ceaser_cypher(), expected_result)

    def test_encryption_ceaser_cypher_roman_number(self):
        num = 3
        test_text = "Fldr lr vrqr Fulvwlqd dqg L oryh wkh qxpehu LAAA"
        expected_result = "Ciao io sono Cristina and I love the number IXXX"

        with mock.patch('builtins.input', side_effect=[num, test_text]):
            self.assertEqual(homework.decryption_ceaser_cypher(), expected_result)


class TestPrintBoard(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_print_board_eleven(self, mock_stdout):
        L = "land"
        W = "water"

        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, W],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        expected_result = (W + "\n") * 11 + (
                            W + "\n") * 4 + (L + "\n") * 2 + (W + "\n") * 5 + (
                            W + "\n") * 8 + (L + "\n") * 2 + (W + "\n") + (
                            W + "\n") * 3 + (L + "\n") + (W + "\n") * 5 + (L + "\n") + (W + "\n") + (
                            W + "\n") * 3 + (L + "\n") + (W + "\n") + (L + "\n") * 2 + (W + "\n") * 4 + (
                            W + "\n") * 4 + (L + "\n") * 4 + (W + "\n") * 3 + (
                            W + "\n") * 3 + (L + "\n") * 7 + (W + "\n") + (
                            W + "\n") * 3 + (L + "\n") * 2 + (W + "\n") + (L + "\n") * 3 + (W + "\n") * 2 + (
                            W + "\n") * 6 + (L + "\n") * 2 + (W + "\n") * 3 + (
                            W + "\n") + (L + "\n") + (W + "\n") * 3 + (L + "\n") + (W + "\n") * 5 + (
                            W + "\n") * 11

        homework.print_board(world)

        # display the whole diff
        self.maxDiff = None

        self.assertEqual(mock_stdout.getvalue(), expected_result)


class TestPrintReversedBoard(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_print_board_eleven(self, mock_stdout):
        L = "land"
        W = "water"

        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, W],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        expected_result = (W + "\n") * 11 + (
                            W + "\n") * 5 + (L + "\n") + (W + "\n") * 3 + (L + "\n") + (W + "\n") + (
                            W + "\n") * 3 + (L + "\n") * 2 + (W + "\n") * 6 + (
                            W + "\n") * 2 + (L + "\n") * 3 + (W + "\n") + (L + "\n") * 2 + (W + "\n") * 3 + (
                            W + "\n") + (L + "\n") * 7 + (W + "\n") * 3 + (
                            W + "\n") * 3 + (L + "\n") * 4 + (W + "\n") * 4 + (
                            W + "\n") * 4 + (L + "\n") * 2 + (W + "\n") + (L + "\n") + (W + "\n") * 3 + (
                            W + "\n") + (L + "\n") + (W + "\n") * 5 + (L + "\n") + (W + "\n") * 3 + (
                            W + "\n") + (L + "\n") * 2 + (W + "\n") * 8 + (
                            W + "\n") * 5 + (L + "\n") * 2 + (W + "\n") * 4 + (
                            W + "\n") * 11

        homework.print_reversed_board(world)

        # display the whole diff
        self.maxDiff = None

        self.assertEqual(mock_stdout.getvalue(), expected_result)


class TestGenerateRandomBoard(unittest.TestCase):
    def test_print_board_eleven(self):
        N = 11

        # test that the number of rows is N
        self.assertEqual(len(homework.generate_random_board(N)), N)

        # and the number of columns is N
        self.assertEqual(len(homework.generate_random_board(N)[0]), N)

    def test_print_board_n_time_m(self):
        N = 5
        M = 4

        # test that the number of rows is N
        self.assertEqual(len(homework.generate_random_board(N, M)), N)

        # and the number of columns is N
        self.assertEqual(len(homework.generate_random_board(N, M)[0]), M)

    def test_print_board_randomness(self):
        N = 5

        L = "land"
        W = "water"

        expected_result = [
                            [W, W, L, W, W],
                            [W, W, W, W, L],
                            [L, W, L, L, W],
                            [L, W, L, L, W],
                            [W, L, W, W, W]
                          ]

        # Settable seed enables you to intentionally repeat your sequences by reusing the same seed.
        # https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
        random.seed(0)

        random_world = homework.generate_random_board(N)

        self.assertEqual(random_world, expected_result)


class TestContinentCounter(unittest.TestCase):
    def test_continent_counter_from_zero(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, W],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        self.assertEqual(homework.continent_counter(world, 0, 0), 0)

    def test_continent_counter_from_number(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, W],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        self.assertEqual(homework.continent_counter(world, 5, 5), 23)

    def test_continent_counter_border_edge(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        self.assertEqual(homework.continent_counter(world, 5, 5), 24)

    def test_continent_counter_n_times_m(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L],
            [W, W, W, L, W, W, W, W, W, L],
            [W, W, W, L, W, L, L, W, W, W],
            [W, W, W, W, L, L, L, L, W, W],
            [W, W, W, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W],
            [W, W, W, W, W, W, L, L, W, W],
            [W, L, W, W, W, L, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W]
        ]

        self.assertEqual(homework.continent_counter(world, 5, 5), 23)


class TestFindContinents(unittest.TestCase):
    def test_find_continets_no_border_edge(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, W],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        expected_result = {'continent-row-1-column-9': 1, 'continent-row-3-column-3': 23, 'continent-row-4-column-1': 2,
                           'continent-row-8-column-2': 3}

        self.assertEqual(homework.find_continets(world), expected_result)

    def test_find_continets_border_edge(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

        expected_result = {'continent-row-1-column-9': 1, 'continent-row-3-column-3': 24, 'continent-row-4-column-1': 2,
                           'continent-row-8-column-2': 3}

        self.assertEqual(homework.find_continets(world), expected_result)

    def test_find_continets_n_times_m(self):
        L = 'land'
        W = 'water'
        world = [
            [W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L],
            [W, W, W, L, W, W, W, W, W, L],
            [W, W, W, L, W, L, L, W, W, W],
            [W, W, W, W, L, L, L, L, W, W],
            [W, W, W, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W],
            [W, W, W, W, W, W, L, L, W, W],
            [W, L, W, W, W, L, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W]
        ]

        expected_result = {'continent-row-1-column-9': 1, 'continent-row-3-column-3': 23, 'continent-row-4-column-1': 2,
                           'continent-row-8-column-2': 3}

        self.assertEqual(homework.find_continets(world), expected_result)


class TestFindLargestNContinents(unittest.TestCase):
    def setUp(self):
        L = 'land'
        W = 'water'
        self.world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

    def tearDown(self):
        L = 'land'
        W = 'water'
        self.world = [
            [W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, L, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, L, L, W],
            [W, W, W, L, W, W, W, W, W, L, W],
            [W, W, W, L, W, L, L, W, W, W, W],
            [W, W, W, W, L, L, L, L, W, W, W],
            [W, W, W, L, L, L, L, L, L, L, L],
            [W, W, W, L, L, W, L, L, L, W, W],
            [W, W, W, W, W, W, L, L, W, W, W],
            [W, L, W, W, W, L, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W]
        ]

    def test_find_largest_n_continents_zero(self):
        expected_result = {}

        self.assertEqual(homework.find_largest_n_continents(self.world, 0), expected_result)

    def test_find_largest_n_continents_one(self):
        expected_result = {'continent-row-3-column-3': 24}

        self.assertEqual(homework.find_largest_n_continents(self.world, 1), expected_result)

    def test_find_largest_n_continents_two(self):
        expected_result = {'continent-row-3-column-3': 24, 'continent-row-8-column-2': 3}

        self.assertEqual(homework.find_largest_n_continents(self.world, 2), expected_result)

    def test_find_largest_n_continents_tot_length(self):
        expected_result = {'continent-row-3-column-3': 24, 'continent-row-8-column-2': 3, 'continent-row-4-column-1': 2,
                           'continent-row-1-column-9': 1}

        self.assertEqual(homework.find_largest_n_continents(self.world, len(self.world)), expected_result)

    def test_find_largest_n_continents_greater_tot_length(self):
        expected_result = {'continent-row-3-column-3': 24, 'continent-row-8-column-2': 3,
                           'continent-row-4-column-1': 2,
                           'continent-row-1-column-9': 1}

        self.assertEqual(homework.find_largest_n_continents(self.world, len(self.world)+1), expected_result)


class TestCharFrequencyDictFromAlphabet(unittest.TestCase):
    def test_char_frequency_dict_from_alphabet_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = {'a': 2, 'b': 0, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 4, 'j': 0, 'k': 0,
                           'l': 0, 'm': 0, 'n': 2, 'o': 4, 'p': 0, 'q': 0, 'r': 1, 's': 2, 't': 1, 'u': 0, 'v': 0,
                           'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertEqual(homework.char_frequency_dict_from_alphabet(test_text), expected_result)

    def test_char_frequency_dict_from_alphabet_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = {'a': 9804, 'b': 1746, 'c': 3003, 'd': 5469, 'e': 15396, 'f': 2383, 'g': 2944, 'h': 7890,
                           'i': 8634, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2466, 'n': 8053, 'o': 9480, 'p': 1968,
                           'q': 220, 'r': 6612, 's': 7269, 't': 12204, 'u': 3979, 'v': 963, 'w': 2952, 'x': 176,
                           'y': 2584, 'z': 80}

        self.assertEqual(homework.char_frequency_dict_from_alphabet(read_data), expected_result)

    def test_char_frequency_list_from_alphabet_non_alpha(self):
        test_text = "Ciao. 1 50170 Cristina!!!"
        expected_result = {'a': 2, 'b': 0, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 3,
                           'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 1,
                           's': 1, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        self.assertEqual(homework.char_frequency_dict_from_alphabet(test_text), expected_result)


class TestCharFrequencyDictOnlyPresentAlphas(unittest.TestCase):
    def test_char_frequency_dict_only_present_alphas_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = {'c': 2, 'i': 4, 'a': 2, 'o': 4, 's': 2, 'n': 2, 'r': 1, 't': 1}
        self.assertEqual(homework.char_frequency_dict_only_present_alphas(test_text), expected_result)

    def test_char_frequency_dict_only_present_alphas_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = {'a': 9804, 'b': 1746, 'c': 3003, 'd': 5469, 'e': 15396, 'f': 2383, 'g': 2944, 'h': 7890,
                           'i': 8634, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2466, 'n': 8053, 'o': 9480, 'p': 1968,
                           'q': 220, 'r': 6612, 's': 7269, 't': 12204, 'u': 3979, 'v': 963, 'w': 2952, 'x': 176,
                           'y': 2584, 'z': 80}

        self.assertEqual(homework.char_frequency_dict_only_present_alphas(read_data), expected_result)

    def test_char_frequency_dict_only_present_alphas_non_alpha(self):
        test_text = "Ciao. 1 50170 Cristina!!!"
        expected_result = {'a': 2, 'c': 2, 'i': 3, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1}

        self.assertEqual(homework.char_frequency_dict_only_present_alphas(test_text), expected_result)


class TestSong(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_sing_me_a_song(self, mock_stdout):
        lyric = ["Happy birthday to you",
                 "I don't want to get sued",
                 "So I'll stop right there"]

        expected_result = lyric[0] + "\n" + lyric[1] + "\n" + lyric[2] + "\n"

        happy_bday = homework.Song(lyric)
        happy_bday.sing_me_a_song()
        self.assertEqual(mock_stdout.getvalue(), expected_result)


class TestDictSortValue(unittest.TestCase):
    def test_sort_dict_by_numeric_value_numbers(self):
        input_dict = {'c': 24, 'z': 1, 'a': 100, 'r': 6612, 'h': 7890}
        expected_result = {'h': 7890, 'r': 6612, 'a': 100, 'c': 24, 'z': 1}

        self.assertEqual(homework.sort_dict_by_numeric_value(input_dict), expected_result)


class TestDictSortKey(unittest.TestCase):
    def test_sort_dict_by_key(self):
        input_dict = {'c': 24, 'z': 1, 'a': 100, 'r': 6612, 'h': 7890}
        expected_result = {'a': 100, 'c': 24, 'h': 7890, 'r': 6612, 'z': 1}

        self.assertEqual(homework.sort_dict_by_key(input_dict), expected_result)


class TestPerson(unittest.TestCase):
    def test_person_with_country(self):
        person1 = homework.Person('Cristina', 'Tarantino', 'Italy')

        self.assertEqual(person1.firstname, 'Cristina')
        self.assertEqual(person1.lastname, 'Tarantino')
        self.assertEqual(person1.country, 'Italy')

    def test_person_without_country(self):
        person1 = homework.Person('Cristina', 'Tarantino')

        self.assertEqual(person1.firstname, 'Cristina')
        self.assertEqual(person1.lastname, 'Tarantino')
        self.assertEqual(person1.country, None)


class TestUser(unittest.TestCase):
    def test_person_with_country(self):
        person1 = homework.User('Cristina', 'Tarantino', 'cristina@tarantino.io', 'Italy')

        self.assertEqual(person1.firstname, 'Cristina')
        self.assertEqual(person1.lastname, 'Tarantino')
        self.assertEqual(person1.country, 'Italy')
        self.assertEqual(person1.email, 'cristina@tarantino.io')
        self.assertEqual(person1.uid, 1)

    def test_person_without_country(self):
        person2 = homework.User('Cristina2', 'Tarantino2', 'cristina@tarantino.io')
        person3 = homework.User('Cristina3', 'Tarantino3', 'cristina@tarantino.io')

        self.assertEqual(person2.uid, 2)
        self.assertEqual(person3.uid, 3)


if __name__ == '__main__':
    unittest.main()
