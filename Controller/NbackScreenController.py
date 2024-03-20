from View.nback_screen.nback_screen import NbackScreenView
from kivymd.uix.button import MDRectangleFlatIconButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class NbackScreenController:

    def __init__(self, model) -> None:
        self.model = model
        self.view = NbackScreenView(controller=self, model=self.model)

    def show_menu(self):
        self.model.show_menu()

    def back(self):
        try:
            self.model.cancel()
        except:
            pass
        self.view.ids.progress.value = 0
        self.view.ids.menu2_btn.text = '0/20'
        self.view.ids.n_start.clear_widgets()
        self.view.ids.n_start.add_widget(MDRectangleFlatButton(text="Начать", size_hint=(0.3, 0.75),
                                                               on_press=lambda btn: self.test(), id='n_start_btn'))
        self.model.export_data.clear()
        self.view.back()

    def restart(self):
        self.view.ids.progress.value = 0
        self.view.ids.menu2_btn.text = '0/20'
        self.view.ids.n_start.clear_widgets()
        self.view.ids.n_start.add_widget(MDRectangleFlatButton(text="Начать", size_hint=(0.3, 0.75),
                                                               on_press=lambda btn: self.test(), id='n_start_btn'))
        self.model.restart()

    def pos_match(self, btn):
        self.model.pos_match(btn)
        btn.disabled = True

    def sound_match(self, btn):
        self.model.sound_match(btn)
        btn.disabled = True

    def press_n1(self, n):
        self.view.ids.menu_btn.text = 'n = '+str(n)
        self.model.n = int(n)
        print(self.model.n)
        self.view.menu.dismiss()

    def press_n2(self, n):
        self.view.ids.menu2_btn.text = '0/'+str(n)
        self.model.len_step = int(n)
        self.view.menu_2.dismiss()

    def test(self):
        self.view.ids.menu_btn.disabled = True
        self.view.ids.menu2_btn.disabled = True
        self.model.test()
        self.view.ids.n_start.clear_widgets()
        self.view.ids.n_start.add_widget(MDRectangleFlatIconButton(size_hint=(0.3,  1), id='nbtn1', icon='rectangle', icon_size='72sp',
                                                               on_press=lambda btn: self.pos_match(btn), halign='right'))
        self.view.ids.n_start.add_widget(MDRectangleFlatIconButton(size_hint=(0.3, 1), id='nbtn2', icon='music', icon_size='72sp',
                                                      on_press=lambda btn: self.sound_match(btn), halign='right'))

    def get_view(self) -> NbackScreenView:
        return self.view
