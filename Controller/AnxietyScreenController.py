from View.anxiety_screen.anxiety_screen import AnxietyScreenView
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.expansionpanel import MDExpansionPanel
from Model.data import questions_anxiety, answer_anxiety
from kivymd.uix.boxlayout import MDBoxLayout


class AnxietyScreenController:

    def __init__(self, model):
        self.model = model
        self.view = AnxietyScreenView(controller=self, model=self.model)
        self.panel = None

    def show_panel(self, instance, value):
        self.view.btn_1.disabled = True
        self.view.btn_2.disabled = True
        self.view.btn_3.disabled = True
        self.view.btn_4.disabled = True
        self.view.btn_5.disabled = True
        self.view.add_widget(self.view.exm_cls)

    def start(self):
        self.view.ids.scale_box.remove_widget(self.view.ids.scale_inst_lb)
        self.view.ids.scale_box.remove_widget(self.view.ids.scale_start_btn)
        self.view.lb_1 = MDLabel(text=answer_anxiety[0], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_2 = MDLabel(text=answer_anxiety[1], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_3 = MDLabel(text=answer_anxiety[2], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_4 = MDLabel(text=answer_anxiety[3], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_5 = MDLabel(text=answer_anxiety[4], halign='center', font_style='H6', theme_text_color='Primary')
        self.view.lb_question = (MDLabel(text=questions_anxiety[0], size_hint=(1, 0.4), markup=True,
                                       halign='center', font_style='H6', theme_text_color='Primary'))
        self.view.lb_question.bind(on_ref_press=self.show_panel)
        self.view.top_bar = MDLabel(text='Вопрос №' + str(int(self.view.i))+'/35', size_hint=(1, 0.1), font_style="H6",
        halign='center')
        self.view.btn_1 = MDRectangleFlatButton(id='sc_btn1', size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 0, "anxiety_screen"))
        self.view.btn_2 = MDRectangleFlatButton(id='sc_btn2', size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 1, "anxiety_screen"))
        self.view.btn_3 = MDRectangleFlatButton(id='sc_btn3', size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 2, "anxiety_screen"))
        self.view.btn_4 = MDRectangleFlatButton(id='sc_btn4', size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 3, "anxiety_screen"))
        self.view.btn_5 = MDRectangleFlatButton(id='sc_btn5', size_hint=(1, 0.12),
                                           on_press=lambda btn: self.model.choose(btn, 4, "anxiety_screen"))
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

    def send_data(self, count, export):
        self.model.send_data(count, export)

    def get_view(self) -> AnxietyScreenView:
        return self.view