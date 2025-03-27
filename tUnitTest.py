import unittest

from t_json import tJsonData

class TestTJson(unittest.TestCase):
    data_path = './data.json'
    item_path = './item.json'

    def test_delete(self):
        tJson = tJsonData( self.data_path )
        tJson.remove_file()
        self.assertEqual(0, tJson.get_size())
    
    def test_add_one_item(self):
        tJson = tJsonData( self.data_path )
        tJson.remove_file()

        self.assertEqual(0, tJson.get_size())
        
        items = {
            'temp': '4'
        }
        tJson.create_item(items, self.item_path)
        tJson.add_item(self.item_path)
        self.assertEqual(1, tJson.get_size())

        tJson.remove_first_item()
        self.assertEqual(0, tJson.get_size())
    
    def test_add_two_items(self):
        tJson = tJsonData( self.data_path )
        tJson.remove_file()

        self.assertEqual(0, tJson.get_size())
        
        items = {
            'temp': '4'
        }
        tJson.create_item(items, self.item_path)
        tJson.add_item(self.item_path)

        items = {
            'temp': '5'
        }
        tJson.create_item(items, self.item_path)
        tJson.add_item(self.item_path)
        self.assertEqual(2, tJson.get_size())

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTJson('test_delete'))
    suite.addTest(TestTJson('test_add_one_item'))
    suite.addTest(TestTJson('test_add_two_items'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
