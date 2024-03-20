from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from Model.data import questions_asthenia, result_asthenia, result_asthenia_2
from kivymd.uix.button import MDRectangleFlatButton

class AstheniaScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(AstheniaScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.top_bar = None, None, None, None, None, None
        self.lb_1, self.lb_2, self.lb_3, self.lb_4, self.lb_5, self.lb_question = None, None, None, None, None, None
        self.count = 0
        self.i = 1
        self.answer = "Ваш результат: " + "\n" + "\n"
        self.answer_list = [0]
        self.top_app = MDTopAppBar(size_hint_y=0.1,  title="Субъективная шкала оценки астении",
                                   left_action_items=[["arrow-left", lambda x: self.back()]])
        self.scale_inst_lb = MDLabel(text=self.get_instruction(), font_style="H6", halign='center')
        self.scale_start_btn = MDRectangleFlatButton(text="Начать тестирование", size_hint=(1, 0.15),
                                                     on_press=lambda bts: self.controller.start())
        self.ids.scale_box.add_widget(self.top_app)
        self.ids.scale_box.add_widget(self.scale_inst_lb)
        self.ids.scale_box.add_widget(self.scale_start_btn)
        self.Flag = False

    def back(self):
        self.ids.scale_box.clear_widgets()
        self.ids.scale_box.add_widget(self.top_app)
        self.ids.scale_box.add_widget(self.scale_inst_lb)
        self.ids.scale_box.add_widget(self.scale_start_btn)
        self.controller.model.export_data.clear()
        self.i = 1
        self.count = 0
        self.answer = "Ваш результат: " + "\n" + "\n"
        self.answer_list = [0]
        self.Flag = False
        self.manager_screens.current = 'start_screen'

    def get_instruction(self):
        instruction = "Инструкция:" + \
                      "\n" + "\n" +"Внимательно прочитайте каждое предложение " \
                      "\n" + "\n" + "Оцените его применительно к вашему состоянию в данный момент. "
        return instruction

    def model_is_changed(self):
        if self.i < 20:
            self.lb_question.text = questions_asthenia[self.i]
            self.i += 1
            self.top_bar.text = 'Вопрос №' + str(int(self.i)) + '/20'
        else:
            self.ids.scale_box.remove_widget(self.top_bar)
            self.ids.scale_box.remove_widget(self.btn_1)
            self.ids.scale_box.remove_widget(self.btn_2)
            self.ids.scale_box.remove_widget(self.btn_3)
            self.ids.scale_box.remove_widget(self.btn_4)
            self.ids.scale_box.remove_widget(self.btn_5)
            self.ids.scale_box.remove_widget(self.lb_question)
            count_list = []
            if self.answer_list[1]+self.answer_list[5]+self.answer_list[12]+self.answer_list[16] <= 12:
                self.answer += result_asthenia[0] + "\n" + "\n"
                comment = result_asthenia[0]
            else:
                self.answer += result_asthenia_2[0] + "\n" + "\n"
                comment = result_asthenia_2[0]
                self.Flag = True
            if self.answer_list[3]+self.answer_list[6]+self.answer_list[10]+self.answer_list[17] <= 12:
                self.answer += result_asthenia[1] + "\n" + "\n"
            else:
                self.answer += result_asthenia_2[1] + "\n" + "\n"
                self.Flag = True
            if self.answer_list[4]+self.answer_list[9]+self.answer_list[15]+self.answer_list[18] <= 12:
                self.answer += result_asthenia[2] + "\n" + "\n"
            else:
                self.answer += result_asthenia_2[2] + "\n" + "\n"
                self.Flag = True
            if self.answer_list[2]+self.answer_list[8]+self.answer_list[14]+self.answer_list[20] <= 12:
                self.answer += result_asthenia[3] + "\n" + "\n"
            else:
                self.answer += result_asthenia_2[3] + "\n" + "\n"
                self.Flag = True
            if self.answer_list[7]+self.answer_list[11]+self.answer_list[13]+self.answer_list[19] <= 12:
                self.answer += result_asthenia[4] + "\n" + "\n"
            else:
                self.answer += result_asthenia_2[4] + "\n" + "\n"
                self.Flag = True
            if self.Flag:
                self.answer += result_asthenia_2[5]
            count_list.append(self.answer_list[1] + self.answer_list[5] + self.answer_list[12] + self.answer_list[16])
            count_list.append(self.answer_list[3]+self.answer_list[6]+self.answer_list[10]+self.answer_list[17])
            count_list.append(self.answer_list[4]+self.answer_list[9]+self.answer_list[15]+self.answer_list[18])
            count_list.append(self.answer_list[2]+self.answer_list[8]+self.answer_list[14]+self.answer_list[20])
            count_list.append(self.answer_list[7]+self.answer_list[11]+self.answer_list[13]+self.answer_list[19])
            self.ids.scale_box.add_widget(MDLabel(text=self.answer, halign='center', font_style='H6', theme_text_color='Primary'))
            self.controller.send_data(self.answer, comment, count_list)
