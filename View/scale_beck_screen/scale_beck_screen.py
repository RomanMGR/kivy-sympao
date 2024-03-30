from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from Model.data import questions_scale, results_scale


class ScaleBeckScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(ScaleBeckScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.top_bar = None, None, None, None, None
        self.lb_1, self.lb_2, self.lb_3, self.lb_4 = None, None, None, None
        self.count = 0
        self.i = 4
        self.answer = "Ваш результат: "

    def back(self):
        self.ids.scale_box.clear_widgets()
        self.ids.scale_box.add_widget(self.ids.top_app)
        self.ids.scale_box.add_widget(self.ids.scale_inst_lb)
        self.ids.scale_box.add_widget(self.ids.scale_start_btn)
        self.i = 4
        self.count = 0
        self.answer = "Ваш результат: "
        self.controller.model.export_data.clear()
        self.manager_screens.current = 'start_screen'

    def get_instruction(self):
        instruction = "Инструкция:" + \
                      "\n" + "\n" +"Вам предлагается ряд утверждений. " \
                      "\n" + "\n" + "Выберите одно утверждение в каждой группе, которое лучше всего описывает " \
                      "Ваше состояние за прошедшую неделю, включая сегодняшний день. " + "\n" + "\n" + \
                      "Прежде чем сделать выбор, внимательно прочтите все утверждения в каждой группе."
        return instruction

    def model_is_changed(self):
        if self.i < 84:
            self.choice_1, self.choice_2, self.choice_3, self.choice_4 = questions_scale[self.i + 0], questions_scale[self.i + 1], \
                                                                         questions_scale[self.i + 2], questions_scale[self.i + 3]
            self.lb_1.text, self.lb_2.text, self.lb_3.text, self.lb_4.text = self.choice_1, self.choice_2, self.choice_3, self.choice_4
            self.btn_1.clear_widgets(), self.btn_2.clear_widgets(), self.btn_3.clear_widgets(), self.btn_4.clear_widgets()
            self.btn_1.add_widget(self.lb_1)
            self.btn_2.add_widget(self.lb_2)
            self.btn_3.add_widget(self.lb_3)
            self.btn_4.add_widget(self.lb_4)
            self.i += 4
            self.top_bar.text = 'Вопрос №' + str(int(self.i / 4)) + '/21'
        else:
            self.ids.scale_box.remove_widget(self.top_bar)
            self.ids.scale_box.remove_widget(self.btn_1)
            self.ids.scale_box.remove_widget(self.btn_2)
            self.ids.scale_box.remove_widget(self.btn_3)
            self.ids.scale_box.remove_widget(self.btn_4)
            export = ''
            if self.count <= 9:
                self.answer += str(self.count) + "\n" + "\n" + results_scale[0]
                export = results_scale[0]
            elif self.count <= 18:
                self.answer += str(self.count) + "\n" + "\n" + results_scale[1]
                export = results_scale[1]
            elif self.count <= 29:
                self.answer += str(self.count) + "\n" + "\n" + results_scale[2]
                export = results_scale[2]
            else:
                self.answer += str(self.count) + "\n" + "\n" + results_scale[3]
                export = results_scale[3]
            self.ids.scale_box.add_widget(MDLabel(text=self.answer, halign='center', font_style='H6', theme_text_color='Primary'))
            self.controller.send_data(self.count, export)

