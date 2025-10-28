import os
import shutil
import json

class DirectoryTreeManager:
    def __init__(self, root_path):
        self.root_path = root_path

    def create_structure(self, structure):
        self._create_recursive(self.root_path, structure)

    def _create_recursive(self, current_path, structure):
        for name, content in structure.items():
            path = os.path.join(current_path, name)
            if content is None:
                open(path, 'w').close()
            else:
                os.makedirs(path, exist_ok=True)
                self._create_recursive(path, content)

    def get_tree(self, path=None):
        target_path = os.path.join(self.root_path, path) if path else self.root_path

        def build_tree(current_path):
            tree = {}
            for item in os.listdir(current_path):
                item_path = os.path.join(current_path, item)
                if os.path.isdir(item_path):
                    tree[item] = build_tree(item_path)
                else:
                    tree[item] = None
            return tree

        return build_tree(target_path)

    def save_tree_to_json(self, output_file, path=None):
        tree = self.get_tree(path)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(tree, f, indent=4, ensure_ascii=False)

    def load_tree_from_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            structure = json.load(f)
        self.create_structure(structure)

    def display_tree(self):
        for root, dirs, files in os.walk(self.root_path):
            level = root.replace(self.root_path, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")

    def add_folder(self, path):
        full_path = os.path.join(self.root_path, path)
        try:
            os.makedirs(full_path, exist_ok=True)
            print(f"Đã tạo thư mục: {full_path}")
        except Exception as e:
            print(f"Lỗi khi tạo thư mục: {e}")

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.root_path, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Đã xóa thư mục: {folder_path}")
        else:
            print(f"Thư mục không tồn tại: {folder_path}")

    def list_folders(self, path=None):
        target_path = os.path.join(self.root_path, path) if path else self.root_path
        if not os.path.exists(target_path):
            print(f"Đường dẫn không tồn tại: {target_path}")
            return []
        return [name for name in os.listdir(target_path)
                if os.path.isdir(os.path.join(target_path, name))]

    def list_files(self, path=None):
        target_path = os.path.join(self.root_path, path) if path else self.root_path
        if not os.path.exists(target_path):
            print(f"Đường dẫn không tồn tại: {target_path}")
            return []
        return [name for name in os.listdir(target_path)
                if os.path.isfile(os.path.join(target_path, name))]

    def rename_folder(self, old_name, new_name):
        old_path = os.path.join(self.root_path, old_name)
        new_path = os.path.join(self.root_path, new_name)
        if os.path.exists(old_path) and os.path.isdir(old_path):
            os.rename(old_path, new_path)
            print(f"Đã đổi tên thư mục: {old_name} → {new_name}")
        else:
            print(f"Thư mục không tồn tại: {old_path}")

    def rename_file(self, folder_path, old_name, new_name):
        full_folder_path = os.path.join(self.root_path, folder_path)
        old_file_path = os.path.join(full_folder_path, old_name)
        new_file_path = os.path.join(full_folder_path, new_name)
        if os.path.exists(old_file_path) and os.path.isfile(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f"Đã đổi tên file: {old_name} → {new_name}")
        else:
            print(f"File không tồn tại: {old_file_path}")
