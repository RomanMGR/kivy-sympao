import os

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty, ColorProperty
from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.uix.button import Button


class StartScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    devices_list = ObjectProperty()
    bar_color1 = ColorProperty([1.0, 0.0, 0.0, 0.9])
    bar_inactive_color1 = ColorProperty([0.0, 1.0, 0.0, 0.9])


    def __init__(self, **kwargs):
        super(StartScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)
        print('init ',self)

    def model_is_changed(self):
        for device in self.model.scanned_devices:
            name = str(device.name)
            print(device.name)
            MAC = str(device.address)
            self.ids.devices_list.add_widget(Button(
                text=('[size=60]' + '[b]' + name + '[/size]' + '\n' + 'MAC:  ' + '[/b]' + MAC),
                markup=True, size_hint_y=None, height=300, size_hint_x=1,
                on_press = lambda name=name, MAC=MAC: self.controller.change_screen(name, MAC)))
        self.ids.devices_list.bind(minimum_height=self.ids.devices_list.setter('height'))
        self.ids.bts.text = "scan"

