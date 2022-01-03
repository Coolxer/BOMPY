from core.scene_manager import SceneManager
from core.file_manager import FileManager

# klasa przechowująca wartości globalne w obrębie programu
class Store:
    def __init__(self):
        self.window = None
        self.scene_manager = None
        self.project_name = None
        self.file_path = None
        self.data = {}
        self.selected_item = None
        self.identifier = None

    def set_window(self, window):
        self.window = window

    def get_window(self):
        return self.window

    def get_scene_manager(self):
        return SceneManager(self.window)

    def get_file_manager(self):
        return FileManager()

    def set_project_name(self, name):
        self.project_name = name

    def get_project_name(self):
        return self.project_name

    def set_file_path(self, path):
        self.file_path = path

    def get_file_path(self):
        return self.file_path

    def set_data(self, data):
        self.data = data

    def get_data(
        self,
    ):
        return self.data

    def set_item(self, item, identifier):
        item["values"].insert(0, identifier)
        self.selected_item = item
        self.identifier = identifier

    def get_item(self):
        return self.selected_item

    def get_identifier(self):
        return self.identifier


instance = Store()
