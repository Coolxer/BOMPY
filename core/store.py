from core.scene_manager import SceneManager


class Store:
    def __init__(self):
        self.scene_manager = None
        self.data = {}
        self.selected_item = None

    def set_scene_manager(self, window):
        self.scene_manager = SceneManager(window)

    def get_scene_manager(self):
        return self.scene_manager

    def call_switch_scene(self, scene_index):
        self.scene_manager.switch_scene(scene_index)

    def set_data(self, data):
        self.data = data

    def get_data(
        self,
    ):
        return self.data

    def set_item(self, item):
        self.selected_item = item

    def get_item(self):
        return self.selected_item


instance = Store()
