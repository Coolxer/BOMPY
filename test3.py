import nested_lookup as ns
from core.filemanager import FileManager

file_manager = FileManager(
    "F:/CURRENT/USLUGI_SIECIOWE_W_BIZNESIE/PRO/code/target_structure.json"
)

document = file_manager.load_from_file()

# print(nested_lookup("name", document))

# keys = ns.get_all_keys(document)
# print(keys)

size = (100, 300)


def something(s):
    print(s[1])


something(size)

print(size)
