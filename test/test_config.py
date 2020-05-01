import unittest
import config
import sys
import os

class TestConfig(unittest.TestCase):
    def test_getdata(self):
        dataset = config.Config.get_data_path("semeval")
        print(dataset)
        self.assertEqual(
            "/Users/parasol_tree/Resource/019 - Github/FSZoo/datasets/data_filtered/supervisedRE/semeval",
            dataset
        )



if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))
    unittest.main()
