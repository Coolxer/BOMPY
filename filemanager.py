import json


class FileManager:
    path = None

    def __init__(self, path):
        self.path = path

    def load_from_file(self):
        file = open(self.path, "r")

        data = json.load(file)

        file.close()

        # if not self.valid_file(data):
        #    return

        return data

    def valid_file(self, data):
        return 1

    def save_to_file(self, data):
        file = open(self.path, "w+")
        file.write(data)
        file.close()
