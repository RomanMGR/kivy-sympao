from View.nback_screen.nback_screen import NbackScreenView
from kivymd.uix.button import MDRectangleFlatButton

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
        self.view.ids.n_start.clear_widgets()
        self.view.ids.n_start.add_widget(MDRectangleFlatButton(text="Start", size_hint=(0.3, 0.5),
                                                               on_press=lambda btn: self.test(), id='n_start_btn'))
        self.view.back()

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

    def test(self):
        self.view.ids.menu_btn.disabled = True
        self.model.test()
        self.view.ids.n_start.clear_widgets()
        self.view.ids.n_start.add_widget(MDRectangleFlatButton(text="Position match", size_hint=(0.3, 0.5), id='nbtn1',
                                                               on_press=lambda btn: self.pos_match(btn)))
        self.view.ids.n_start.add_widget(MDRectangleFlatButton(text="Sound match", size_hint=(0.3, 0.5), id='nbtn2',
                                                               on_press=lambda btn: self.sound_match(btn)))

    def get_view(self) -> NbackScreenView:
        return self.view
