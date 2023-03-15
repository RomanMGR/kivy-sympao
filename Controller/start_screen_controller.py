from View.start_screen.start_screen import StartScreenView
from Model.DeviceScreenModel import DeviceScreenModel


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
        self.model.scanm()
        self.view.ids.bts.text = 'SCANNING ...'

    def change_screen(self, bts, device):
        DeviceScreenModel.device = device
        self.view.manager_screens.current = 'device_screen'
        DeviceScreenModel().check_volt()

    def get_view(self) -> StartScreenView:
        return self.view
