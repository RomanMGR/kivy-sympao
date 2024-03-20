from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


class Content_result_scab(BoxLayout):
    text_result = '12345'


class ScabScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(ScabScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.lbl_txt = None, None, None, None, None, None
        self.bar = None
        self.scab_inst_lb = MDLabel(text=self.get_instruction(), font_style="H6", halign='center')
        self.scab_start_btn = MDRectangleFlatButton(text="Начать тестирование", size_hint=(1, 0.15),
                                                    on_press=lambda btn: self.controller.start())
        self.ids.scab_box.add_widget(self.scab_inst_lb)
        self.ids.scab_box.add_widget(self.scab_start_btn)
        self.dialog_res = None
        self.result = ''


    def show_result_dialog(self):
        Content_result_scab.text_result = str(self.result)
        if not self.dialog_res:
            self.dialog_res = MDDialog(title='Ваш результат:  ', buttons=[
                MDFlatButton(text="Продолжить", on_release=lambda bts: self.close_res())
            ], type="custom", content_cls=Content_result_scab())
        self.dialog_res.open()

    def close_res(self):
        self.dialog_res.dismiss()
        self.dialog_res = None

    def get_instruction(self):
        instruction = "Инструкция:" + \
                      "\n" + "\n" + "В первом этапе теста выберите в палитре ниже тот цвет, который написан черным текстом на предъявляемых карточках." \
                      "\n" + "\n" + "Во втором выберите цвет надписи, независимо от значения слова." \
                      "\n" + "\n" + "Выбирайте цвет как можно быстрее"
        return instruction

    def restart(self):
        self.controller.restart()

    def back(self):
        if self.controller.Flag:
            self.ids.scab_box.remove_widget(self.btn_1)
            self.ids.scab_box.remove_widget(self.btn_2)
            self.ids.scab_box.remove_widget(self.btn_3)
            self.ids.scab_box.remove_widget(self.btn_4)
            self.ids.scab_box.remove_widget(self.btn_5)
            self.ids.scab_box.remove_widget(self.lbl_txt)
            self.ids.scab_box.remove_widget(self.bar)
            self.ids.scab_box.add_widget(self.scab_inst_lb)
            self.ids.scab_box.add_widget(self.scab_start_btn)
        self.controller.reset()
        self.controller.model.export_data.clear()
        self.manager_screens.current = 'start_screen'

    def model_is_changed(self):
        self.bar.text = 'Вопрос №' + str(int(self.model.current_element+1))+'/60'