from View.scab_screen.scab_screen import ScabScreenView
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel


class ScabScreenController:

    def __init__(self, model):
        self.model = model
        self.view = ScabScreenView(controller=self, model=self.model)
        self.Flag = False

    def start(self, **kwargs):
        self.view.ids.scab_box.remove_widget(self.view.scab_start_btn)
        self.view.ids.scab_box.remove_widget(self.view.scab_inst_lb)
        self.view.btn_1 = MDRectangleFlatButton(md_bg_color="red", size_hint=(1, 0.15), on_press=lambda btn: self.scab_btn(btn, 'Красный'))
        self.view.btn_2 = MDRectangleFlatButton(md_bg_color="yellow", size_hint=(1, 0.15), on_press=lambda btn: self.scab_btn(btn, 'Желтый'))
        self.view.btn_3 = MDRectangleFlatButton(md_bg_color="blue", size_hint=(1, 0.15), on_press=lambda btn: self.scab_btn(btn, 'Синий'))
        self.view.btn_4 = MDRectangleFlatButton(md_bg_color="black", size_hint=(1, 0.15), on_press=lambda btn: self.scab_btn(btn, 'Черный'))
        self.view.btn_5 = MDRectangleFlatButton(md_bg_color="green", size_hint=(1, 0.15), on_press=lambda btn: self.scab_btn(btn, 'Зеленый'))
        self.view.lbl_txt = MDLabel(text="Тест", size_hint_y=0.35, theme_text_color="Custom", halign='center', font_style='H4')
        self.view.bar = MDLabel(text='Вопрос №' + str(int(self.model.current_element+1))+'/60', size_hint=(1, 0.1), font_style="H6",
        halign='center')
        self.view.ids.scab_box.add_widget(self.view.bar)
        self.view.ids.scab_box.add_widget(self.view.lbl_txt)
        self.view.ids.scab_box.add_widget(self.view.btn_1)
        self.view.ids.scab_box.add_widget(self.view.btn_2)
        self.view.ids.scab_box.add_widget(self.view.btn_3)
        self.view.ids.scab_box.add_widget(self.view.btn_4)
        self.view.ids.scab_box.add_widget(self.view.btn_5)
        self.Flag = True
        self.model.start()

    def scab_btn(self, btn, n):
        self.model.press_btn(n)

    def reset(self):
        self.model.current_element = 0
        self.model.list_sector.clear()
        self.model.color_sector.clear()
        self.model.time.clear()
        self.model.total_first = 30
        self.model.total_second = 30
        self.view.result = ''
        self.Flag = False

    def restart(self):
        self.reset()
        self.view.ids.scab_box.remove_widget(self.view.btn_1)
        self.view.ids.scab_box.remove_widget(self.view.btn_2)
        self.view.ids.scab_box.remove_widget(self.view.btn_3)
        self.view.ids.scab_box.remove_widget(self.view.btn_4)
        self.view.ids.scab_box.remove_widget(self.view.btn_5)
        self.view.ids.scab_box.remove_widget(self.view.lbl_txt)
        self.view.ids.scab_box.remove_widget(self.view.bar)
        self.view.ids.scab_box.add_widget(self.view.scab_inst_lb)
        self.view.ids.scab_box.add_widget(self.view.scab_start_btn)
        self.Flag = False

    def get_view(self) -> ScabScreenView:
        return self.view