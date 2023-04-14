from View.start_screen.start_screen import StartScreenView
from kivy.lang import Builder
from Model.DeviceScreenModel import DeviceScreenModel
from View.device_screen.device_screen import DeviceScreenView


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
        # DeviceScreenModel.device = device
        # DeviceScreenView.name_c(name)
        # self.view.manager_screens.current = 'device_screen'
        # DeviceScreenView.model2.check_volt()
        self.model.on_device_connect_taped(device, mac, name)

    def get_view(self) -> StartScreenView:
        return self.view
