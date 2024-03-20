from kivy.storage.jsonstore import JsonStore
import uuid
from datetime import datetime


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

    def save_data(self, type_of_test, *args):
        print(args)
        current = datetime.now()
        current_date = current.strftime('%Y-%m-%d')
        current_time = current.strftime('%H:%M:%S')
        n = ''
        for i in args:
            n += str(i) + '\n'
        self.store.put(key=current_date+current_time, date=current_date, time=current_time, type=type_of_test, n=n)

    def get_data(self):
        for i in self.store.find():
            print('result= ', i)
        return self.store
