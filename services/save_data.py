from kivy.storage.jsonstore import JsonStore


class SaveData:

    def __init__(self):
        self.store = JsonStore('Simp.json')

    def save_data(self, result):
        key = len(self.store)
        self.store.put(key=key, result=result)

    def get_data(self):
        for i in self.store.find():
            print('result= ', i)
        return self.store
