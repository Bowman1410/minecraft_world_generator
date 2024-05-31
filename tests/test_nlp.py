import unittest
from src.nlp.model import NLPModel

class TestNLPModel(unittest.TestCase):
    def test_generate_response(self):
        model = NLPModel()
        response = model.generate_response("Build a castle")
        self.assertIn("castle", response.lower())

    def test_extract_details(self):
        model = NLPModel()
        details = model.extract_details("Build a castle and a forest")
        self.assertTrue(details['castle'])
        self.assertTrue(details['forest'])

if __name__ == '__main__':
    unittest.main()