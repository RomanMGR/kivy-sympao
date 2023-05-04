from kivy.uix.screenmanager import Screen
from Utility.observer import Observer
from kivy.properties import ObjectProperty, ListProperty, ColorProperty


class NbackScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kwargs):
        super(NbackScreenView, self).__init__(**kwargs)
        self.model.add_observer(self)

    def back(self):
        self.manager_screens.current = 'start_screen'

    def model_is_changed(self):
        pass