from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty, ListProperty, ColorProperty


class DeviceScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(DeviceScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        print('init device_screen', self)

    def back(self):
        self.manager_screens.current = 'start_screen'
        self.model._task.cancel()

    def model_is_changed(self):
        self.ids.lb_volt.text = self.model.lb_battery_voltage
