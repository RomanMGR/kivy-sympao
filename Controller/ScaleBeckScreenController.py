from View.scale_beck_screen.scale_beck_screen import ScaleBeckScreenView
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from Model.data import questions_scale


class ScaleBeckScreenController:

    def __init__(self, model):
        self.model = model
        self.view = ScaleBeckScreenView(controller=self, model=self.model)
        self.choice_1, self.choice_2, self.choice_3, self.choice_4 = questions_scale[0], questions_scale[1], questions_scale[2], questions_scale[3]

    def start(self):
        self.view.ids.scale_box.remove_widget(self.view.ids.scale_inst_lb)
        self.view.ids.scale_box.remove_widget(self.view.ids.scale_start_btn)
        self.view.lb_1 = MDLabel(text=self.choice_1, halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_2 = MDLabel(text=self.choice_2, halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_3 = MDLabel(text=self.choice_3, halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_4 = MDLabel(text=self.choice_4, halign='center', font_style='H6', theme_text_color='Primary')
        self.view.top_bar = MDLabel(text='Вопрос №' + str(int(self.view.i/4))+'/21', size_hint=(1, 0.1), font_style="H6",
        halign='center')
        self.view.btn_1 = MDRectangleFlatButton(id='sc_btn1', size_hint=(1, 0.25),
                                           on_press=lambda btn: self.model.choose(btn, 0, "scale_beck_screen"))
        self.view.btn_2 = MDRectangleFlatButton(id='sc_btn2', size_hint=(1, 0.25),
                                           on_press=lambda btn: self.model.choose(btn, 1, "scale_beck_screen"))
        self.view.btn_3 = MDRectangleFlatButton(id='sc_btn3', size_hint=(1, 0.25),
                                           on_press=lambda btn: self.model.choose(btn, 2, "scale_beck_screen"))
        self.view.btn_4 = MDRectangleFlatButton(id='sc_btn4', size_hint=(1, 0.25),
                                           on_press=lambda btn: self.model.choose(btn, 3, "scale_beck_screen"))
        self.view.btn_1.add_widget(self.view.lb_1)
        self.view.btn_2.add_widget(self.view.lb_2)
        self.view.btn_3.add_widget(self.view.lb_3)
        self.view.btn_4.add_widget(self.view.lb_4)
        self.view.ids.scale_box.add_widget(self.view.top_bar)
        self.view.ids.scale_box.add_widget(self.view.btn_1)
        self.view.ids.scale_box.add_widget(self.view.btn_2)
        self.view.ids.scale_box.add_widget(self.view.btn_3)
        self.view.ids.scale_box.add_widget(self.view.btn_4)
        self.model.export_data.react_time_pos('start')

    def send_data(self, count, comment):
        self.model.send_data(count, comment)

    def get_view(self) -> ScaleBeckScreenView:
        return self.view
