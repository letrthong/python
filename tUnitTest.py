import unittest

from t_json import tJsonData

class TestMathOperations(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
    
    def test_subtraction(self):
        data_path = './data.json'
        item_path = './item.json'

        tJson = tJsonData( data_path )
        tJson.remove_file()

        self.assertEqual(0, tJson.get_size())
        
        items = {
            'temp': '4'
        }
        tJson.create_item(items, item_path)
        tJson.add_item(item_path)
        self.assertEqual(1, tJson.get_size())

        tJson.remove_first_item()
        self.assertEqual(0, tJson.get_size())


if __name__ == '__main__':
    unittest.main()
