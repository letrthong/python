import unittest
import os
import shutil
import json
from directory_tree_manager import DirectoryTreeManager

class TestDirectoryTreeManager(unittest.TestCase):
    def setUp(self):
        self.test_root = 'my_project'
        self.structure = {
            'old_folder': {
                'file.txt': None
            }
        }
        self.manager = DirectoryTreeManager(self.test_root)
        self.manager.create_structure(self.structure)
        self.manager.delete_folder("new_folder")
        self.manager.add_folder('src/new_module')
    # def tearDown(self):
        # if os.path.exists(self.test_root):
        #     shutil.rmtree(self.test_root)

    def test_rename_folder_success(self):
        old_path = os.path.join(self.test_root, 'old_folder')
        new_path = os.path.join(self.test_root, 'new_folder')

        self.assertTrue(os.path.exists(old_path))
        self.manager.rename_folder('old_folder', 'new_folder')
        self.assertFalse(os.path.exists(old_path))
        self.assertTrue(os.path.exists(new_path))

    def test_rename_folder_not_exist(self):
        self.manager.rename_folder('non_existing', 'new_name')
        new_path = os.path.join(self.test_root, 'new_name')
        self.assertFalse(os.path.exists(new_path))


class TestLoadTreeFromJson(unittest.TestCase):
    def setUp(self):
        self.test_root = 'test_load_json'
        self.json_file = 'test_structure.json'
        self.structure = {
            "folderA": {
                "file1.txt": None,
                "subfolder": {
                    "file2.txt": None
                }
            },
            "main.py": None
        }
        with open(self.json_file, 'w', encoding='utf-8') as f:
            json.dump(self.structure, f, indent=4)
        self.manager = DirectoryTreeManager(self.test_root)

    # def tearDown(self):
    #     if os.path.exists(self.test_root):
    #         shutil.rmtree(self.test_root)
    #     if os.path.exists(self.json_file):
    #         os.remove(self.json_file)

    def test_load_tree_from_json(self):
        self.manager.load_tree_from_json(self.json_file)
        self.assertTrue(os.path.exists(os.path.join(self.test_root, 'folderA', 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_root, 'folderA', 'subfolder', 'file2.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_root, 'main.py')))


if __name__ == '__main__':
    unittest.main()
