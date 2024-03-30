from View.device_screen.device_screen import DeviceScreenView
from kivymd.uix.segmentedcontrol.segmentedcontrol import MDSegmentedControl, MDSegmentedControlItem


class DeviceScreenController:
    """
    The `start_screen_controller` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model) -> None:
        self.model = model
        self.view = DeviceScreenView(controller=self, model=self.model)

    def send_anode(self, n, checkbox, value):
        if value:
            self.model.send_anode(n)

    def send_amp(self):
        self.model.send_amp(self.view.ids.slider_amp_id.value)

    def send_dlit(self):
        self.model.send_dlit(self.view.ids.slider_dlit_id.value)

    def send_chast(self):
        self.model.send_chast(self.view.ids.slider_chast_id.value)

    def send_segment(self, n) -> None:
        print('n', str(n))
        self.model.send_segment(n)
        self.view.slider_amp_text = 0
        self.view.ids.slider_amp_id.value = 0
        self.model.parameters[0] = 0
        self.view.ids.text_field_id.text = str(0)

    def get_view(self) -> DeviceScreenView:
        return self.view