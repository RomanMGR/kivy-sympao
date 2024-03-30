from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import BoxLayout


class Content_device_corsi(BoxLayout):
    pass


class Content_result_corsi(BoxLayout):
    text_result = '12345'


class CorsiScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    current_step = 2
    result = ''
    dialog = None
    dialog_res = None

    def __init__(self, **kwargs):
        super(CorsiScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(title="Инструкция",buttons=[
                MDFlatButton(text="Продолжить", on_release=lambda bts: self.close_dialog())
            ], type="custom", content_cls=Content_device_corsi())
        self.dialog.open()

    def show_result_dialog(self):
        Content_result_corsi.text_result = str(self.result)
        if not self.dialog_res:
            self.dialog_res = MDDialog(title='Ваш результат:  ', buttons=[
            MDFlatButton(text="Продолжить", on_release=lambda bts: self.close_res())
            ], type="custom", content_cls=Content_result_corsi())
        self.dialog_res.open()

    def close_dialog(self):
        self.dialog.dismiss()

    def close_res(self):
        self.dialog_res.dismiss()
        self.controller.restart()
        self.dialog_res = None

    def model_is_changed(self):
        if self.current_step < 9:
            self.current_step += 1
            self.ids.corsi_step_btn.text = " Длина последовательности        " + str(self.current_step) + "/9"
