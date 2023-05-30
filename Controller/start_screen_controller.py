from View.start_screen.start_screen import StartScreenView
from kivymd.uix.navigationdrawer import MDNavigationLayout

class StartScreenController:
    """
    The `start_screen_controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model) -> None:
        self.model = model
        self.view = StartScreenView(controller=self, model=self.model)

    def scan(self)->None:
        self.view.show_alert_dialog()
        self.model.scanm()

    def on_device_connect_taped(self, device, mac, name):
        self.model.on_device_connect_taped(device, mac, name)

    def drawer1_taped(self):
        self.view.manager_screens.current = "start_screen"
        self.view.ids.nav_drawer.set_state("close")
        print('drawer1 taped!')

    def drawer2_taped(self):
        self.view.manager_screens.current = "nback_screen"
        self.view.ids.nav_drawer.set_state("close")
        self.model.start_n()
        print('drawer2 taped!')

    def drawer3_taped(self):
        self.view.manager_screens.current = "results_screen"
        self.view.ids.nav_drawer.set_state("close")
        self.model.start_results()
        print('drawer3 taped!')

    def get_view(self) -> StartScreenView:
        return self.view
