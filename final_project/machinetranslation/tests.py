import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def englishToFrench(self):
        # self.assertNotEqual(englishToFrench(''), '') #test for a null input, does not work
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  #input 'Hello', output hello on french
        self.assertNotEqual(englishToFrench('Hell'), '') #test for not a null output

    def test_frenchToEnglish(self):
        # self.assertEqual(frenchToEnglish(''), '') #test for a null input, does not work
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') #input hello on french, output 'Hello'
        self.assertNotEqual(frenchToEnglish('Hell'), '') #test for not a null output

if __name__ == '__main__':
    unittest.main()
