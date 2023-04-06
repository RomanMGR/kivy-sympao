from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from Model.DeviceScreenModel import DeviceScreenModel


class DeviceScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    name = 'not load'

    def __init__(self, **kwargs):
        super(DeviceScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        print('init device_screen', self)

    def back(self):
        self.manager_screens.current = 'start_screen'
        self.model.discon()

    def name_c(cls, name):
        print(DeviceScreenView.ids)
        DeviceScreenView.ids.named.text = name

    def model_is_changed(self):
        # self.ids.lb_volt.text = DeviceScreenModel.lb_battery_voltage
        name = self.model.get_name()
        self.ids.named.text = name
