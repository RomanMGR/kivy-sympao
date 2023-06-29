from kivy.properties import ObjectProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from services.save_data import SaveData
from kivy.uix.button import Button


class ResultsScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    bar_color1 = ColorProperty([1.0, 0.0, 0.0, 0.9])
    bar_inactive_color1 = ColorProperty([0.0, 1.0, 0.0, 0.9])
    savedata = SaveData()
    uuid = "None"

    def __init__(self, **kwargs):
        super(ResultsScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.result_list = {}

    def start(self):
        self.result_list = self.savedata.get_data()
        self.ids.result_list.add_widget(Button(
                text=('uuid:' + str(self.savedata.get_uuid())),
                markup=True, size_hint_y=None, height=100, size_hint_x=1, halign="left"))
        self.model_is_changed()

    def back(self):
        self.ids.result_list.clear_widgets()
        self.manager_screens.current = 'start_screen'

    def model_is_changed(self):
        for i in self.result_list.find():
            n = "Попытка №" + str(int(i[0])+1)
            result = str(i[1]['result'])+'%'
            n_back = str(i[1]['n'])
            self.ids.result_list.add_widget(Button(
                text=('[size=60]' + '[b]' + n + '[/size]' + '\n' + 'Итоговый счет:  ' + '[/b]' + result + '\n'
                      + 'Н-назад:  ' + '[/b]' + n_back),
                markup=True, size_hint_y=None, height=250, size_hint_x=1, halign="left"))
