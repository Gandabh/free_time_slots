class CustomList(list):
    def remove_if_exist(self, item):
        try:
            self.remove(item)
        except ValueError:
            # print(f'{item} not in list')
            pass