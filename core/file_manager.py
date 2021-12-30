import json


class FileManager:
    path = None

    def __init__(self, path):
        self.path = path

    def load_from_file(self):
        file = open(self.path, "r")

        data = json.load(file)

        file.close()

        if not self.valid_file(data):
            return None

        return data

    def valid_file(self, data):
        if "application" not in data or "name" not in data:
            return False

        elif data["application"] != "bompy":
            return False

        return True

    def save_to_file(self, data):
        file = open(self.path, "w+")
        file.write(data)
        file.close()
