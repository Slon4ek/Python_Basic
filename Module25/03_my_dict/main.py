class MyDict(dict):
    def __init__(self):
        super().__init__()

    def get(self, key):
        if key in self.keys():
            return self.__getitem__(key)
        else:
            return 0


my_dict = MyDict()
my_dict['asd'] = 23
my_dict['zxc'] = 432
print(my_dict)
print(my_dict.get('asdasdas'))
print(my_dict.get('asd'))
