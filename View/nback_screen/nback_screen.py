from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty, ListProperty, ColorProperty, StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window


class Content_device_n(BoxLayout):
    pass


class Content_result(BoxLayout):
    text_result = '12345'


class NbackScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    dialog = None
    dialog_res = None
    total = '0'
    total_pos = 0
    total_s = 0
    step = '1'
    result = 0

    def __init__(self, **kwargs):
        super(NbackScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        menu_items = [
            {
                'text': f'n={i}',
                'viewclass': 'OneLineListItem',
                'on_release': lambda x=f'{i}': self.controller.press_n1(x),
            } for i in range(1, 4, 1)
        ]
        menu2_items = [
            {
                'text': f'n={i}',
                'viewclass': 'OneLineListItem',
                'on_release': lambda x=f'{i}': self.controller.press_n2(x),
            } for i in range(20, 60, 10)
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.menu_btn,
            items=menu_items,
            width_mult=2
        )
        self.menu_2 = MDDropdownMenu(
            caller=self.ids.menu2_btn,
            items=menu2_items,
            width_mult=3
        )
        # self.snackbar = Snackbar(text="Отправка сообщения", snackbar_x="10dp", snackbar_y='24dp')

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(title="Инструкция",buttons=[
                MDFlatButton(text="Продолжить", on_release=lambda bts: self.close_dialog())
            ], type="custom", content_cls=Content_device_n())
        self.dialog.open()

    def show_result_dialog(self):
        Content_result.text_result = str("Суммарный: "+ str(self.total) + '/' + str(self.model.result) +
                 '\n' + 'Позициональный: ' + str(self.total_pos) + '/' + str(self.model.result_pos) + '\n' +\
                 'Звуковой: ' + str(self.total_s) + '/' + str(self.model.result_s))
        if not self.dialog_res:
            self.dialog_res = MDDialog(title='Ваш результат:  ' + str(self.result) + '%', buttons=[
            MDFlatButton(text="Продолжить", on_release=lambda bts: self.close_res())
            ], type="custom", content_cls=Content_result())
        self.dialog_res.open()

    def close_dialog(self):
        self.dialog.dismiss()

    def close_res(self):
        self.controller.restart()
        self.dialog_res.dismiss()
        self.dialog_res = None

    def back(self):
        self.manager_screens.current = 'start_screen'

    def model_is_changed(self):
        pass
