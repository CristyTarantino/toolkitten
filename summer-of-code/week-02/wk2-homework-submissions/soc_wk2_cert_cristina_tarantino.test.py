# Intro to Python testing
# Testing Taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# Python unittest reference https://docs.python.org/3/library/unittest.html

# import io
# import unittest
# import unittest.mock
# mock = unittest.mock.MagicMock()
# from unittest.mock import patch

import unittest
from unittest import mock
from io import StringIO

import soc_wk2_cert_cristina_tarantino as homework


class TestCharFrequencyListFromAlphabet(unittest.TestCase):
    def test_char_frequency_list_from_alphabet_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = [['a', 2], ['b', 0], ['c', 2], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 4], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 2], ['o', 4], ['p', 0], ['q', 0], ['r', 1], ['s', 2], ['t', 1], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]

        self.assertEqual(homework.char_frequency_list_from_alphabet(test_text), expected_result)

    def test_char_frequency_list_from_alphabet_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = [['a', 9804], ['b', 1746], ['c', 3003], ['d', 5469], ['e', 15396], ['f', 2383], ['g', 2944], ['h', 7890], ['i', 8634], ['j', 235], ['k', 1290], ['l', 5211], ['m', 2466], ['n', 8053], ['o', 9480], ['p', 1968], ['q', 220], ['r', 6612], ['s', 7269], ['t', 12204], ['u', 3979], ['v', 963], ['w', 2952], ['x', 176], ['y', 2584], ['z', 80]]

        self.assertEqual(homework.char_frequency_list_from_alphabet(read_data), expected_result)


class TestCharFrequencyListOnlyPresentAlphas(unittest.TestCase):
    def test_char_frequency_dict_only_present_alphas_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = [['a', 2], ['c', 2], ['i', 4], ['n', 2], ['o', 4], ['r', 1], ['s', 2], ['t', 1]]

        self.assertEqual(homework.char_frequency_list_only_present_alphas(test_text), expected_result)

    # def test_char_frequency_dict_only_present_alphas_file(self):
    #     filename = "../alice_in_wonderland.txt"
    #     # source http://www.gutenberg.org/files/11/11-0.txt
    #
    #     # open the file in read only mode
    #     # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    #     with open(filename) as f:
    #         read_data = f.read()
    #     f.closed
    #
    #     expected_result = [['a', 9804], ['b', 1746], ['c', 3003], ['d', 5469], ['e', 15396], ['f', 2383], ['g', 2944], ['h', 7890], ['i', 8634], ['j', 235], ['k', 1290], ['l', 5211], ['m', 2466], ['n', 8053], ['o', 9480], ['p', 1968], ['q', 220], ['r', 6612], ['s', 7269], ['t', 12204], ['u', 3979], ['v', 963], ['w', 2952], ['x', 176], ['y', 2584], ['z', 80]]
    #
    #     self.assertEqual(homework.char_frequency_list_only_present_alphas(read_data), expected_result)


# https://learnbyexample.gitbooks.io/python-basics/content/Testing.html#using-unittest.mock-to-test-user-input-and-program-output
# TODO research decorator and sys.stdout
class TestNumbersToLetters(unittest.TestCase):
        expected_result = 'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n'

        @mock.patch('sys.stdout', new_callable=StringIO)
        def test_numbers_to_letters(self, mock_stdout):
            homework.numbers_to_letters()
            self.assertEqual(mock_stdout.getvalue(), self.expected_result)


class TestCypherMessage(unittest.TestCase):
    def test_cypher_message(self):
        test_text = "Ciao io sono Cristina e ti amo tanto"
        expected_result = [67, 105, 97, 111, 32, 105, 111, 32, 115, 111, 110, 111, 32, 67, 114, 105, 115, 116, 105,
                                       110, 97, 32, 101, 32, 116, 105, 32, 97, 109, 111, 32, 116, 97, 110, 116, 111]

        with mock.patch('builtins.input', return_value=test_text):
            self.assertEqual(homework.cypher_message(), expected_result)


class TestCharFrequencyDictFromAlphabet(unittest.TestCase):
    def test_char_frequency_dict_from_alphabet_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = {'a': 2, 'b': 0, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 4, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 2, 'o': 4, 'p': 0, 'q': 0, 'r': 1, 's': 2, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertEqual(homework.char_frequency_dict_from_alphabet(test_text), expected_result)

    def test_char_frequency_dict_from_alphabet_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = {'a': 9804, 'b': 1746, 'c': 3003, 'd': 5469, 'e': 15396, 'f': 2383, 'g': 2944, 'h': 7890, 'i': 8634, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2466, 'n': 8053, 'o': 9480, 'p': 1968, 'q': 220, 'r': 6612, 's': 7269, 't': 12204, 'u': 3979, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}

        self.assertEqual(homework.char_frequency_dict_from_alphabet(read_data), expected_result)


class TestCharFrequencyDictOnlyPresentAlphas(unittest.TestCase):
    def test_char_frequency_dict_only_present_alphas_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = {'c': 2, 'i': 4, 'a': 2, 'o': 4, 's': 2, 'n': 2, 'r': 1, 't': 1}
        self.assertEqual(homework.char_frequency_dict_only_present_alphas(test_text), expected_result)

    def test_char_frequency_dict_only_present_alphast_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = {'a': 9804, 'b': 1746, 'c': 3003, 'd': 5469, 'e': 15396, 'f': 2383, 'g': 2944, 'h': 7890, 'i': 8634, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2466, 'n': 8053, 'o': 9480, 'p': 1968, 'q': 220, 'r': 6612, 's': 7269, 't': 12204, 'u': 3979, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}

        self.assertEqual(homework.char_frequency_dict_only_present_alphas(read_data), expected_result)


if __name__ == '__main__':
    unittest.main()