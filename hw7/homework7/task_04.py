# create a dictionary with access by attributes:  read the data with a sign separation '='
# and checking for the contents of the digits
class KeyValueStorage:
    def __init__(self, file_path: str):
        with open(file_path) as file:
            self.attr_dict = {
                f"{line.strip().split('=')[0]}": line.strip().split("=")[1] if not line.strip().split("=")[
                    1].isdigit() else int(line.strip().split("=")[1])
                for line in file}
            self.name = self.attr_dict["name"]
            self.last_name = self.attr_dict["last_name"]
            self.power = self.attr_dict["power"]
            self.song = self.attr_dict["song"]

# when a value cannot be assigned to an attribute, Value Error is raised
    def __getitem__(self, item):
        try:
            __item = self.attr_dict[item]
        except Exception:
            raise ValueError("Incorrect key")
        else:
            return __item


storage = KeyValueStorage("tasks/task_04.txt")

print(storage['name'])
print(storage['last_name'])
print(storage['song'])
print(storage['power'])
print("----------------")
print(storage.name)
print(storage.last_name)
print(storage.power)
print(storage.song)
