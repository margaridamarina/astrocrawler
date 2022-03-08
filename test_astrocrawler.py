from unittest import TestCase
from astrocrawler import extract_data
import json

class TestData(TestCase):
    def test_extract_data(self):
        with open('Post.html', 'r') as f:
            post = f.read()
        
        # post_teste = extract_data([post])
        with open('Post-teste.json', 'r') as f:
            # json.dump(post_teste, f)
            post_test = json.load(f)


        self.assertEqual(extract_data([post]), post_test)
