import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        input_english = 'Hello'
        self.assertIsNotNone(input_english,'Input Not Null')
        self.assertEqual(english_to_french(input_english), 'Bonjour')
        self.assertNotEqual(english_to_french(input_english),'Bonjo')
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        input_french = 'Bonjour'
        self.assertIsNotNone(input_french ,'Input not Null')
        self.assertEqual(french_to_english(input_french), 'Hello') 
        self.assertNotEqual(french_to_english(input_french), 'Hell')
        
unittest.main()