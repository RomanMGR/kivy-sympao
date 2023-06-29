from kivy.storage.jsonstore import JsonStore
import uuid


class SaveData:

    def __init__(self):
        self.store = JsonStore('Simp.json')
        self.store_uuid = JsonStore('Simp_uuid.json')

    def get_uuid(self):
        if not self.store_uuid.exists('uuid'):
            id_uuid = uuid.uuid4()
            self.store_uuid.put(key='uuid', uuid=str(id_uuid))
            print(id_uuid)
        for i in self.store_uuid.find():
            return str(i[1]['uuid'])

    def save_data(self, result, n_back):
        key = len(self.store)
        self.store.put(key=key, result=result, n=n_back)

    def get_data(self):
        for i in self.store.find():
            print('result= ', i)
        return self.store
