# Intro to Python testing
# Testing Taxonomies: https://wiki.python.org/moin/PythonTestingToolsTaxonomy

# Python unittest reference https://docs.python.org/3/library/unittest.html

import io
import unittest
import unittest.mock

from soc_wk2_cert_cristina_tarantino import count_letters_list
from soc_wk2_cert_cristina_tarantino import numbers_to_letters
from soc_wk2_cert_cristina_tarantino import count_letters_dict


class TestCountLettersToList(unittest.TestCase):
    def test_count_letters_list_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = [['a', 2], ['b', 0], ['c', 2], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 4], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 2], ['o', 4], ['p', 0], ['q', 0], ['r', 1], ['s', 2], ['t', 1], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]

        self.assertEqual(count_letters_list(test_text), expected_result)

    def test_count_letters_list_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = [['a', 9804], ['b', 1746], ['c', 3003], ['d', 5469], ['e', 15396], ['f', 2383], ['g', 2944], ['h', 7890], ['i', 8634], ['j', 235], ['k', 1290], ['l', 5211], ['m', 2466], ['n', 8053], ['o', 9480], ['p', 1968], ['q', 220], ['r', 6612], ['s', 7269], ['t', 12204], ['u', 3979], ['v', 963], ['w', 2952], ['x', 176], ['y', 2584], ['z', 80]]

        self.assertEqual(count_letters_list(read_data), expected_result)


# I don't understand this test class code at the moment but it allows me to test the function
# https://stackoverflow.com/questions/33767627/how-to-write-a-unittest-for-console-print
class TestNumbersToLetters(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        numbers_to_letters()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_numbers_to_letters(self):
        self.assert_stdout(2, 'A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n')


class TestCountLettersToDic(unittest.TestCase):
    def test_count_letters_dict_string(self):
        test_text = "Ciao io sono Cristina"
        expected_result = {'a': 2, 'b': 0, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 4, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 2, 'o': 4, 'p': 0, 'q': 0, 'r': 1, 's': 2, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.assertEqual(count_letters_dict(test_text), expected_result)

    def test_count_letters_dict_file(self):
        filename = "../alice_in_wonderland.txt"
        # source http://www.gutenberg.org/files/11/11-0.txt

        # open the file in read only mode
        # source https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(filename) as f:
            read_data = f.read()
        f.closed

        expected_result = {'a': 9804, 'b': 1746, 'c': 3003, 'd': 5469, 'e': 15396, 'f': 2383, 'g': 2944, 'h': 7890, 'i': 8634, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2466, 'n': 8053, 'o': 9480, 'p': 1968, 'q': 220, 'r': 6612, 's': 7269, 't': 12204, 'u': 3979, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}

        self.assertEqual(count_letters_dict(read_data), expected_result)


if __name__ == '__main__':
    unittest.main()
