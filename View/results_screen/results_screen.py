from kivy.properties import ObjectProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from services.save_data import SaveData
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class ContentResultScreen(BoxLayout):
    text_result = '12345'


class ResultsScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    bar_color1 = ColorProperty([1.0, 0.0, 0.0, 0.9])
    bar_inactive_color1 = ColorProperty([0.0, 1.0, 0.0, 0.9])
    savedata = SaveData()
    dialog = None
    uuid = "None"

    def __init__(self, **kwargs):
        super(ResultsScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.result_list = {}

    def start(self):
        self.ids.result_list.clear_widgets()
        self.result_list = self.savedata.get_data()
        self.ids.result_list.add_widget(Button(
                text=('uuid:' + str(self.savedata.get_uuid())),
                markup=True, size_hint_y=None, height=100, size_hint_x=1, halign="left"))
        self.model_is_changed()

    def back(self):
        self.ids.result_list.clear_widgets()
        self.manager_screens.current = 'start_screen'

    def show_bar(self, type, date, time, n):
        ContentResultScreen.text_result = date + '\n' + time + '\n' + n
        self.dialog = MDDialog(title=type, buttons=[
            MDFlatButton(text="Закрыть", on_release=lambda bts: self.close_dialog())], type="custom",
                               content_cls=ContentResultScreen())
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()
        ContentResultScreen.text_result = ''

    def model_is_changed(self):
        for i in self.result_list.find():
            date = 'Дата: ' + str(i[1]['date'])
            time = 'Время: ' + str(i[1]['time'])
            n = str(i[1]['n'])
            type_test = str(i[1]['type'])
            self.ids.result_list.add_widget(Button(
                text=('[size=60]' + '[b]' + 'Тип теста:  ' + type_test +'\n' + date + '\n' + time + '[/b]' + '[/size]'),
                markup=True, size_hint_y=None, height=250, size_hint_x=1,
                on_press=lambda bts, type_test=type_test, date=date, time=time, n=n: self.show_bar(type_test, date, time, n)))
