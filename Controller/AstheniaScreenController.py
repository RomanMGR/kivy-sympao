from View.astenia_screen.asthenia_screen import AstheniaScreenView
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from Model.data import questions_asthenia, answer_asthenia


class AstheniaScreenController:

    def __init__(self, model):
        self.model = model
        self.view = AstheniaScreenView(controller=self, model=self.model)

    def start(self):
        self.view.ids.scale_box.remove_widget(self.view.scale_inst_lb)
        self.view.ids.scale_box.remove_widget(self.view.scale_start_btn)
        self.view.lb_1 = MDLabel(text=answer_asthenia[0], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_2 = MDLabel(text=answer_asthenia[1], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_3 = MDLabel(text=answer_asthenia[2], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_4 = MDLabel(text=answer_asthenia[3], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_5 = MDLabel(text=answer_asthenia[4], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_question = (MDLabel(text=questions_asthenia[0], halign='center', font_style='H6', theme_text_color='Primary',
                                         size_hint=(1, 0.4)))
        self.view.top_bar = MDLabel(text='Вопрос №' + str(int(self.view.i))+'/20', size_hint=(1, 0.1), font_style="H6",
        halign='center')
        self.view.btn_1 = MDRectangleFlatButton(size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 1, "asthenia_screen"))
        self.view.btn_2 = MDRectangleFlatButton(size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 2, "asthenia_screen"))
        self.view.btn_3 = MDRectangleFlatButton(size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 3, "asthenia_screen"))
        self.view.btn_4 = MDRectangleFlatButton(size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 4, "asthenia_screen"))
        self.view.btn_5 = MDRectangleFlatButton(size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 5, "asthenia_screen"))
        self.view.btn_1.add_widget(self.view.lb_1)
        self.view.btn_2.add_widget(self.view.lb_2)
        self.view.btn_3.add_widget(self.view.lb_3)
        self.view.btn_4.add_widget(self.view.lb_4)
        self.view.btn_5.add_widget(self.view.lb_5)
        self.view.ids.scale_box.add_widget(self.view.top_bar)
        self.view.ids.scale_box.add_widget(self.view.lb_question)
        self.view.ids.scale_box.add_widget(self.view.btn_1)
        self.view.ids.scale_box.add_widget(self.view.btn_2)
        self.view.ids.scale_box.add_widget(self.view.btn_3)
        self.view.ids.scale_box.add_widget(self.view.btn_4)
        self.view.ids.scale_box.add_widget(self.view.btn_5)
        self.model.export_data.react_time_pos('start')

    def send_data(self, export, comment, count_list):
        self.model.send_data(export, comment, count_list)

    def get_view(self) -> AstheniaScreenView:
        return self.view