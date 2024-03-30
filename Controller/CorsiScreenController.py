from View.corsi_screen.corsi_screen import CorsiScreenView


class CorsiScreenController:

    def __init__(self, model) -> None:
        self.model = model
        self.view = CorsiScreenView(controller=self, model=self.model)

    def start_test(self):
        self.view.ids.corsi_btn_start.disabled = True
        self.view.ids.corsi_check_bnt.disabled = True
        self.model.start_test()

    def corsi_press(self, n):
        self.model.press_btn(n)

    def active_inversion(self):
        self.model.active_inversion()

    def back(self):
        self.restart()
        self.model.export_data.clear()
        self.view.manager_screens.current = 'start_screen'

    def restart(self):
        try:
            self.model.cancel()
        except:
            pass
        self.view.current_step = 2
        self.view.ids.corsi_step_btn.text = " Длина последовательности          " + str(self.view.current_step) + "/9"
        self.view.result = ''
        self.view.ids.corsi_btn_start.text = "Начать"
        self.view.ids.corsi_btn_start.disabled = False
        self.view.ids.corsi_check_bnt.disabled = False
        self.view.dialog = None
        self.view.dialog_res = None

    def get_view(self) -> CorsiScreenView:
        return self.view
