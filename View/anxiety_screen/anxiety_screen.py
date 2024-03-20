from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from Model.data import questions_anxiety, result_anxiety
from services.screen_transition import ScreenTransitionService


class ContentAnxiety(MDCard):
    text = ""

    def start(self, *args, **kwargs):
        for i in range(len(questions_anxiety[:16])):
            ContentAnxiety.text += str(i + 1) + '. ' + questions_anxiety[i] + '\n'
        self.ids.card_axn_lb.text = ContentAnxiety.text


class AnxietyScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(AnxietyScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.top_bar = None, None, None, None, None, None
        self.lb_1, self.lb_2, self.lb_3, self.lb_4, self.lb_5, self.lb_question = None, None, None, None, None, None
        self.exm_cls = ContentAnxiety()
        self.exm_cls.start()
        self.exm_cls.ids.card_axn_bt.on_press = self.close
        self.count = 0
        self.i = 1
        self.answer = "Ваш результат: "

    def back(self):
        self.ids.scale_box.clear_widgets()
        self.ids.scale_box.add_widget(self.ids.top_app)
        self.ids.scale_box.add_widget(self.ids.scale_inst_lb)
        self.ids.scale_box.add_widget(self.ids.scale_start_btn)
        self.controller.model.export_data.clear()
        self.i = 1
        self.count = 0
        self.answer = "Ваш результат: "
        self.manager_screens.current = 'start_screen'

    def close(self):
        self.remove_widget(self.exm_cls)
        self.btn_1.disabled = False
        self.btn_2.disabled = False
        self.btn_3.disabled = False
        self.btn_4.disabled = False
        self.btn_5.disabled = False

    def get_instruction(self):
        instruction = "Инструкция:" + \
                      "\n" + "\n" + "Вам предлагается 35 вопросов. " \
                                    "\n" + "\n" + "При ответе на каждый вопрос оцените наличие и степень симптомов " \
                                                  "у вас за прошедшую неделю, включая сегодняшний день. "
        return instruction

    def model_is_changed(self):
        if self.i < 35:
            self.lb_question.text = questions_anxiety[self.i]
            self.i += 1
            self.top_bar.text = 'Вопрос №' + str(int(self.i)) + '/35'
        else:
            self.ids.scale_box.remove_widget(self.top_bar)
            self.ids.scale_box.remove_widget(self.btn_1)
            self.ids.scale_box.remove_widget(self.btn_2)
            self.ids.scale_box.remove_widget(self.btn_3)
            self.ids.scale_box.remove_widget(self.btn_4)
            self.ids.scale_box.remove_widget(self.btn_5)
            self.ids.scale_box.remove_widget(self.lb_question)
            export = ''
            if self.count <= 20:
                self.answer += str(self.count) + "\n" + "\n" + result_anxiety[0]
                export = result_anxiety[0]
            elif self.count <= 30:
                self.answer += str(self.count) + "\n" + "\n" + result_anxiety[1]
                export = result_anxiety[1]
            elif self.count <= 80:
                self.answer += str(self.count) + "\n" + "\n" + result_anxiety[2]
                export = result_anxiety[2]
            else:
                self.answer += str(self.count) + "\n" + "\n" + result_anxiety[3]
                export = result_anxiety[3]
            self.ids.scale_box.add_widget(
                MDLabel(text=self.answer, halign='center', font_style='H6', theme_text_color='Primary'))
            self.controller.send_data(self.count, export)
