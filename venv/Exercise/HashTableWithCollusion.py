class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def print(self):
        print(self.arr)

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((kay, value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


table = HashTable()
table["primary 1"] = 45
table["primary 2"] = 77
table["primary 3"] = 120

del table["primary 2"]

print(table["primary 3"])
table.print()