from core.filemanager import FileManager


file_manager = FileManager(
    "F:/CURRENT/USLUGI_SIECIOWE_W_BIZNESIE/PRO/code/target_structure.json"
)

data = file_manager.load_from_file()

selected = "material"

for item in data:
    print(item)
